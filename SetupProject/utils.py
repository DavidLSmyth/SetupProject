#given args, creates file system for project

import sys
import os

import shutil

from git import Repo


def run_setup_with_args(args):
	#navigate to correct directory
	print('Initliasing new project in directory {} with args {}'.format(args.directory, vars(args)))
	os.makedirs(args.directory +'/' + args.project_name + '_module')
	os.chdir(args.directory + '/' + args.project_name + '_module')	
	
	#clone git repo
	try:
		Repo.clone_from('https://github.com/DavidLSmyth/samplemod.git','.')
	except exception as e:
		print('''Could not clone git repository, please check that you have permissions to 
		write to the specified folder''')
	#rename the main code directory
	os.rename('./sample', args.project_name)
	#remove unnecessary files
	for removeable in filter(lambda x: x, vars(args)):
		removeable_path = os.curdir + removeable
		if os.path.isfile(removeable_path):
			os.remove(removeable_path)
		elif os.path.isdir(removeable_path):
			shutil.rmtree(removeable_path)
	