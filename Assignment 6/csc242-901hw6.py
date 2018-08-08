# CSC 242-901
# Assignment 6 template
# Put your name here: Taylor Williams

# List your collaborator(s) here (no more than two other people
# either directly or indirectly): I collaborated with Josh Derosier
# In question 2, we talked about what math was actually going on, and
# what our base case would be. In all questions, subsequent we checked
# eachothers base cases to see if we came up with the same one. We also
# collaborated possible indixes to use as well. More specifically on possible points
# to slice things.
# Add a comment in this file with a clear and detailed explanation
# of the contributions of each collaborator

# If you did not collaborate with anyone, say that

# Files without the above information will earn a 0

# Include doc strings for full credit

# Question 1
def printTriangle(n, indent):
    'Prints a triangle with a base of n at top with indent number of spaces prior'
    if n < 1:
        return
    else:
        print(indent * ' ', n*'*')
        printTriangle(n-2, indent+1)
    pass

# Question 2
def recPowProd(k, n, p):
    'find the product of the numbers between k and n to the pth power'
    if k > n:
        return 1
    elif k == n:
        return k**p
    else:
        prev = recPowProd(k+1, n, p)
        sumation = (prev) * (k**p)
        return sumation
    
    pass
# Question 3
def recNumCount(s):
    'Counts the occurences of numbers in a string'
    if s == '':
        return 0
    elif s[-1].isnumeric():
        return recNumCount(s[:-1])+1
        
    else:
        return(recNumCount(s[:-1]))
    pass


# Question 4
def reversible(lst):
    'Checks to see if a list is reverible'
    if len(lst) == 0 or len(lst)==1:
        return True
    elif lst[0] == lst[-1]:
        return(reversible(lst[1:-1]))
    else:
        return False
    pass

# Question 5
def itemCount(lst):
    'Counts the amount of objects in an arbitrarily nested list exempting []'
    if lst == []:
        return 0
    elif type(lst[-1]) == list:
        x = itemCount(lst[-1])
        return itemCount(lst[:-1]) + x
    else:
        return itemCount(lst[:-1]) + 1
    pass
