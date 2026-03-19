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


name = input("Enter your name: ")
age = int(input("Enter your age: "))

person = Person(name, age)
print(person.check_driving_license()) 