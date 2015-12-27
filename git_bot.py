import os
import random
import shutil
import subprocess
from git import Repo
from os import listdir
from os.path import isfile, join


GITCMD = '/Users/pawan/src/self-maker/git-cmd.sh'
SOURCE = '/Users/pawan/src1/'
DEST = '/Users/pawan/src/'

def init_repos():

    repo_list = []

    repo_names = []

    for name in repo_names:
        repo1 = Repo('/Users/pawan/src/self-maker')
        if not repo1.bare:
            repo_list.append(repo1)

def copy_random_files():

    onlyfiles = []

    for root, directories, filenames in os.walk(SOURCE):
        for filename in filenames:
            onlyfiles.append(os.path.join(root,filename))

    count_files = len(onlyfiles) - 10
    count = random.randint(3,10)

    for iter in range(count):

        src_files_path = onlyfiles[random.randint(1,count_files)]
        dest_file_path = src_files_path.replace(SOURCE,DEST)

        relative_dest_path = dest_file_path.split(DEST)[1]
        repo_name = relative_dest_path.split(os.path.sep)[0]

        repo_path = SOURCE + repo_name
        print repo_path

        if os.path.isfile (src_files_path): print "Success"
        # shutil.copy (filename1, filename2)

    subprocess.call(["sh", GITCMD, ".", "Adding random generator"])

def automate():
    copy_random_files()
    pass


if __name__ == "__main__":

    #init_repos()
    automate()