from subprocess import call, STDOUT
import os

def is_cwd_git_repo ():
    if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
        return False
    else:
        return True