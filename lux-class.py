# %load_ext line_profiler

# %lprun -f check_driving_license check_driving_license()

"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 22:
    print("You are eligible to apply for a driving license.")
elif age >= 35:
    print(f"Hello, {name}! You are eligible to apply for a driving license and you can also apply for a commercial driving license.")
else:
    print(f"Hello, {name}! You are not eligible to apply for a driving license yet. Please wait until you are 22 years old.")
"""


# creating a class for driving license eligibility
class DrivingLicenseEligibility:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_eligibility(self):
        if self.age >= 22:
            return f"Hello, {self.name}! You are eligible to apply for a driving license."
        elif self.age >= 35:
            return f"Hello, {self.name}! You are eligible to apply for a driving license and you can also apply for a commercial driving license."
        else:
            return f"Hello, {self.name}! You are not eligible to apply for a driving license yet. Please wait until you are 22 years old."


# creating a class for a person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.eligibility = DrivingLicenseEligibility(name, age)

    def check_driving_license(self):
        return self.eligibility.check_eligibility()

# testing the person class

name = input("Enter your name: ")
age = int(input("Enter your age: "))

person = Person(name, age)
print(person.check_driving_license()) 

# class bank account 

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance is {self.balance}."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."

    def check_balance(self):
        return f"Current balance is {self.balance}."

# testing the bank account class
name = input("Enter your Account name: ")
account_number = input("Enter your Account number: ")
account = BankAccount(name, account_number)

print(account.deposit(1000))
print(account.withdraw(500))
print(account.check_balance())