# CSC 242-901
# Assignment 1 template
# Put your name here Taylor Williams

# List your collaborator(s) here (no more than two other people
# I worked alone
# either directly or indirectly)
# Add a comment in this file with a clear and detailed explanation
# of the contributions of each collaborator

# If you did not collaborate with anyone, say that

# Files without the above information will earn a 0

# Include doc strings for full credit

import random

# Question 1
def mathtutor(n):
    c = 0
    correct = 0
    incorrect = 0
    while c<n:
        number1 = random.randint(0,9)
        number2 = random.randint(0,9)
        plusminus = random.random()
        if plusminus>=.5:
            answer1 = number1 + number2
            print(str(number1) + ' + ' + str(number2) + ' =')
            userAnswer1 = eval(input('Enter your answer:'))
            if answer1 == userAnswer1:
                print('Correct')
                correct += 1
            else:
               print('Incorrect')
               incorrect += 1
        
        else:
            if number1 > number2:
                big = number1
                little = number2
            else:
                big = number2
                little = number1
            answer2 = big - little
            print(str(big) + ' - ' + str(little) +' =')
            userAnswer2 = eval(input('Enter your answer:'))
            if answer2 == userAnswer2:
                print('Correct')
                correct += 1
            else:
                print('Incorrect')
                incorrect += 1
        c+=1
    print('You got ' + str(correct) + ' correct answers out of ' + str(n))
    pass
#Question 2
def find_words(infname, outfname, c):
    inf = open(infname, 'r')
    contents = inf.read()
    inf.close()
    for s in '".,?!;':
        contents.replace(s, ' ')
    contents = sontents.lower
    wlst = contents.split()
    wlst.sort()
    outf = open(outfname, 'w')
    for word in wlst:
        if word[0] == c.lower():
            outf.write(word)
            outf.write('\n')
    outf.close()
    pass

#Question 3
class BankAccount(object):
    pass
