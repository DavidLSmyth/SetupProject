# SetupProject
A utility to automatically set up a project with desired specifications

You can use SetupProject via the command line or through the GUI to create python project in a consistent and logical manner as recommended by Kenneth Reitz: https://github.com/kennethreitz/samplemod
The SetupProject tool allows you to choose whether you want to include directories such as test and will create a file structure that will allow you to skip tiresome setup steps such as adding a .gitignore.

# Usage
usage:
python SetupProject.py directory_to_initialise project_name -docs -tests -LICENCE -Makefile -setup.py -repo REPO

optional arguments remove the specified folder/file name from setup, repo specifies a github repo to copy from. The default is that recommended by Kenneth Reitz: https://github.com/DavidLSmyth/samplemod. Github repo must be called sample (working on changing this).

OR

python setup_project_graphical.py to use the GUI (only tested on Windows)

# Customization
Edit the code to point at a gitHub repo that you have setup in order to modify the options available in setup.


