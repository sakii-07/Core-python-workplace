'''
Tuple ----> Tuple is immutable , heretogenious collection of element where 
            insertin order is maintained and duplicated are allowed

Immutable ----> we can not insert, update, delete, append elements from tuple

'''

t = (10,20,30,40,50,50)
print(type(t)) # <class 'tuple'>
print(t) # (10, 20, 30, 40, 50, 50)
print(t[1]) # 20
print(len(t)) # 6

# single element in tuple gives data type which type of data insered
t1 = (10)
print(type(t1)) # <class 'int'>

t2 = ("saki")
print(type(t2)) # <class 'str'>

t3 = (10.4)
print(type(t3)) # <class 'float'>

# if we want to make tuple with single value then give comma at last
t5 = (10,)
print(type(t5)) # <class 'tuple'>

# empty tuple
t6 = ()
print(type(t6)) # <class 'tuple'>

# we can not modify data in tuple
t1 = (10,20,30,40)
t1[2] = 200
print(t1) # TypeError: 'tuple' object does not support item assignment

# we can insert , update, detele, append element in tuple
t.append(10)
t.add(20)

l1 = [10]
print(type(l1)) # <class 'list'>

l2 = [10,]
print(type(l2)) # <class 'list'>

t7 = (1,2,3,4,[21,3,2,4],9,8,7)
print(t7) # (1, 2, 3, 4, [21, 3, 2, 4], 9, 8, 7)
print(type(t7)) # <class 'tuple'>
print(t7[4]) # [21, 3, 2, 4]

'''
Packing and Unpacking in list and tuple :-

Packing ---->  many variable (list or tuple) into single variables
'''

e1 = "T-shirt"
e2 = "jeans"
e3 = "cash"
e4 = "charger"

# Automatically packing of the elements into a tuple
bag = e1,e2,e3,e4 # Tuples creates by default
print(bag) # ('T-shirt', 'jeans', 'cash', 'charger')
print(type(bag)) # <class 'tuple'>

bag1 = [e1,e2,e3,e4] # list created manually
print(bag1) # ['T-shirt', 'jeans', 'cash', 'charger']
print(type(bag1)) # <class 'list'>

'''
UnPacking ---->  single variable (list or tuple) into many variables
'''

v1,v2,v3,v4 = bag # tuple unpacking
print(v1)
print(v2)
print(v3)
print(v4)

v5,v6,v7,v8 = bag1 # list unpacking
print(v5)
print(v6)
print(v7)
print(v8)

# swap two variables using packing and unpacking
a = 10
b = 20
print("before swapping : a = ",a,"b = ",b)
t = a,b
b,a =t
print("After swapping : a = ",a,"b = ",b)

# swap two variables without using third variable in packing and unpacking
a = 10
b = 20
print("before swapping : a = ",a,"b = ",b)
a,b = b,a
print("After swapping : a = ",a,"b = ",b)

# swap two variables  using mathematics
a = 10
b = 20
print("before swapping : a = ",a,"b = ",b)
a = a + b
b = a - b
a = a - b
print("After swapping : a = ",a,"b = ",b)

# swap two variables using third variable
a = 10
b = 20
print("before swapping : a = ",a,"b = ",b)
temp = a
a = b
b = temp
print("After swapping : a = ",a,"b = ",b)
