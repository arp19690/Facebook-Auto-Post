#!/bin/bash

if [ $1 = "fbautopost" ];then
    echo "Activating VirtualENV"
    . /Applications/XAMPP/htdocs/work/svn/Facebook-Auto-Post/venv/bin/activate

    echo "Running the script now"
    python /Applications/XAMPP/htdocs/work/svn/Facebook-Auto-Post/run.py

    echo "Deactivating VirtualENV"
    deactivate
elif [ $1 = "amazonaffiliates" ];then
    echo "Activating VirtualENV"
    . /Applications/XAMPP/htdocs/work/svn/Facebook-Auto-Post/venv/bin/activate

    echo "Running the script now"
    python /Applications/XAMPP/htdocs/work/svn/Facebook-Auto-Post/AmazonAffiliateFunctions.py

    echo "Deactivating VirtualENV"
    deactivate
fi
