#!/bin/bash

echo "Getting into Facebook Auto Post Directory"
cd /Applications/XAMPP/htdocs/work/svn/Facebook-Auto-Post

echo "Activating VirtualENV"
. venv/bin/activate

echo "Running the script now"
python run.py

echo "Deactivating VirtualENV"
deactivate
