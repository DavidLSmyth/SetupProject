import os
import shutil
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
	os.chdir('./' + args.project_name + '_module')
	#first copy over Kenneth's directory structure and then remove files/directories
	#specified by the user
	cloned_repo = Repo.clone_from('https://github.com/DavidLSmyth/samplemod.git', '.')
	print('working directory of cloned repo: ',cloned_repo.working_dir)

	#rename sample to user specified name
	os.rename('./sample',args.project_name)

	#then setup sub files/directories
	for optional_arg in filter(lambda x: x, vars(args)):
		arg_path = './' + optional_arg
		#if directory, remove tree
		if os.path.isdir(arg_path):
			shutil.rmtree(arg_path)
		#if file, remove
		elif os.path.isfile(arg_path):
			os.remove(arg_path)