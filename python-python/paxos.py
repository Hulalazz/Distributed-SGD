# ------------------------------------------------------------
# Implements a Paxos server and runs Paxos with this server. 
# This function is called through run_paxos if the client_server
# has gone down.
# ------------------------------------------------------------

from __future__ import print_function
from __future__ import absolute_import
from grpc.beta import implementations
import time
import sys
from threading import Thread

import paxos_pb2
import argparse
import traceback

import autograd.numpy as np
import autograd.numpy.random as npr
from autograd import grad
import random

from protobuf_utils.utils import * 
from server_utils.utils import * 

import subprocess

_TIMEOUT_SECONDS = 4
PAXOS_PORT_STR = 50052

# Actual implementation of the PaxosServer that is used to communicate between the clients. 
# Paxos is called to determine the future main server from amongst many different clients.
class PaxosServer(paxos_pb2.BetaPaxosServerServicer):
    def __init__(self, hostname):
    	# Initial consensus value is none, this will be the server
    	self.new_server = ''
    	self.consensus_value = None
    	self.consensus_reached = False

    	# Values for paxos 
    	self.n = random.random()
    	self.prop_n = 0
    	self.v = ''
    	self.n_v = 0

    	# Exponential backoff to prevent spamming other servers 
    	# Randomness is introduced to help Paxos converge quicker
    	self.backoff = (1 * random.gauss(1, 0.25))
    	if self.backoff < 0:
    		self.backoff = 1

    	# Saves the server's address as well
    	self.address = hostname

    # Runs the prepare phase of the Paxos algorithm
    def prepare(self, request, context):
    	# Update the highest seen proposal
    	if request.n > self.prop_n:
    		self.prop_n = request.n 
    	# Returns an acknowledgement containing highest accepted proposal
    	return paxos_pb2.ack(n=self.n, v=self.v, n_v=self.n_v)

    # Accepts the proposal if it is higher than  
    def accept(self, request, context):
    	if request.n >= self.prop_n:
    		self.n_v = request.n
    		self.v = request.v
    		self.n = request.n
        	return paxos_pb2.acquiescence(accept_bool=True)
        else:
        	return paxos_pb2.acquiescence(accept_bool=False)

    # Notifies the server that consensus has been reached
    def accepted(self, request, context):
    	self.consensus_reached = True
    	self.new_server = request.v
    	return paxos_pb2.empty()

    # Ping function to allow confirmation between PaxosServer that they
    # are still running
    def ping(self, request, context):
    	return paxos_pb2.empty() 

# Runs the PaxosServer. Checks periodically to see if a consensus has 
# been reached.
def run_server(server, paxos_server):
	server.start()
	while True:
		time.sleep(0.1)
		try:
			if paxos_server.consensus_reached:
				if paxos_server.new_server != '':
					log_info('Consensus reached, server shutting down')
				# Wait briefly for the consensus message to propogate out
				time.sleep(5)
				server.stop(0)
				break
			time.sleep(1)
		except KeyboardInterrupt:
			server.stop(0)

# Actually instantiates the Paxos Server according to a defined port
def create_server(hostname, local_id):
    # Allow argument that allows this parameter to be changsed
	paxos_server = PaxosServer(hostname) 
	server = paxos_pb2.beta_create_PaxosServer_server(paxos_server)
	if local_id is None:
		server.add_insecure_port(hostname + ':' + str(PAXOS_PORT_STR))
	else:
		server.add_insecure_port(hostname)
	return paxos_server, server

# Attempts to send proposals to all the other servers
def send_proposals(server_stubs, self_paxos_server):
	# Increments the proposal number from the previous one that it sends out
	self_paxos_server.n = self_paxos_server.n * (1 + random.random())
	self_paxos_server.v = self_paxos_server.address
	n_proposal = self_paxos_server.n
	value = self_paxos_server.address
	log_info('Making a proposal from {0} for n = {1} '.format(self_paxos_server.address, n_proposal))

	# Track the failures of the proposals
	n_so_far = 0
	failed = False
	responded = 0

	for server_stub in server_stubs:
		# Makes the connection to the server
		try:
			# gRPC call to other Paxos Servers to see if they acceept the proposal
			response = server_stub.prepare(paxos_pb2.proposal(n=n_proposal), _TIMEOUT_SECONDS)

			# Sees a higher n value then it's current value and immediately stops the process
			if response.n >= n_proposal:
				failed = True
				log_info('Proposal ' + str(n_proposal) + ' failed')
				break
			else:
				# If the response is positive, then it notes the positive response
			 	if response.n_v > n_so_far:
					n_so_far = response.n
					value = response.v
				responded += 1
		except Exception as e:
			if ('ExpirationError' in str(e)):
				log_info('Failure to connect to server_stub')
				continue
			else:
				# More severe error, should log and crash
				traceback.print_exc()
				sys.exit(1)

	# No proposals have been sent so far, suggests its own IP 
	if value is None:
		value = self_paxos_server.address

	# If it does not have a majority of responses, Paxos fails
	if responded < len(server_stubs) / 2.0:
		failed = True
		
	return(failed, n_proposal, value)

