#Python Strings and  Strings Operations
# String is a sequence of character ensclosed in a single quote or double quotes

name = 'Clinton'
number = '12345' # a number but it is treated as a string if it is enclosed in quotes
status = 'True' # a boolean but it is treated as a string if it is enclosed in quotes

# String operations
# newline character

print("Hello \n World") # \n is a newline character that creates a new line

# tab character
print("Hello\tWorld") # \t is a tab character that creates a tab space

# string concatenation
first_name = 'Clinton'
last_name = 'Ombui'

print(first_name + ' ' + last_name) # concatenating first name and last name with a space in between

# str indexing
name = 'Clinton'

print(name[0]) # accessing the first character of the string
print(name[1]) # accessing the second character of the string
print(name[-1]) # accessing the last character of the string
print(name[-2]) # accessing the second last character of the string

# str slicing
print(name[0:3]) # accessing the first three characters of the string
print(name[3:6]) # accessing the characters from index 3 to index 6
print(name[:3]) # accessing the first three characters of the string
print(name[::2]) # accessing every second character of the string
print(name[::-1]) # reversing the string

# looping through a string
for char in name:
    print(char.upper()) # printing each character of the string on a new line

# string length
print('The length of ' + name + ' is ' + str(len(name))) # printing the length of the string

# membership operator
print('t' in name) # checking if 't' is in the string
print('z' in name) # checking if 'z' is in the string

print('t' not in name) # checking if 't' is not in the string
print('z' not in name) # checking if 'z' is not in the string

# string methods
print(name.upper()) # converting the string to uppercase
print(name.lower()) # converting the string to lowercase
print(name.capitalize()) # capitalizing the first character of the string
print(name.title()) # capitalizing the first character of each word in the string
print(name.strip()) # removing any leading or trailing whitespace from the string

print(name.replace('o', '0')) # replacing 'o' with '0' in the string
print(name.split('n')) # splitting the string into a list using 'n' as the delimiter
print(name.find('o')) # finding the index of the first occurrence of 'o'
print(name.count('o')) # counting the number of occurrences of 'o' in the string    


# To review all other string methods like isalpha(), isdigit(), isspace(), startswith(), endswith(), join(), format(), f-strings, and how to use them in different scenarios.
print(name.isalpha()) # checking if all characters in the string are alphabetic
print(name.isdigit()) # checking if all characters in the string are digits
print(name.isalnum()) # checking if all characters in the string are alphanumeric
print(name.isspace()) # checking if all characters in the string are whitespace
print(name.startswith('C')) # checking if the string starts with 'C'
print(name.endswith('n')) # checking if the string ends with 'n'
print(' '.join(name)) # joining the characters of the string with a space in between
print('My name is {}'.format(name)) # using the format method to insert the string into another string
print(f'My name is {name}') # using f-strings to insert the string into another string


## Boolean values and Boolean operations
# Boolean values are either True or False
x = 9
y = 10

print(x > y) # checking if x is greater than y
print(x < y) # checking if x is less than y
print(x == y) # checking if x is equal to y
print(x != y) # checking if x is not equal to y
print(x >= y) # checking if x is greater than or equal to y
print(x <= y) # checking if x is less than or equal to y

# prac question
score = int(input("Enter your score: "))
print(score >= 50) # checking if the score is greater than or equal to 50

# prac question 2 to check if a number is positive or negative
number = int(input("Enter a number: "))
print(number > 0) # checking if the number is greater than 0

# prac question 3 to check if a number is even or odd
number = int(input("Enter a number: "))
print(number % 2 == 0) # checking if the number is even
print(number % 2 != 0) # checking if the number is odd