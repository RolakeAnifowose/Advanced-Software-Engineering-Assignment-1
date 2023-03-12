#define class customer
class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_details(self):
        return f"Welcome, {self.name.title()}."

class Bank(Customer):
    total_deposits = 0
    total_withdrawals = 0

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance

    def show_balance(self):
        return f"Hi {self.name.title()}, your account balance is £{round(self.balance, 2)}"
    
    def deposit(self):
        deposit_amount = float(input(f"Hi {self.name.title()}, please input the amount you will like to deposit"))
        print("Thank you for your transaction...")
        self.balance += deposit_amount
        self.total_deposits += 1
        return f"Your transaction was successful, your account balance is now £{round(self.balance, 2)}"
    
    def withdraw(self):
        withdraw_amount = float(input(f"Hi {self.name.title()}, how much will you will like to withdraw?"))
        if withdraw_amount > self.balance:
            return f"You do not have sufficient amount for this transaction."
        else:
            print("Thank you for your transaction")
            self.balance -= withdraw_amount
            self.total_withdrawals += 1
            return f"Your current account balance is now £{round(self.balance, 2)}"

def options(customer_two):
    print("Welcome to Cloud Bank\n Thank you for banking with us.")
    print("Kindly choose the number that corresponds to your intended transaction type")
    while True:
        option_choice = int(input("1 - Account Balance\n 2 - Withdrawal\n 3 - Deposit\n 4 - Transfer\n 5 - Total Withdrawals\n 6 - Total Deposits\n 7 - Quit\n "))
        if option_choice == 1:
            print(customer_one_bank.show_details())
            if option_choice == 1 and customer_two != None:
                print(customer_two_bank.show_details())
        elif option_choice == 2:
            print(customer_one_bank.withdraw())
            if option_choice == 2 and customer_two != None:
                wd = input(f"{customer_two.name}, please confirm if you will like to withdraw by typing Yes or No ")
                if wd.lower() == "yes":
                    print(customer_two_bank.withdraw())
        elif option_choice == 3:
            print(customer_one_bank.deposit())
            if option_choice == 3 and customer_two != None:
                dep = input(f"{customer_two.name}, please confirm if you will like to deposit by typing Yes or No")
                if dep.lower == "yes":
                    print(customer_two_bank.deposit())
        elif option_choice == 5:
            print(f"You have performed {customer_one_bank.total_withdrawals} withdraws.")
            if option_choice == 5 and customer_two != None:
                print(f"You have performed {customer_two_bank.total_withdrawals} withdraws.")
        elif option_choice == 6:
            print(f"You have performed {customer_one_bank.total_deposits} deposits.")
            if option_choice == 6 and customer_two != None:
                print(f"You have performed {customer_two_bank.total_deposits} deposits.")
        elif option_choice == 7:
            print(f"Thank you for using Cloud Bank, {customer_one_bank.name}")
            if option_choice == 7 and customer_two != None:
                print(f"Thank you for using Cloud Bank, {customer_two_bank.name}")
            return False
            break
        else:
            print("Please choose a transaction number from 1 - 7.")

def create_bank(name):
    balance = float(input(f"{name.title()}, how much money do you have?"))
    return balance

while True:
    print("Welcome to Cloud Bank")
    name = input("Enter your name")
    age = int(input("Enter your age as at your last birthday"))
    customer_one = Customer(name, age)
    customer_two = None
    new_user = input("Would you like to register a new person? Type 'No' to proceed with creating your account")
    if new_user.lower() == 'yes':
        name = input("Enter the second person's name")
        age = int(input("Enter the second person's age as at their last birthday"))
        customer_two = Customer(name, age)
        print("Thank you for registering 2 people. Kindly proceed to create your bank accounts.")
        customer_one_balance = create_bank(customer_one.name)
        customer_two_balance = create_bank(customer_two.name)
        customer_one_bank = Bank(customer_one.name, customer_one.age, customer_one_balance)
        customer_two_bank = Bank(customer_two.name, customer_two.age, customer_two_balance)
        flag = options(customer_two)
        if flag == False:
            break
    else: 
        customer_one_balance = create_bank(customer_one.name)
        customer_one_bank = Bank(customer_one.name, customer_one.age, customer_one_balance)
        flag = options(customer_two)
        if flag == False:
            break