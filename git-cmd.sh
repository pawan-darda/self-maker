#!/usr/bin/env bash

cd $1

if [ $# -eq 3 ]
then
    echo "GIT Add File"
    echo $2
    git add $2
    sleep 0.5
    echo "GIT Commit"
    git commit -a -m "$3"
    sleep 0.5
else
    git commit -a -m "$2"
    sleep 0.5
fi

echo "GIT Pull"
git pull origin master
sleep 0.5
echo "GIT Push"
git push origin master

