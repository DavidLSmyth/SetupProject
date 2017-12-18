#test SetupProject.py
import unittest
import os
import shutil
import sys
sys.path.append('..')

from SetupProject.setup_project import parse_args
from SetupProject.utils import run_setup_with_args

class TestSetupProject(unittest.TestCase):
	def setUp(self):
		self.test_args = ['C:\\Users\\13383861\\Dropbox\\SoftwareDevelopment\\miscProjects\\SetupProject_module\\test_repo', 'test_project', '-docs', '-LICENCE']
		self.test_args1 = ['.', 'test_project', '-docs', '-licence']
		self.test_args2 = ['.', 'test_project', '-docs', '-licence']
		os.chdir('./')
		
	def test_parse_args(self):
		args = parse_args(self.test_args)
		self.assertEqual(args.project_name, 'test_project')
		self.assertFalse(args.docs)
		self.assertFalse(args.LICENCE)
		self.assertTrue(args.tests)
		
	def run_setup_with_args_helper(self):
		run_setup_with_args(parse_args(self.test_args))
		
	def test_run_setup(self):
		#run the setup and then verify the directory structure is as intended
		#t1 = threading.Thread(target = run_setup_with_args, args = (parse_args(self.test_args),))
		#t1.start()
		#t1.join()
		#run_setup_with_args(parse_args(self.test_args))
		self.run_setup_with_args_helper()
		self.assertTrue(os.path.exists('./test_project'))
		self.assertFalse(os.path.exists('./test_project/docs'))
		self.assertFalse(os.path.isfile('./test_project/LICENCE'))
		pass
		
	def tearDown(self):
		'''Removes all intermediate directories'''
		try:
			#print("removing all files and subdirectories from  {}".format(os.path.dirname('../test_project_module')))
			os.chdir('..')
			shutil.rmtree('C:\\Users\\13383861\\Dropbox\\SoftwareDevelopment\\miscProjects\\SetupProject_module\\test_repo')
		except Exception as e:
			print('Could not clean up temp test directories successfully, please check manually')
			print(e)
			
if __name__ == '__main__':
	unittest.main()
	
	