#given args, creates file system for project

import sys
import os

import shutil

from git import Repo


def run_setup_with_args(args):
	#navigate to correct directory
	print('Initliasing new project in directory {} with args {}'.format(args.directory, vars(args)))
	os.chdir(args.directory)
		
	#clone git repo
	Repo.clone('https://github.com/DavidLSmyth/samplemod.git','.')
	
	os.rename('./sample_mod', args.project_name + '_mod')
	os.rename('./sample_mod/sample', args.project_name)
	os.chdir('./args.project_name' + '_mod')
	#remove unnecessary files
	for removeable in filter(lambda x: x, args):
		removeable_path = os.curdir + removeable
		if os.path.isfile(removeable_path):
			os.remove(removeable_path)
		elif os.path.is_dir(removeable_path):
			shutil.rmtree(removeable_path)
	