# CSC 242-901
# Assignment 3 template

# Put your name here

# List your collaborator(s) here (no more than two other people
# either directly or indirectly)
# Add a comment in this file with a clear and detailed explanation
# of the contributions of each collaborator

# If you did not collaborate with anyone, say that

# Files without the above information will earn a 0

# Include doc strings for full credit

# Question 1
class Money(object):     
     def __init__(self, dollars = 0, cents = 0):
          "Initializes the money object"
          self.doll = dollars
          if cents > 100:
               extra = cents // 100
               self.doll += extra
               self.cent = cents - (extra * 100)
          else:
              self.cent = cents
          pass
     def __str__(self):
          "Defines how money object will be represented when needed as string"
          if int(self.cent) < 10:
               finalCent = '0{}'.format(self.cent)
          else:
               finalCent = int(self.cent)
          self.normal = '${}.{}'.format(self.doll,finalCent)
          return self.normal
          pass
     def __repr__(self):
          "representation for money object"
          return 'Money({}, {})'.format(self.doll, self.cent)
          pass
     def convert(self):
          "Converts self from dollars to euros"
          euroConvert = self.doll + (self.cent/100)
          conversion = euroConvert * 0.72
          return(conversion)
          pass
     def __add__(self, other):
          "overloads the add function"
          total = self.doll*100 + self.cent
          otherTotal = other.doll*100 + other.cent
          final = total + otherTotal
          finalDoll = final // 100
          finalCent = final - (finalDoll*100)
          finalAdd = Money(finalDoll, finalCent)
          return finalAdd
          pass
     def __sub__(self, other):
          "overloads the subtract function"
          total = self.doll*100 + self.cent
          otherTotal = other.doll*100 + other.cent
          final = total - otherTotal
          finalDoll = final // 100
          finalCent = final - ((finalDoll*100))
          finalMoney = Money(finalDoll, finalCent)
          return finalMoney
          pass
     def __gt__(self, other):
          "Overloads the greater than/less than function"
          return float(self.doll*100+self.cent) > float(other.doll*100+other.cent)
          pass
     def __neg__(self):
          "Assigns negative to self"
          total = self.doll*100 + self.cent
          negTotal = total
          negDoll = negTotal // 100
          negCent = negTotal - (negDoll*100)
          newSelf = Money(-negDoll,negCent)
          return newSelf
          pass
     def zero():
          "Creates new money object with 0 throughout"
          return (Money())
          pass          

# Question 2
class BankAccount(object):
     def __init__(self, initBalance = Money.zero()):
          "initializes BankAccount object"
          self.account = initBalance
          self.transactions = []
          pass
     def __str__(self):
          "Defines how BankAccount object should be represented in a string"
          self.baccount = 'Bank account with balance {}'.format(self.account)
          return self.baccount
          pass
     def deposit(self, amount):
          "adds amount to bank account and appends transaction"
          self.account = self.account + amount
          self.transactions.append(amount)
     def withdraw(self, amount):
          "records transaction and subtracts money from bank account"
          self.account = self.account - amount
          self.transactions.append(-amount)
          pass
     def getBalance(self):
          "returns balance of bank account"
          return(self.account)
          pass
     def getTransactions(self):
          "shows all transactionslinked to that bank account"
          return(self.transactions)
          pass
     def __getitem__(self, index):
          "allows user to call an index from list of transactions and to see it"
          return self.transactions[index]
          pass

