#!/usr/bin/python3
import os
import shutil

files = os.listdir()

extensions = set()
for some_file in files:
    if os.path.isfile(some_file):
        _, ext = os.path.splitext(some_file)
        extensions.add(ext)
print(extensions)

for ext in extensions:
    if ext == '':
        dirname = 'none'
    else:
        dirname = ext[1:]
    if os.path.isdir("./" + dirname) is False:
        os.mkdir(dirname)
    for some_file in files:
        _, file_ext = os.path.splitext(some_file)
        if file_ext == ext:
            shutil.move(some_file, dirname)
