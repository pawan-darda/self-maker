#!/usr/bin/env bash

cd $1

if [ $# -eq 3 ]
then
    git add $2
    sleep 0.5
    git commit -a -m "$3"
    sleep 0.5
else
    git commit -a -m "$2"
    sleep 0.5
fi

git pull origin master
sleep 0.5
git push origin master

