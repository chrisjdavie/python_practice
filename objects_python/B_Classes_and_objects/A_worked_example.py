'''
Standard class and inheritance example

Created on 11 Nov 2015

@author: chris
'''
def main():
    a = BankAccount()
    b = BankAccount()
    
    print a.deposit(100)
    print b.deposit(50)
    print b.withdraw(10)
    print a.withdraw(10)
    
    c = MinimumBalanceAccount(0)
    print c.deposit(15)
    print c.withdraw(10)
    print c.withdraw(10)
    

class BankAccount:
    def __init__(self):
        self.balance = 0
        
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print 'Sorry, minimum balance must be maintained'
        else:
            BankAccount.withdraw(self, amount)
            
        return self.balance
        

if __name__ == '__main__':
    main()