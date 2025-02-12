#!/bin/bash
#####################
#  Locally install  #
#####################

echo "Setting up virtualenv..."
virtualenv venv
virtualenv -p python3.13 venv

echo "ACtivating virtualenv..."
source venv/bin/activate

echo "Install packages..."
[ -f "poetry.lock" ] && rm "poetry.lock"
poetry install
echo "[OK] Completed. Now you can run 'run.sh' for starting server."