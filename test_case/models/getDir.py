# !/usr/bin/python3

"""
FileName    : getDir.py
Author      : kun
Date        : 2018-07-26
Describe    : get path
"""
import os

currentDir = os.path.abspath(os.path.dirname(__file__))
proDir = os.path.split(currentDir)[0]