#parent class
import random 

class Customer():
    def __init__(self, name):
        self.name = name
        
    
    def showDetails(self):
        accountNumber = random.randint(00000000, 99999999)
        # a = accountNumber
        x = 'Personal details'
        y = 'Name: ' + self.name
        z = 'Account balance is now £' + str(self.balance) 
        result = [x,y,z]
        #return f"Hi, {self.name}, thanks for banking with us.Your newly assigned account number is {accountNumber}" 
        



#child class
class Bank(Customer):
    def __init__(self, name):
        super().__init__(name)
        self.balance = 0
    
    def deposit(self, amount):
        self.amount = int(amount)
        self.balance = self.amount + self.balance
        return 'Account balance is now £' + str(self.balance)
    
    def withdraw(self, amount):
        self.amount = int(amount)
        if self.amount > self.balance:
            return 'Insufficient funds £' + str(self.balance)
        else:
            self.balance = self.balance - self.amount
            return 'Account balance is now £' + str(self.amount)
    
    def transfer(self, amount):
        self.amount = int(amount)
        if self.amount > self.balance:
            return 'Insufficient funds £' + str(self.balance)
        else:
            self.balance = self.balance - self.amount
            return 'Account balance is now £' + str(self.amount)

    def viewBalance(self):
        return self.showDetails()


    

