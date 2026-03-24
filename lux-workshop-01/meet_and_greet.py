# creating a function to greet people

def greet(name, course):
    print(f"Hello, {name}! Welcome to the {course} Workshop!")

name = input("Please enter your name: ")
course = input("Which course are you attending? ")
greet(name, course)

# calculator function for all functions
def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ")
result = calculator(num1, num2, operation)
print(f"The result of {operation}ing {num1} and {num2} is: {result}")