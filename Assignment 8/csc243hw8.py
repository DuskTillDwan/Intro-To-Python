# CSC 243-501
# Assignment 8 template

# Stephanie Nordlund

# 

import os

# Question 1
def traverse(path, indent):
    'Takes a file name and prints all contained subfolders and files'
   
    for item in os.listdir(path):
        n = os.path.join(path,item)
        if os.path.isdir(n):
            print(' ' * indent + n)
            
            indent += 4
            traverse(n, indent)
            indent -= 4
            
        if os.path.isfile(n):
            
            print(' ' * indent  + n)
            
          
# Question 2
def search(fname, path):
    'searches for a file in a directory and it\'s sub directories and returns the path name where the file can be found'
    if fname in os.listdir(path):
        return os.path.join(path, fname)
    else:
        for item in os.listdir(path):
            n = os.path.join(path,item)
            if os.path.isdir(n):
                p = search(fname, n)
                return p
            if os.path.isfile(n):
                pass
                
                

# Question 3
def fileCount(path):
    'Returns a number representing the count of files found in all sub directories'
    fileflow = 0
    for item in os.listdir(path):
        n = os.listdir(path)
        if os.path.isfile(n):
            fileflow += 1
        else:
            r = fileCount(n)
            return r
    return fileflow

# Question 4
def nestingCount(path):
    'Returns a number representing the maximum number of sub directories found within'
    maxpath = 0
    for item in os.listdir(path):
        d = os.path.join(path, item)
        if os.path.isdir(d):
            val = nestingCount(d) + 1
            if val > maxpath:
                maxpath = val
    return maxpath


