import os
from git import Repo

SOURCE = '/Users/pawan/src1/'
DEST = '/Users/pawan/src/'

def init_repos():

    repo_list = []

    repo_names = []

    for name in repo_names:
        repo1 = Repo('/Users/pawan/src/')
        if not repo1.bare:
            repo_list.append(repo1)

def get_list_files():
    pass

def automate():
    pass


if __name__ == "__main__":

    init_repos()
    automate()