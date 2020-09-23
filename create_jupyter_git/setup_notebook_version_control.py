#!/usr/bin/env python

import os
import stat
import click
import pathlib
import pyfiglet
import shutil
from colr import Colr as color

from .is_cwd_git_repo import is_cwd_git_repo

@click.command()
@click.argument('directoryname')
def generate_repo(directoryname):

    print(color().bright().blue(pyfiglet.figlet_format("Create Jupyter Git")))

    # determine all the important paths needed
    current_working_directory = pathlib.Path(os.getcwd()).absolute()
    current_directory_path = pathlib.Path(__file__).parent.absolute()
    repo_template_path = os.path.join(current_directory_path, 'repo_template')

    target_directory_path = os.path.join(current_working_directory, directoryname)
    target_script_path = os.path.join(target_directory_path, 'scripts/ipynb_output_filter.py')

    script_absolute_path = os.path.join(target_directory_path, "scripts/ipynb_output_filter.py")
    git_attributes_path = os.path.join(target_directory_path, ".gitattributes")

    # ensure the taret directory exists first
    if not os.path.exists(target_directory_path):
        pathlib.Path(target_directory_path).mkdir(parents=True, exist_ok=True)

    # move into that target directory to perform some system commands
    os.chdir(target_directory_path)

    # don't attempt to do anything if we are already inside a repo
    if (is_cwd_git_repo()):
        print(color().bright().red('already within a repository, exiting with no changes'))
        return

    # copy the repo template over
    print(repo_template_path)
    print(target_directory_path)
    shutil.copytree(repo_template_path, target_directory_path, dirs_exist_ok=True)
    
    # make our magic script executable
    st = os.stat(target_script_path)
    os.chmod(target_script_path, st.st_mode | stat.S_IEXEC)

    # initialize the git repo
    os.system("git init")
    print(color().bright().green('git repository initialized'))

    # setup .gitattributes
    with open(git_attributes_path, "w") as git_attributes_file:
        print("*.ipynb    filter=dropoutput_ipynb", file=git_attributes_file)
        git_attributes_file.flush()

    # update git configs to utilize the filter script
    os.system("git config core.attributesfile {}".format(git_attributes_path))
    os.system("git config filter.dropoutput_ipynb.clean {}".format(script_absolute_path))
    os.system("git config filter.dropoutput_ipynb.smudge cat")
    
    # switch back to the original current working directory to be a good steward
    os.chdir(current_working_directory)