
import sys
import os

def lowercase(path):
    dir, name = os.path.split(path)
    newname = name.lower()
    if newname == name:
        return path
    newpath = os.path.join(dir, newname)
    os.rename(path, newpath)
    return newpath

def rename(patch):
    patch = os.path.normpath(patch)
    if os.path.isdir(patch):
        newpath = lowercase(patch)
        for entry in os.listdir(newpath):
            nextpath = os.path.join(newpath, entry)
            rename(nextpath)
    elif os.path.isfile(patch):
        lowercase(patch)
    else:
        sys.exit()

arg = sys.argv[1]
arg = os.path.expanduser(arg)
rename(arg)