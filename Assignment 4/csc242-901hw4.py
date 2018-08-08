# CSC 242-901
# Assignment 4  template

# Put your name here Taylor Williams

# List your collaborator(s) here (no more than two other people
# either directly or indirectly) : I collaborated with Josh Derosier

# Add a comment in this file with a clear and detailed explanation
# of the contributions of each collaborator: collaborated on beginning of ProcessTrans

# If you did not collaborate with anyone, say that

# Files without the above information will earn a 0

# Include doc strings for full credit

# Code provided for the assignment
class Money(object):     
     def __init__(self, dollars = 0, cents = 0):
          self.dollars = dollars
          self.cents = cents
     def __str__(self):
          # 2 digits after the decimal point
          return '${0:0=1d}.{1:0=2d}'.format(self.dollars,self.cents)
     def __repr__(self):
          return 'Money({},{})'.format(self.dollars,self.cents)
     def convert(self):
          'convert to Euros; $1 = .72 euros'
          return (self.dollars + self.cents/100)*.72
     def __add__(self, other):
          mycents = self.dollars * 100 + self.cents
          othercents = other.dollars * 100 + other.cents
          allcents = mycents + othercents
          newdollars = allcents // 100
          newcents = allcents % 100
          return Money(newdollars, newcents)
     def __sub__(self, other):
          mycents = self.dollars * 100 + self.cents
          othercents = other.dollars * 100 + other.cents
          allcents = mycents - othercents
          newdollars = allcents // 100
          newcents = allcents % 100
          return Money(newdollars, newcents)
     def __gt__(self, other):
          mycents = self.dollars * 100 + self.cents
          othercents = other.dollars * 100 + other.cents
          return mycents > othercents
     # Method added for the fourth assignment
     def __ge__(self, other):
          mycents = self.dollars * 100 + self.cents
          othercents = other.dollars * 100 + other.cents
          return mycents >= othercents
     def __neg__(self):
          return Money(-self.dollars, self.cents)
     def zero():
          return Money(0,0)

# Modify this class for the assignment
# Make your file completely self-contained, e.g. do NOT use import
# statements and instead define any necessary classes in this file
class BankAccount(object):
     def __init__(self, initBalance = Money.zero()):
          self.balance = initBalance
          self.transactions = []
     def __str__(self):
          return 'Bank account with balance {}'.format(self.balance)
     def deposit(self, amount):
          self.balance = self.balance + amount
          self.transactions.append(amount)
     def withdraw(self, amount):
          if self.balance > amount:
               self.balance = self.balance - amount
               self.transactions.append(-amount)
          else:
               raise WithdrawError('A withdrawal of {} would produce a balance of {}'.format(amount, self.amount)
     def getBalance(self):
          return self.balance
     def getTransactions(self):
          return self.transactions
     def __getitem__(self, index):
          return self.transactions[index]
     # Write this method for the first question
     def __iter__(self):
          return revBankIter(self.transactions)
          pass
     # Method added for the fourth assignment
     def __repr__(self):
          return repr(self.balance)

class WithdrawError(Exception):
     "Defines Withdraw error"
     
     def __init__(self, value = ''):
          self.v=value
     def __str__(self):
          return str(self.v)
     

class DepositError(Exception):
     "Defines deposit error"
     def __init__(self, value = ''):
          self.v=value
     def __str__(self):
          return str(self.v)

class revBankIter(object):
     "a reversed list iterator for Money"
     def __init__(self, s):
          "constructor"
          self.transactions = s
          self.index = len(self.transactions)-1

     def __next__(self):
          if self.index<0:
               raise StopIteration()
          val = self.transactions[self.index]
          self.index -= 1
          return val
# Question 3
def processTrans(fname):
          'carries out functions of file'
          b1 = BankAccount()
          content = open(fname)
          contentlst = content.readlines()
          content.close()
          lst = []
          for line in contentlst:
               line = line.split()
               print(info)
               for i in info:
                    try:
                         if line[0].lower() == 'w':
                              m = Money(eval(line[1]))
                              b1.withdraw(m) #may raise withdraw error
                              print("Withdrawal: ", m)
                              lst.append(m)
                         elif line[0].lower() == 'd':
                              m = Money(eval(line[1]))
                              b1.deposit(m)
                              print("Deposit: ", m)
                              lst.append(m)
                    except WithdrawError as err:
                         print('Withdrawal skipped in file {}: {}'
                                   
                                   
                              
                    except:
                         print('Deposit skipped in trans.txt: deposit of {} is invalid'.format(info[1]))
          return b1
          pass
