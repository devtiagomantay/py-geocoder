#!/usr/bin/env bash

sudo apt install python3-venv
echo "python3-venv installed"
python3 -m venv .venv
echo "Python3 virtual env created"
. .venv/bin/activate
echo "env created"
echo "Python3 virtual env activated"
pip install -r requirements.txt
echo "Requirements installed!"