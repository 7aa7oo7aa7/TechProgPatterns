#!/bin/bash
pip3 freeze > requirements.txt
python3 ./code/interface.py
