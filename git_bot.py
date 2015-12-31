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

    print count_files

    for iter in range(count):

        src_file_path = onlyfiles[random.randint(1,count_files)]
        dest_file_path = src_file_path.replace(SOURCE,DEST)

        print "Processing File "
        print "%s" %(dest_file_path)
        if not (src_file_path or dest_file_path):
            continue

        relative_dest_path = dest_file_path.split(DEST)[1]
        file_items = relative_dest_path.split(os.path.sep)
        repo_name = file_items[0]
        file_name = file_items[-1]
        repo_path = DEST + repo_name + os.path.sep

        message = "Pushing new files"
        if file_name.endswith("js"):
            message = "Adding '%s' javascript file to %s repository" %(file_name.replace(".js",""), repo_name)
        elif file_name.endswith("css"):
            message = "UI Changes to repo:%s" %(repo_name)
        elif file_name.endswith("py"):
            message = "Python module '%s' added to repo %s" %(file_name.replace(".py",""), repo_name)
        elif file_name.endswith("pyc"):
            message = "Python Compiled Object : %s" %(file_name.replace(".pyc",""))
        elif file_name.endswith("html"):
            message = "Template for %s in %s" %(file_name.replace(".html","s"), repo_name)
        elif file_name.endswith("png") or file_name.endswith("jpg") or file_name.endswith("jpeg") :
            message = "Pushing New Assests"

        if not os.path.exists(os.path.dirname(dest_file_path)):
            os.makedirs(os.path.dirname(dest_file_path))

        if not os.path.isfile(dest_file_path):
            if os.path.isfile(src_file_path):
                shutil.copy(src_file_path, dest_file_path)

        if os.path.isfile(dest_file_path):
            subprocess.call(["touch", dest_file_path])
            if os.path.isfile(src_file_path):
                os.remove(src_file_path)

        subprocess.call(["sh", GITCMD, repo_path, dest_file_path, message])

        print "Done \n"

def automate():
    copy_random_files()
    return

if __name__ == "__main__":

    automate()