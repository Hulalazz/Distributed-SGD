------------------------------------------------------------------------
-- server.lua
--
-- A general Distributed SGD Parameter server written in lua/torch
--
-- The is a general parameter server file. It takes in the command line 
-- 		options that are necessary to launch the server. The server 
--		will be of the class: 'server_class'. The 'server_class' must 
--		be a class definied with two required functions: :init() and :run()
--		This file will load in the class, call the init() function
-- 		and then call the run() function in a protected loop
--
-- The 'add_to_path' option is a string that will be appended onto the 
--		path before requiring the new 'server_class'
--     
-- Run 
--		th server.lua --help
-- to see a full list of options for the parameter server
------------------------------------------------------------------------

-- Library used to handle data types
require 'data'

-- Library used to run clients in parallel
require 'parallel'

-- Used to update the path variable
require 'package'

------------
-- Options
------------

cmd = torch.CmdLine()

cmd:text("")
cmd:text("**General options**")
cmd:text("")

cmd:option('-server_class',    'demo_server',     	'Class name to use')
cmd:option('-add_to_path' , 	'', 				'A string that will be appended on to the front of the path')

cmd:text("")
cmd:text("**_____________________________**")
cmd:text("Below are all options specific to models")
cmd:text("**_____________________________**")
cmd:text("")

cmd:text("")
cmd:text("**Data options**")
cmd:text("")
cmd:option('-data_file',    'data/demo-train.hdf5',     'Path to the training *.hdf5 file from preprocess.py')
cmd:option('-val_data_file','data/demo-val.hdf5',       'Path to validation *.hdf5 file from preprocess.py')
cmd:option('-save_file',    'demo-seq2seq_lstm',         'Save file name (model will be saved as savefile_epochX_PPL.t7  where X is the X-th epoch and PPL is the validation perplexity')
cmd:option('-train_from',   '',                         'If training from a checkpoint then this is the path to the pretrained model.')

cmd:text("")
cmd:text("**Model options**")
cmd:text("")

cmd:option('-num_layers',       2,      'Number of layers in the LSTM encoder/decoder')
cmd:option('-hidden_size',      300,    'Size of LSTM hidden states')
cmd:option('-word_vec_size',    300,    'Word embedding sizes')
cmd:option('-layer_type',       'lstm', 'Recurrent layer type (rnn, gru, lstm, fast)')

cmd:text("")
cmd:text("**Optimization options**")
cmd:text("")

cmd:option('-num_epochs',       10,     'Number of training epochs')
cmd:option('-start_epoch',      1,      'If loading from a checkpoint, the epoch from which to start')
cmd:option('-param_init',       0.1,    'Parameters are initialized over uniform distribution with support (-param_init, param_init)')
cmd:option('-learning_rate',    1,      'Starting learning rate')
cmd:option('-max_grad_norm',    5,      'If the norm of the gradient vector exceeds this, renormalize it to have the norm equal to max_grad_norm')
cmd:option('-dropout',          0.3,    'Dropout probability. Dropout is applied between vertical LSTM stacks.')
cmd:option('-lr_decay',         0.5,    'Decay learning rate by this much if (i) perplexity does not decrease on the validation set or (ii) epoch has gone past the start_decay_at_limit')
cmd:option('-start_decay_at',   9,      'Start decay after this epoch')
cmd:option('-fix_word_vecs',    0,      'If = 1, fix lookup table word embeddings')
cmd:option('-beam_k',           5,      'K value to use with beam search')
cmd:option('-max_bleu',         4,      'The number of n-grams used in calculating the bleu score')

cmd:option('-pre_word_vecs',    '', 'If a valid path is specified, then this will load pretrained word embeddings (hdf5 file) on the encoder side. See README for specific formatting instructions.')

cmd:text("")
cmd:text("**Other options**")
cmd:text("")

-- GPU
cmd:option('-gpuid',    -1, 'Which gpu to use. -1 = use CPU')
cmd:option('-gpuid2',   -1, 'If this is >= 0, then the model will use two GPUs whereby the encoder is on the first GPU and the decoder is on the second GPU. This will allow you to train with bigger batches/models.')

-- Bookkeeping
cmd:option('-save_every',   1,      'Save every this many epochs')
cmd:option('-print_every',  5,      'Print stats after this many batches')
cmd:option('-seed',         3435,   'Seed for random initialization')

-- Parallel options
cmd:option('-n_proc',           2,      			'The number of processes to farm out')

cmd:option('-setup',    false,   'When true, executes code to setup external servers ')
cmd:option('-remote',           false,   'When true, the farmed out processes are run on remote servers. overrides localhost')
cmd:option('-torch_path',       '/home/michaelfarrell/torch/install/bin/th',   'The path to the torch directory')
cmd:option('-extension',       'Distributed-SGD/lua-lua/',   'The location from the home directory to the helper functions')
cmd:option('-username',       'michaelfarrell',   'The username for connecting to remote clients')

-- Parse arguments
opt = cmd:parse(arg)
opt.print = parallel.print

-- Add on location to path of new class if not already in path
package.path = opt.add_to_path .. package.path

-- Load in the class type
server = require(opt.server_class)

-- Main server function, initializes and runs
function server_main()
	-- Print from parent process
	parallel.print('Im the parent, my ID is: ',  parallel.id, ' and my IP: ', parallel.ip)

	-- Create a new server
	param_server = server.new(opt)

     -- Run the server
    param_server:run()   

end

-- Protected execution of parllalel script:
ok, err = pcall(server_main)
if not ok then print(err) parallel.close() end