# Requests that the other Paxos Server accepts the proposal
def request_accept(server_stubs, self_paxos_server, n_proposal, value):
	accepted = 0
	for stub in server_stubs:
		try:
			response = stub.accept(paxos_pb2.request_acceptance(n=n_proposal, v=value), _TIMEOUT_SECONDS)
		except Exception as e:
			traceback.print_exc()
			return False
		if response.accept_bool:
			accepted += 1

	# If the majority accept the proposal, then it passes
	if accepted > len(server_stubs) / 2.0:
		log_info('Proposal accepted')
		return True
	else:
		log_info('Proposal {0} rejected with value {1}'.format(n_proposal, value))
		return False

# Checks to ensure that all the stubs are currently available by pinging them
# If more than half of them are available, it begins Paxos. Otherwise, it waits.
def check_stubs_up(stubs):
	responses = 0
	for stub in stubs:
		try:
			response = stub.ping(paxos_pb2.empty(), _TIMEOUT_SECONDS)
			responses += 1
		except Exception as e:
			if ('ExpirationError' in str(e)):
				log_info('Failure to connect to server_stub during startup')
				continue
			else:
				# More severe error, should log and crash
				traceback.print_exc()
				sys.exit(1)
	if responses < len(stubs) / 2:
		return False
	else:
		return True

# Make sure that all machines are aware that the Paxos algorithm is finishing
# Not all machines are aware that the server has failed at the same time. Could 
# be in the middle of calculating gradients or waiting to be timed out.
def gen_server_stubs(self_paxos_server, local_id):
	TOT_ATTEMPTS = 3
	for i in range(TOT_ATTEMPTS):
		server_addresses = gen_server_addresses(local_id, self_paxos_server.address)
		print(server_addresses)
		server_addresses.remove(self_paxos_server.address)
		stubs = []
		for server_address in server_addresses:
			if not self_paxos_server.consensus_reached:
				if local_id is not None:
					server_port = int(server_address[-5:])
					channel = implementations.insecure_channel('localhost', server_port)
				else:
					channel = implementations.insecure_channel(server_address, PAXOS_PORT_STR)

				stub = paxos_pb2.beta_create_PaxosServer_stub(channel)
				stubs.append(stub)
		all_stubs_responsive = check_stubs_up(stubs)
		if all_stubs_responsive:
			return stubs
		time.sleep(1 * TOT_ATTEMPTS)
	return None

# Sends to all servers that consensus was reached and a server was chosen.
def broadcast_consensus(server_stubs, self_paxos_server, value):
	for stub in server_stubs:
		response = stub.accepted(paxos_pb2.consensus(n=self_paxos_server.n, v=value), 2 * _TIMEOUT_SECONDS)

# Begins the Paxos protocol
def start_paxos(server_stubs, self_paxos_server):
	proposal_failed, n_proposal, value = send_proposals(server_stubs, self_paxos_server)
	if not proposal_failed and not self_paxos_server.consensus_reached:
		# Have everyone accept the proposal
		accepted = request_accept(server_stubs, self_paxos_server, n_proposal, value)
		if accepted and not self_paxos_server.consensus_reached:
			# If accepted, let everyone know that the server has been chosen
			broadcast_consensus(server_stubs, self_paxos_server, value)
			self_paxos_server.new_server = value
			self_paxos_server.consensus_reached = True
			return True

	# If proposal failed, backoff to try again later
	self_paxos_server.backoff = self_paxos_server.backoff * (1 + 10 * random.random())
	return False

# Client loops and runs the paxos algorithm every few seconds
def paxos_loop(self_paxos_server, local_id):
	time_slept = 0
	send_proposal_time = self_paxos_server.backoff

	while not self_paxos_server.consensus_reached:
		time.sleep(0.1)
		time_slept += 0.1

		# Send a proposal at allocated time
		if time_slept > send_proposal_time and not self_paxos_server.consensus_reached:
			time.sleep(random.random())
			server_stubs = gen_server_stubs(self_paxos_server, local_id)
			if server_stubs is None:
				self_paxos_server.new_server = ''
				break
			start_paxos(server_stubs, self_paxos_server)
			send_proposal_time = (random.gauss(1, 0.25) * self_paxos_server.backoff)
			time_slept = 0

		# If proposal fails, revert to checking for a server
		if send_proposal_time > 60:
			self_paxos_server.consensus_reached = True
			self_paxos_server.consensus_value = ''
			break

# This is the final function that exterior functions like client.py will call
def run_paxos(local_id=None):
	# Generates the host name
	hostname = gen_local_address(local_id)
	log_info(hostname + ' called to run Paxos for determining the server')

	# Generates the server
	paxos_server, server = create_server(hostname, local_id)
	try:
		# Launch the server on a separate thread
		Thread(target=run_server, args=(server,paxos_server,)).start()
		start_paxos = time.time()

		# Begin to run Paxos
		paxos_loop(paxos_server, local_id)
		if paxos_server.new_server != '':
			log_info('Done, new server is: {0} finished paxos in {1:2}s'.format(paxos_server.new_server, time.time()-start_paxos))
		else:
			# New server is empty only when a suitable server was not found after a predefined amount of time
			log_info('Failure to connect to other allocated instances. Stopping paxos.')
	except KeyboardInterrupt:
		sys.exit(0)
	finally:
		paxos_server.consensus_reached = True
		server.stop(0)
	return paxos_server.new_server

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--id')
	args = parser.parse_args()
	local_id = args.id
	if local_id is not None:
		local_id = int(local_id)
		assert(local_id > 0)
	log_info(run_paxos(local_id))
