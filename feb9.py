# data types in python - 1) fundamental data types
#Integer Data Type - value without decimal point

price = 100
runs = 40
wickets = 0
temp = -20

# print("The price is ", price)
# print(type(price))         # <class 'int'> indicates that price is integer

# print("The runs is ", runs)
# print(type(runs))

# print("The wickets is ", wickets)
# print(type(wickets))

# print("The temprature is ", temp)
# print(type(temp))

#float data type - value with decimal point

petrol_price = 103.45
overs = 20.4
balance = 100.4

# print("The petrol price is ", petrol_price)
# print(type(petrol_price))  # <class 'float'>

# print("The overs is ", overs)
# print(type(overs))

# print("The balance is ", balance)
# print(type(balance))

#bool data type - Used for logical representation of data

is_present = True
is_secured = True

# print(is_present)
# print(type(is_present))  # <class 'bool'>

# print(is_secured)
# print(type(is_secured))

result = is_present + is_secured
# print(result)  # 2 
# print(type(result))

res = float(result)
# print(type(res))

# print the id of the variable
print(id(price))
print(id(overs))
print(id(petrol_price))
print(id(temp))
print(id(runs))