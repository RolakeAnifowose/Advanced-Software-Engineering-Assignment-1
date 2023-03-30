
import random 

# class User definition
# parent class
class User():
    def __init__(self, name):
        self.name = name
        
    
    def showDetails(self):
        accountNumber = random.randint(00000000, 99999999)
        # a = accountNumber
        x = 'Personal details'
        y = 'Name: ' + self.name
        z = 'Account balance is now £' + str(self.balance) 
        a = 'Account Number is ' + str(accountNumber)
        result = [x,y,z,a]
        return result
        

# child class Bank definition
class Bank(User):
    def __init__(self, name):
        super().__init__(name)
        self.balance = 0
    
    # defining the deposit method
    def deposit(self, amount):
        self.amount = int(amount)
        self.balance = self.amount + self.balance
        return 'Account balance is now £' + str(self.balance)
    
    # defining the withdraw method
    def withdraw(self, amount):
        self.amount = int(amount)
        if self.amount > self.balance:
            return 'Insufficient funds £' + str(self.balance)
        else:
            self.balance = self.balance - self.amount
            return 'Account balance is now £' + str(self.balance)
    
    # defining the transfer method
    def transfer(self, amount):
        self.amount = int(amount)
        if self.amount > self.balance:
            return 'Insufficient funds £' + str(self.balance)
        else:
            self.balance = self.balance - self.amount
            return 'Account balance is now £' + str(self.balance)
        
    # defining the view balance method
    def viewBalance(self):
        return str(self.balance)

# Ola = Bank('Ola')
# print(Ola.showDetails())
# print(Ola.deposit(1000))
# print(Ola.showDetails()) 
# print(Ola.withdraw(200))   
# print(Ola.showDetails())
