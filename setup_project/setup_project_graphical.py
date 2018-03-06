#A graphical interface to setup project
from tkinter import (Label, IntVar, StringVar, Button, Entry,
Checkbutton, W, E, Tk, filedialog, mainloop)
from utils import parse_args, run_setup_with_args

class PythonProjGUI:
	def __init__(self, master):
		self.master = master
		master.title("Python Project initialiser")
		
		self.directory_selector_label = Label(master, text="Root directory to create project: ")
		self.directory_selector_label.grid(row=0, column=0, sticky=W)
		self.chosen_directory = StringVar()
		self.directory_selector = Button(master, text="Browse", command=self.load_file, width=12)
		self.directory_selector.grid(row=0, column = 1,sticky = E)
		
		self.project_name_label = Label(self.master, text="Choose a project name: ")
		self.project_name_label.grid(row=2, column=0, sticky=W)
		
		self.project_name = StringVar()
		self.project_name_text = Entry(self.master, textvariable=self.project_name)
		self.project_name_text.grid(row = 2, column = 1, sticky=E)
		
		self.folders = ['tests', 'docs']
		self.folders_vars = [IntVar() for _ in self.folders]
		self.files = ['.travis.yml', 'requirements.txt', 'LICENCE', 'makefile', 'setup.py']
		self.files_vars = [IntVar() for _ in self.files]
	
	
		self.folder_checkbuttons = []
		self.file_checkbuttons = []
		for folder, folder_var in zip(self.folders, self.folders_vars):
			self.folder_checkbuttons.append(Checkbutton(master, text="{} folder".format(folder), variable=folder_var))
			#.grid(row=row_counter, sticky=W)
			
		for file_var, file in zip(self.files_vars, self.files):
			self.file_checkbuttons.append(Checkbutton(master, text=file, variable=file_var))
			
			#.grid(row=row_counter, sticky=W)
		self.OptionsLabel = Label(self.master, text="\nCheck to exclude from project:\n")
		self.OptionsLabel.grid(row = 3, column = 0, sticky = W)
		row_counter = 5
		for checkbutton in self.folder_checkbuttons+self.file_checkbuttons:
			checkbutton.grid(row=row_counter, column=0, sticky=W)
			row_counter += 1
				
		self.quit_button = Button(master, text='Quit', command=master.quit)
		self.quit_button.grid(row=row_counter, sticky=W, pady=4)
		self.create_proj_button = Button(master, text='Create Project', command=self.create_proj)
		self.create_proj_button.grid(row=row_counter, sticky=E, pady=4)
	
	def load_file(self):
		self.directory = filedialog.askdirectory()
		self.directory_label = Label(self.master, text='Folder: {}'.format(self.directory))
		self.directory_label.grid(row = 1, sticky=W)
		
	def create_proj(self):
		args = []
		for arg, value in zip(self.folders+self.files, self.folders_vars + self.files_vars):
			if value.get():
				args.append('-'+arg)
		args.insert(0, self.project_name.get())
		args.insert(0, self.directory)
		print('creating project with args: {}'.format(args))
		run_setup_with_args(parse_args(args))
		root.destroy()
		
root = Tk()
root.geometry('350x350')
root.resizable(True, False)
my_gui = PythonProjGUI(root)
root.mainloop()





