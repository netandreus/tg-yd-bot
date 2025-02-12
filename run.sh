#!/bin/bash
#################
#  Run locally  #
#################

echo "Switching to virtualenv 'venv'..."
source venv/bin/activate

echo "Running server...."
poetry run server