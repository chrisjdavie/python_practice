'''
Going through http://anandology.com/python-practice-book/object_oriented_programming.html

Created on 11 Nov 2015

@author: chris
'''

# Crappy one with globals

# example is good enough only if we want to have just a single account. Things start 
# getting complicated if want to model multiple accounts.

balance = 0

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance += amount
    return balance