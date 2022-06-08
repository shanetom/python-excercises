#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import zipfile

"""Copy Special exercise
"""


def get_special_paths(dr):
    abs_path_files = []
    filenames = os.listdir(dr)

    for filename in filenames:
        path = os.path.join(dr, filename)
        abs_path = os.path.abspath(path)
        if re.search('_', abs_path):
            abs_path_files.append(abs_path)

    return abs_path_files


def copy_to(paths, dr):
    for path in paths:
        if os.path.exists(dr):
            shutil.copy(path, dr)
        else:
            os.mkdir(dr)
            shutil.copy(path, dr)


def zip_to(paths, zippath):
    zf = zipfile.ZipFile(zippath, "w")
    for path in paths:
        zf.write(path, compress_type=zipfile.ZIP_DEFLATED)
    zf.close()

# +++your code here+++
# Write functions and modify main() to call them


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    # +++your code here+++
    # Call your functions

    if todir == '' and tozip == '':
        for arg in args:
            abs_path_files = get_special_paths(arg)
            print(*abs_path_files, sep='\n')

    if todir != '':
        for arg in args:
            abs_path_files = get_special_paths(arg)
            copy_to(abs_path_files, todir)

    if tozip != '':
        for arg in args:
            abs_path_files = get_special_paths(arg)
            zip_to(abs_path_files, tozip)


if __name__ == "__main__":
    main()
