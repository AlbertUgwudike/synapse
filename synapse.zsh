#!/bin/zsh

echo "\n### SYNAPSE: Installing Dependencies ....\n"
python3 -m venv venv
source venv/bin/activate
venv/bin/pip install pandas
echo "\n### SYNAPSE: Finished installing dependencies!\n"
venv/bin/python3 main.py
deactivate