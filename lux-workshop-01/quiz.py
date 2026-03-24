# sum of two numbers
"""
n1 = 100
n2 = 150

print(n1 + n2)

# concatenating two strings
first_name = input("Please enter your first name: ").upper()
second_name = input("Please enter your second name: ").upper()


print(first_name + " " + second_name)
print(f" My name is {first_name} {second_name}")

# control flow, checking if your first name is equual to second name 
if first_name == second_name:
    print("Your first name is the same as your second name")
else:
    print("Your first name is not the same as your second name")

# check the sum of two numbers is an even number or odd number
n1 = int(input("Please enter the first number: "))
n2 = int(input("Please enter the second number: "))

if (n1 + n2) % 2 == 0:
    print("The sum of n1 and n2 is an even number")
else:
    print("The sum of n1 and n2 is an odd number")

# check if 250 is greater than 100, less than 100 or equal to 100
n3 = int(input("Please enter a number: "))
if n3 > 100:
    print("True")
elif n3 < 100:
    print("True")
else:
    print("False")

# Data structures: list, tuple, set, dictioary
# list
food = ["chicken", "samaki", "nyama choma", "ugali"]

# add an item to the list
food.append("pilau")
print(food)

print(food[0]) # access the first item in the list

# change an item in the list
food[0] = "beef"
print(food)


person = ["John", 25, "Engineer", "Nairobi", "Kenya", "Kenyan", "football", "music", "traveling", "cooking"]


replace_item = input("Which item do you want to replace? ")
new_item = input("What is the new item? ")  
if replace_item in person:
    index = person.index(replace_item)
    person[index] = new_item
    print(person)
else:    
    print("Item not found in the list")



# replace an item in the list person
person = ["John", 25, "Engineer", "Nairobi", "Kenya", "Kenyan", "football", "music", "traveling", "cooking"]
print(person)

replace_item = input("Which item do you want to replace? ")
new_item = input("What is the new item? ")
if replace_item in person:
    index = person.index(replace_item)
    person[index] = new_item
    print(person)
else:
    print("Item not found in the list")



# dictionaries
person = {
    "name": "John",
    "age": 25,
    "profession": "Engineer",
    "city": "Nairobi",
    "country": "Kenya",
    "nationality": "Kenyan",
    "hobbies": ["football", "music", "traveling", "cooking"]
}

# print hobbies of the person
print(person["hobbies"])

# print traveling from the hobbies of the person
print(person["hobbies"][2])

# delete an item from the dictionary
del person["city"]
print(person)

# add an item to the dictionary
person["city"] = "Mombasa"
print(person)

# tuples
coordinates = (10, 20)
print(coordinates)

# sets
fruits = {"apple", "banana", "orange", "grape"}
print(fruits)



# functions
def add_numbers(n1 = 45, n2 = 55):
    return n1 + n2  
"""

# opening a txt file and reading its contents
with open("../MOCK_DATA.txt", "r") as file:
    data = file.read()
    print(data) 