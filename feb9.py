# data types in python - 1) fundamental data types
#Integer Data Type - value without decimal point

price = 100
runs = 40
wickets = 0
temp = -20

print("The price is ", price)
print(type(price))         # <class 'int'> indicates that price is integer

print("The runs is ", runs)
print(type(runs))

print("The wickets is ", wickets)
print(type(wickets))

print("The temprature is ", temp)
print(type(temp))

#float data type - value with decimal point

petrol_price = 103.45
overs = 20.4
balance = 100.4

print("The petrol price is ", petrol_price)
print(type(petrol_price))  # <class 'float'>

print("The overs is ", overs)
print(type(overs))

print("The balance is ", balance)
print(type(balance))

#bool data type - Used for logical representation of data

is_present = True
is_secured = True

print(is_present)
print(type(is_present))  # <class 'bool'>

print(is_secured)
print(type(is_secured))

result = is_present + is_secured
print(result)  # 2 
print(type(result))

res = float(result)
print(type(res))

# print the id of the variable
print(id(price))
print(id(overs))
print(id(petrol_price))
print(id(temp))
print(id(runs))

# types of typecasting
#  1) internal or implicite 
#  2) external or explicite - int, float, bool, complex, eval, list, tuple, disk, set

num = complex(input("Enter number"))
print(num)
print(type(num))

num1 = int(input("Enter number")) # if we gives float number then it gives error
print(num1)
print(type(num1))

num2 = float(input("Enter number")) # if we gives int number then it gives float
print(num2)
print(type(num2))

num3 = list(input("Enter number")) # 
print(num3)
print(type(num3))

num4 = str(input("Enter number ")) # 
print(num4)
print(type(num4))

str1 = "10+5j"
print(bool(str1)) # it works with all datatypes but not with int and float. we can not convert complex to int and float
print(type(str1))
