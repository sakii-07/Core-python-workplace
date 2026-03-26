'''
Lambda function
'''

f = lambda a,b:a+b
print(f(10,20)) # 30

print((lambda a,b:a*b)(10,20)) # 200

# square of number
print((lambda q:q*q)(10)) # 100

# create a lambda function which finds maximum number from two nums
f1 = lambda a,b:a if a>b else b
print(f1(45,90)) # 90

# max = num1 if num1>num2 else num2 # ternary operators

# find given number is even or odd
f3 = lambda num:"even number" if num%2==0 else "odd number"
print(f3(40)) # even number

'''
lambda is used with HOF(high order function)
'''
l = [1,3,4,67,6,7,8,9,0,34]
square_list = list(map(lambda num:num*num,l))
print(square_list) # [1, 9, 16, 4489, 36, 49, 64, 81, 0, 1156]

# filter all even numbers from given list
even_num = list(filter(lambda num:True if num%2==0 else False , l))
l = [1,3,4,67,6,7,8,9,0,34]
print("Original list :",l) 
print("Even number list :",even_num) 
'''
Original list : [1, 3, 4, 67, 6, 7, 8, 9, 0, 34]
Even number list : [4, 6, 8, 0, 34]
'''

# convert this name list into upper case name list
names = ["Raj","Pavan","Nayan","Rahul"]
upper_case = list(map(lambda name:name.upper(),names))
print("Upper case list : ",upper_case) # Upper case list :  ['RAJ', 'PAVAN', 'NAYAN', 'RAHUL']

# filter student who get less than 75 marks in subject.
db = [("Raj",89),("Pavan",67),("Nayan",99),("Rahul",56)]
std = list(filter(lambda std: std[1]<75 ,db))
print(std) # [('Pavan', 67), ('Rahul', 56)]

# Task - filter all even numbers and create it square list
l = [1,3,4,67,6,7,8,9,0,34]
square_even_num = list(map(lambda num:num**2,filter(lambda num:True if num%2==0 else False,l)))
print(square_even_num) # [16, 36, 64, 0, 1156]