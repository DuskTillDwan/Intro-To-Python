# CSC 242-901
# Assignment 5 template
# Put your name here: Taylor Williams

# List your collaborator(s) here (no more than two other people
# either directly or indirectly): Josh Derisier
# Add a comment in this file with a clear and detailed explanation
# of the contributions of each collaborator I collaborated with Josh on this assignment
# i assisted him a large amount on constructing using packing, and grids, and tk windows. For the
#second problem we worked together ono solving the math. I unfortunatly ran out of time to complete the assignmment before work.

# If you did not collaborate with anyone, say that

# Files without the above information will earn a 0

# Include doc strings for full credit

from tkinter import Label, Frame, Entry, Button, LEFT, RIGHT, END
from tkinter.messagebox import showinfo
from random import randint

# Question 1
class Game(Frame):
    'Number guessing application'
    def __init__(self,parent=None):
        'constructor'
        Frame.__init__(self, parent)
        self.pack()
        self.count = 0
        Game.make_widgets(self)
        Game.new_game(self)
        

    def make_widgets(self):
        'create the widgets for the GUI and attach the handler'
        self.val = randint(1, 100)
        Label(self, text='Enter your guess:').pack()
        self.guess = Entry(self, width = 20)
        self.guess.pack()
        Button(self, text = 'Enter', width = 11, command = self.reply).pack()
        pass

    def new_game(self):
        'Starts a new game when correct guess in made'
        self.val = randint(1, 100)
        pass

    def reply(self):
        'the handler for the button "enter"'
        try:
            self.evalguess = eval(self.guess.get())
            if self.evalguess == self.val:
                showinfo(title= 'Congratulations', message = 'You got it!\n It took you {} tries.'.format(self.count))
                self.guess.delete(0, END)
                self.count = 0
                Game.new_game(self)
            elif self.evalguess > self.val:
                showinfo(title = 'Report', message = '{} is too high'.format(self.evalguess))
                self.guess.delete(0, END)
                self.count += 1
            else:
                showinfo(title = 'Report', message = '{} is too low.'.format(self.evalguess))
                self.guess.delete(0, END)
                self.count += 1
        except:
            showinfo(title = 'Oooops!', message = 'Invalid number.')
            self.guess.delete(0, END)
        pass
#Game().mainloop()

# Question 2
class CreditCard(Frame):
    'credit card interest calculation app'
    
    def __init__(self,parent=None):
        'constructor'
        Frame.__init__(self, parent)
        # If you use pack for the widgets in make_widgets, change
        # this to pack
        self.grid()
        CreditCard.make_widgets(self)

    def make_widgets(self):
        'makes widgets for the gui and the handler'
        Label(self, text = 'Enter the Balance:').grid(row = 0, column = 0, columnspan = 3)
        self.balance = Entry(self, width = 20)
        self.balance.grid(row = 0, column = 4, columnspan = 3)
        Label(self, text = 'Enter the interest rate (e.g. 9% = 0.09):').grid(row = 1, column = 0, columnspan = 3)
        self.interest = Entry(self, width = 20)
        self.interest.grid(row = 1, column = 4, columnspan = 3)
        Label(self, text = 'Enter the amount of the monthly payment:').grid(row = 2, column = 0, columnspan = 3)
        self.payment = Entry(self, width = 20)
        self.payment.grid(row = 2, column = 4, columnspan = 3)
        Button(self, text = 'Compute total', width = 11, command = self.compute).grid(row = 3, column = 1, columnspan = 3)
        pass

    def compute(self):
        'handler for compute button'
##        try:
        self.balance2 = eval(self.balance.get())
        
        self.otherbalance = eval(self.balance.get())
        self.otherinterest = eval(self.interest.get())
        self.otherpayment = eval(self.payment.get())
        self.months = 0
        self.totalPayment = 0
        while self.balance2 > 0:
            self.otherbalance = (self.balance2 - self.otherpayment)
            self.months += 1
            self.balance2 = (self.otherbalance * self.otherinterest) + self.otherbalance
            showinfo(title = 'results', message = 'It will take {} months to pay off the balance and require a total payment of $.'.format(self.months))
                
##        except:
##            showinfo(title = "Oooops", message = 'Invalid number')
##            self.balance.delete(0, END)
##            self.interest.delete(0, END)
##            self.payment.delete(0, END)
        pass
CreditCard().mainloop()
