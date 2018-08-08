# CSC 242-901
# Assignment 8 template
# Put your name here Taylor Williams

# List your collaborator(s) here (no more than two other people
# either directly or indirectly): I collaborated with Josh Derosier
# we collabed on the base cases and the os commands as we were both unfamiliar with them.
# Add a comment in this file with a clear and detailed explanation
# of the contributions of each collaborator

# If you did not collaborate with anyone, say that

# Files without the above information will earn a 0

# Include doc strings for full credit

import os

# Question 1
def traverse(path, indent):
    'Prints the pathname of every file in the path'
    for file in os.listdir(path):
        fullDirect = os.path.join(path, file)
        try: 
            print (' ' * indent, fullDirect)
            traverse(fullDirect, indent+1)
        except:
            pass
    pass

# Question 2
def countDir(dname, path):
    count = 0
    for file in os.listdir(path):
        fullDirect = os.path.join(path, file)
        file = file.lower()
        if os.path.isdir(fullDirect):
            return count
    pass

# Question 3
def nestingCount(path):
    maxval = 0
    for item in os.listdir(path):
        itemPath = os.path.join(path, item)
        if os.path.isdir(itemPath):
            val = nestingCount(itemPath) + 1
            if val > maxval:
                maxval = val
    return maxval
    pass
