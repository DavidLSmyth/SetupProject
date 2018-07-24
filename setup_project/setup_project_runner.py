#A program that will set up a project directory in the specified directory that contains
#a layout recommended by Kenneth Reitz https://github.com/DavidLSmyth/samplemod
#Typically may not want to include everything by default, so allow user to decide.

#stdlib imports
import sys
import os
#for recursively manipulating directories over kenneth's directory structure
import shutil
sys.path.append('..')
#keep run_setup_with_args in utils file so that program may be extended
from setup_project.utils import run_setup_with_args, parse_args

#usage: python SetupProject.py directory_to_initialise project_name -docs -tests -LICENCE -Makefile -setup.py




	
if __name__ == '__main__':
	#iterate over all args in the arg_parser and set up directory structure accordingly
	args = parse_args(sys.argv[1:])
	print("provided args: ")
	try:
		run_setup_with_args(args)
	except PermissionError as e:
		print('Could not create directory as specified due to PermissionError: \n{}'.format(e))
	