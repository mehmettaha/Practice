import os, glob, re

def print_directory_contents(sPath):
    a = os.listdir(sPath)
    print(a)
    for i in a:
        if "." not in i:
            newpath = (sPath + "/" + i)
            print_directory_contents(newpath)

print_directory_contents(os.curdir)