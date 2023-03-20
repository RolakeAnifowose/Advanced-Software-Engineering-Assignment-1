import random

class Account(object):
    def __init__(self, name, age, email):
        self.name = name
        self.email = email
        self.accountNumber = random.randint(10000000, 9999999)
        self.age = age
        self.balance = 0
        file_object = open("bank_info.txt", 'a')
        file_object.write(self.name + + " " + str(self.accountNumber) + " " + self.email + " " + str(self.age) + " " + str(self.balance) + '\n')
        file_object.close()

