#!/usr/bin/python3
'''Module to compress folder into tgz'''
from os import path, listdir

files = listdir("versions/")
files.sort()
print(files)