# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dist_sgd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dist_sgd.proto',
  package='dist_sgd',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x64ist_sgd.proto\x12\x08\x64ist_sgd\"`\n\tSubTensor\x12\x12\n\ntensor_len\x18\x01 \x01(\x05\x12\x14\n\x0ctensor_chunk\x18\x02 \x01(\x05\x12\x16\n\x0etensor_content\x18\x03 \x01(\x0c\x12\x11\n\tdata_indx\x18\x04 \x01(\x05\"\x1f\n\nClientInfo\x12\x11\n\tclient_id\x18\x01 \x01(\x05\"\x1c\n\nStatusCode\x12\x0e\n\x06status\x18\x01 \x01(\x05\"6\n\tPrevBatch\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x16\n\x0eprev_data_indx\x18\x02 \x01(\x05\"1\n\tNextBatch\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x11\n\tdata_indx\x18\x02 \x01(\x05\"\x07\n\x05\x65mpty2\xf0\x01\n\x0bParamFeeder\x12;\n\nSendParams\x12\x14.dist_sgd.ClientInfo\x1a\x13.dist_sgd.SubTensor\"\x00\x30\x01\x12;\n\rSendNextBatch\x12\x13.dist_sgd.PrevBatch\x1a\x13.dist_sgd.NextBatch\"\x00\x12;\n\nGetUpdates\x12\x13.dist_sgd.SubTensor\x1a\x14.dist_sgd.StatusCode\"\x00(\x01\x12*\n\x04ping\x12\x0f.dist_sgd.empty\x1a\x0f.dist_sgd.empty\"\x00\x42\x18\n\x0bio.dist_sgdB\x07\x44istSGDP\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SUBTENSOR = _descriptor.Descriptor(
  name='SubTensor',
  full_name='dist_sgd.SubTensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_len', full_name='dist_sgd.SubTensor.tensor_len', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tensor_chunk', full_name='dist_sgd.SubTensor.tensor_chunk', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tensor_content', full_name='dist_sgd.SubTensor.tensor_content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_indx', full_name='dist_sgd.SubTensor.data_indx', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=124,
)


_CLIENTINFO = _descriptor.Descriptor(
  name='ClientInfo',
  full_name='dist_sgd.ClientInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='dist_sgd.ClientInfo.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=157,
)


_STATUSCODE = _descriptor.Descriptor(
  name='StatusCode',
  full_name='dist_sgd.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dist_sgd.StatusCode.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=187,
)


_PREVBATCH = _descriptor.Descriptor(
  name='PrevBatch',
  full_name='dist_sgd.PrevBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='dist_sgd.PrevBatch.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prev_data_indx', full_name='dist_sgd.PrevBatch.prev_data_indx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=243,
)


_NEXTBATCH = _descriptor.Descriptor(
  name='NextBatch',
  full_name='dist_sgd.NextBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='dist_sgd.NextBatch.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_indx', full_name='dist_sgd.NextBatch.data_indx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=294,
)


_EMPTY = _descriptor.Descriptor(
  name='empty',
  full_name='dist_sgd.empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=296,
  serialized_end=303,
)

DESCRIPTOR.message_types_by_name['SubTensor'] = _SUBTENSOR
DESCRIPTOR.message_types_by_name['ClientInfo'] = _CLIENTINFO
DESCRIPTOR.message_types_by_name['StatusCode'] = _STATUSCODE
DESCRIPTOR.message_types_by_name['PrevBatch'] = _PREVBATCH
DESCRIPTOR.message_types_by_name['NextBatch'] = _NEXTBATCH
DESCRIPTOR.message_types_by_name['empty'] = _EMPTY

SubTensor = _reflection.GeneratedProtocolMessageType('SubTensor', (_message.Message,), dict(
  DESCRIPTOR = _SUBTENSOR,
  __module__ = 'dist_sgd_pb2'
  # @@protoc_insertion_point(class_scope:dist_sgd.SubTensor)
  ))
_sym_db.RegisterMessage(SubTensor)

ClientInfo = _reflection.GeneratedProtocolMessageType('ClientInfo', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTINFO,
  __module__ = 'dist_sgd_pb2'
  # @@protoc_insertion_point(class_scope:dist_sgd.ClientInfo)
  ))
_sym_db.RegisterMessage(ClientInfo)

StatusCode = _reflection.GeneratedProtocolMessageType('StatusCode', (_message.Message,), dict(
  DESCRIPTOR = _STATUSCODE,
  __module__ = 'dist_sgd_pb2'
  # @@protoc_insertion_point(class_scope:dist_sgd.StatusCode)
  ))
_sym_db.RegisterMessage(StatusCode)

