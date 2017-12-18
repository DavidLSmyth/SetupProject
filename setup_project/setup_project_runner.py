#A program that will set up a project directory in the specified directory that contains
#a layout recommended by Kenneth Reitz https://github.com/DavidLSmyth/samplemod
#Typically may not want to include everything by default, so allow user to decide.

#stdlib imports
import sys
import argparse
import os
#for recursively manipulating directories over kenneth's directory structure
import shutil
sys.path.append('..')
#keep run_setup_with_args in utils file so that program may be extended
from setup_project.utils import run_setup_with_args

#usage: python SetupProject.py directory_to_initialise project_name -docs -tests -LICENCE -Makefile -setup.py

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
	'-setup':['Whether to include setup.py or not'],
	'-requirements.txt':['Whether to include a requirements file or not'],
	'-travis.yml':['Whether to include a requirements file or not']
	}

	#'store_true' and 'store_false' - These are special cases of 'store_const' used for storing the values 
	#True and False respectively. In addition, they create default values of False and True respectively

	for optional_arg in optional_args.keys():
		parser.add_argument(optional_arg, help=optional_args[optional_arg], action='store_false')
		
	return parser.parse_args(args)
	


	
if __name__ == '__main__':
	#iterate over all args in the arg_parser and set up directory structure accordingly
	args = parse_args(sys.argv[1:])
	try:
		run_setup_with_args(args)
	except PermissionError as e:
		print('Could not create directory as specified due to PermissionError: \n{}'.format(e))
	
	
		














