#!/bin/bash

echo "Activating VirtualENV"
. /Applications/XAMPP/htdocs/work/svn/Facebook-Auto-Post/venv/bin/activate

echo "Running the script now"
python /Applications/XAMPP/htdocs/work/svn/Facebook-Auto-Post/run.py

echo "Deactivating VirtualENV"
deactivate