PrevBatch = _reflection.GeneratedProtocolMessageType('PrevBatch', (_message.Message,), dict(
  DESCRIPTOR = _PREVBATCH,
  __module__ = 'dist_sgd_pb2'
  # @@protoc_insertion_point(class_scope:dist_sgd.PrevBatch)
  ))
_sym_db.RegisterMessage(PrevBatch)

NextBatch = _reflection.GeneratedProtocolMessageType('NextBatch', (_message.Message,), dict(
  DESCRIPTOR = _NEXTBATCH,
  __module__ = 'dist_sgd_pb2'
  # @@protoc_insertion_point(class_scope:dist_sgd.NextBatch)
  ))
_sym_db.RegisterMessage(NextBatch)

empty = _reflection.GeneratedProtocolMessageType('empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'dist_sgd_pb2'
  # @@protoc_insertion_point(class_scope:dist_sgd.empty)
  ))
_sym_db.RegisterMessage(empty)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\013io.dist_sgdB\007DistSGDP\001'))
import abc
import six
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

class BetaParamFeederServicer(six.with_metaclass(abc.ABCMeta, object)):
  """<fill me in later!>"""
  @abc.abstractmethod
  def SendParams(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SendNextBatch(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetUpdates(self, request_iterator, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ping(self, request, context):
    raise NotImplementedError()

class BetaParamFeederStub(six.with_metaclass(abc.ABCMeta, object)):
  """The interface to which stubs will conform."""
  @abc.abstractmethod
  def SendParams(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def SendNextBatch(self, request, timeout):
    raise NotImplementedError()
  SendNextBatch.future = None
  @abc.abstractmethod
  def GetUpdates(self, request_iterator, timeout):
    raise NotImplementedError()
  GetUpdates.future = None
  @abc.abstractmethod
  def ping(self, request, timeout):
    raise NotImplementedError()
  ping.future = None

def beta_create_ParamFeeder_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  request_deserializers = {
    ('dist_sgd.ParamFeeder', 'GetUpdates'): dist_sgd_pb2.SubTensor.FromString,
    ('dist_sgd.ParamFeeder', 'SendNextBatch'): dist_sgd_pb2.PrevBatch.FromString,
    ('dist_sgd.ParamFeeder', 'SendParams'): dist_sgd_pb2.ClientInfo.FromString,
    ('dist_sgd.ParamFeeder', 'ping'): dist_sgd_pb2.empty.FromString,
  }
  response_serializers = {
    ('dist_sgd.ParamFeeder', 'GetUpdates'): dist_sgd_pb2.StatusCode.SerializeToString,
    ('dist_sgd.ParamFeeder', 'SendNextBatch'): dist_sgd_pb2.NextBatch.SerializeToString,
    ('dist_sgd.ParamFeeder', 'SendParams'): dist_sgd_pb2.SubTensor.SerializeToString,
    ('dist_sgd.ParamFeeder', 'ping'): dist_sgd_pb2.empty.SerializeToString,
  }
  method_implementations = {
    ('dist_sgd.ParamFeeder', 'GetUpdates'): face_utilities.stream_unary_inline(servicer.GetUpdates),
    ('dist_sgd.ParamFeeder', 'SendNextBatch'): face_utilities.unary_unary_inline(servicer.SendNextBatch),
    ('dist_sgd.ParamFeeder', 'SendParams'): face_utilities.unary_stream_inline(servicer.SendParams),
    ('dist_sgd.ParamFeeder', 'ping'): face_utilities.unary_unary_inline(servicer.ping),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_ParamFeeder_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  import dist_sgd_pb2
  request_serializers = {
    ('dist_sgd.ParamFeeder', 'GetUpdates'): dist_sgd_pb2.SubTensor.SerializeToString,
    ('dist_sgd.ParamFeeder', 'SendNextBatch'): dist_sgd_pb2.PrevBatch.SerializeToString,
    ('dist_sgd.ParamFeeder', 'SendParams'): dist_sgd_pb2.ClientInfo.SerializeToString,
    ('dist_sgd.ParamFeeder', 'ping'): dist_sgd_pb2.empty.SerializeToString,
  }
  response_deserializers = {
    ('dist_sgd.ParamFeeder', 'GetUpdates'): dist_sgd_pb2.StatusCode.FromString,
    ('dist_sgd.ParamFeeder', 'SendNextBatch'): dist_sgd_pb2.NextBatch.FromString,
    ('dist_sgd.ParamFeeder', 'SendParams'): dist_sgd_pb2.SubTensor.FromString,
    ('dist_sgd.ParamFeeder', 'ping'): dist_sgd_pb2.empty.FromString,
  }
  cardinalities = {
    'GetUpdates': cardinality.Cardinality.STREAM_UNARY,
    'SendNextBatch': cardinality.Cardinality.UNARY_UNARY,
    'SendParams': cardinality.Cardinality.UNARY_STREAM,
    'ping': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'dist_sgd.ParamFeeder', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
