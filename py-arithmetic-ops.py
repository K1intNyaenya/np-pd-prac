# basic arithmetic operations in Python
selling_price = 1000
buying_price = 800
profit = selling_price - buying_price
percentage_profit = (profit/buying_price) * 100

# subtraction
profit = selling_price - buying_price
print("Profit:", profit)

# division
percentage_profit = (profit / buying_price) * 100
print("Percentage Profit:", percentage_profit)

# addition
total_price = selling_price + 500  # assuming another item costs 500
print("Total Price for items A & B:", total_price)

# multiplication
total_cost = selling_price * 2
print("Total Cost for 2 items:", total_cost)


#type conversion(casting)
selling_price = float(selling_price)
buying_price = float(buying_price)

print(type(selling_price))  # Output: <class 'float'>
print(type(buying_price))   # Output: <class 'float'>

#and the vice versa is also possible, from float to int
selling_price = int(selling_price)
buying_price = int(buying_price)
print(type(selling_price))  # Output: <class 'int'> 
print(type(buying_price))   # Output: <class 'int'>

# modulus operator
remainder = selling_price % buying_price
print("Remainder when selling price is divided by buying price:", remainder)

# exponentiation operator
squared_profit = profit ** 2
print("Squared Profit:", squared_profit)

# floor division operator
floor_division_result = selling_price // buying_price
print("Floor Division Result:", floor_division_result)

# operator precedence
result = selling_price + buying_price * 2  # multiplication has higher precedence than addition
print("Result of selling_price + buying_price * 2:", result)