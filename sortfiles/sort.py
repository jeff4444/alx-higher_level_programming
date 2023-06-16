#!/usr/bin/python3
import os
import shutil
import sys

if (len(sys.argv) < 2):
    maindir = '.'
else:
    if os.path.isdir(sys.argv[1]):
        maindir = sys.argv[1]
    else:
        print("Your entered a non-valid path")
        sys.exit(1)
print(len(sys.argv))
files = os.listdir(maindir)

extensions = set()
for some_file in files:
    if os.path.isfile(maindir + '/' + some_file):
        _, ext = os.path.splitext(some_file)
        extensions.add(ext)

for ext in extensions:
    if ext == '':
        dirname = 'none'
    else:
        dirname = ext[1:]
    if os.path.isdir(maindir + "/" + dirname) is False:
        os.mkdir(maindir + '/' + dirname)
    for some_file in files:
        if os.path.isdir(maindir + '/' + some_file):
            continue
        _, file_ext = os.path.splitext(some_file)
        if file_ext == ext:
            shutil.move((maindir + '/' + some_file), (maindir + '/' + dirname))
