import os
import shutil
import argparse
import sys
#to copy the github files from kenneth's directory
from git import Repo

def run_setup_with_args(args):
	'''Sets up folder directory with given args'''
	print('Setting up your project ({}) \nwith specified arguments: {}\n'.format(args.project_name, vars(args)))
	#first set up a new folder to contain the new python project. Work from the directory specified by the user
	os.chdir(args.directory)
	#need to create an empty directory for git to clone to
	try:
		print('Creating a new directory for project...')
		os.makedirs(args.project_name + '_module')
		print('Successfully created new project directory: {}'.format(os.curdir+args.project_name + '_module'))
	except FileExistsError as e:
		print('The directory already exists, please try again with a different name')
		sys.exit(0)
	os.chdir('./' + args.project_name + '_module')
	#first copy over Kenneth's directory structure and then remove files/directories
	#specified by the user
	cloned_repo = Repo.clone_from('https://github.com/DavidLSmyth/samplemod.git', '.')
	print('working directory of cloned repo: ',cloned_repo.working_dir)

	#rename sample to user specified name
	os.rename('./sample',args.project_name)

	#then setup sub files/directories
	for optional_arg in filter(lambda x: not vars(args)[x], vars(args)):
		arg_path = './' + optional_arg
		#if directory, remove tree
		if os.path.isdir(arg_path):
			print('Removing: {}'.format(arg_path))
			shutil.rmtree(arg_path)
		#if file, remove
		elif os.path.isfile(arg_path):
			print('Removing: {}'.format(arg_path))
			os.remove(arg_path)
			
			
			
			

			#add positional and optional arguments.
#first define directory validation function
def validate_directory_exists(dir_path: str)->str:
	'''returns the path if the directory exists and can be written to, otherwise raises ValueError'''
	if os.path.exists(dir_path) and os.access(dir_path, os.W_OK):
		return dir_path
	else:
		raise ValueError


#also define a parser function that can be unit tested
def parse_args(args):
	#create a parser, provide help message
	parser = argparse.ArgumentParser(description='''Set up a python project as recommended by 
	Kenneth Reitz in specified directory''')
	parser.add_argument('directory', type=validate_directory_exists, help='The directory location for the new project', action='store')
	parser.add_argument('project_name', type=str, help='The name of the new project', action='store')
	#parser.add_argument('--not_included', type=str, help='Flag to not include the listed files/subdirecotories')

	
	#define optional args
	optional_args = {'-docs':['Whether to include docs subdirectory or not'], 
	'-tests':['Whether to include tests subdirectory or not'], 
	'-LICENCE':['Whether to include licence or not'],
	'-makefile':['Whether to include makefile or not'],
	'-setup.py':['Whether to include setup.py or not'],
	'-requirements.txt':['Whether to include a requirements file or not'],
	'-.travis.yml':['Whether to include a requirements file or not']
	}

	#'store_true' and 'store_false' - These are special cases of 'store_const' used for storing the values 
	#True and False respectively. In addition, they create default values of False and True respectively

	for optional_arg in optional_args.keys():
		parser.add_argument(optional_arg, help=optional_args[optional_arg], action='store_false')
		
	return parser.parse_args(args)
	