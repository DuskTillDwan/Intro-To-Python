# CSC 242-901
# Assignment 7 template
# Put your name here

# List your collaborator(s) here (no more than two other people
# either directly or indirectly): I collaborated with Josh Derosier
# we discussed base cases for all subsequent problems as well as possible
# indexes for slicing for question 3
# Add a comment in this file with a clear and detailed explanation
# of the contributions of each collaborator

# If you did not collaborate with anyone, say that

# Files without the above information will earn a 0

# Include doc strings for full credit

# Question 1
def crawl(fname):
    'Crawls through files following "links" in said files'
    if fname == '':
        pass
    else:
        print('Visiting {}'.format(fname))
        infile = open(fname)
        content = infile.read()
        lines = content.split()
        
        for line in lines:
            crawl(line)
        
    pass

# Question 2
def recStrMix(s):
    'Mixes the string s'
    if len(s) < 5:
        return(s)
    else:
        first = recStrMix(s[0:2])
        last = recStrMix(s[-2:])
        rest = recStrMix(s[2:-2])
        return first+last+rest 
    pass

# Question 3
def recListSum(lst):
    'Sums the numbers in an arbitrarily nested list (excluding those in dictionaries and tuples)'
    if lst == []:
        return 0
    elif type(lst[-1]) == int or type(lst[-1]) == float:
        return lst[-1] + recListSum(lst[:-1])
    elif type(lst[-1]) == list:
        y = recListSum(lst[-1])
        rest = recListSum(lst[:-1])
        return y + rest
    else:
        rest = recListSum(lst[:-1])
        return rest
    pass

# Question 4
def depthCount(lst):
    'counts the max depth of nested lists in a list'
    if lst == []:
        return 0
    elif type(lst[-1]) == list:
        first = depthCount(lst[-1])
        rest = depthCount(lst[:-1])
        return 1 + first + rest
    else:
        return depthCount(lst[:-1]) 
    pass
