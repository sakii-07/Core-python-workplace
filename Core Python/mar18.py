# pure fuction - fuction with return statement
def f1(a,b):
    res = a + b
    print(res)
f1(10,20) # 30

def f1(a,b):
    res = a + b
    return res
r = f1(10,20) 
print(r) # 30

def f2():
    a = 10
    return "a"
r1 = f2()
print(r1) # a

def f2():
    a = 10
    return a
r1 = f2()
print(r1) # 10

def f2():
    a = 10
    return -34
r1 = f2()
print(r1) # -34

def f2():
    a = 10
    return True
r1 = f2()
print(r1) # True

def f2():
    a = 10
r1 = f2()
print(r1) # None
''' If a function does not return anything, Python returns :- None 
None ----> none is data type in python 

Any datatype we can return form a function

'''

a = 10
res = print(a) # 10 - print returns None
print(res) # None

print(print(print(10))) # first executes the inner print statement and returns none, after that another print statements executes inner to outer side
'''
10
None
None
'''

'''
Q. can we return multiple values at a time from a function?
--> yes, we can return multiple values at a time
'''
def f1():
    return 10,"saki",20
res = f1()
print(type(res)) # <class 'tuple'>
a,b,c = f1() # tuple unpacking
print(a) # 10

'''Any datatype we can return form a function'''
def f1():
    return 10,"saki",20
res = f1()
print(res) # (10, 'saki', 20)

def f1():
    return [10,"saki",20]
res = f1() 
print(res) # [10, 'saki', 20]

p = 30
def f1():
    p=p+2
    print(p)
f1() # UnboundLocalError: cannot access local variable 'p' where it is not associated with a value

p = 30
def f1():
    print(p)
f1() # 30
'''we can not directly change global variable value from local scope
global ---> give rights to a variable to change inside a function
'''

p = 30
def f1():
    global p
    p=p+2
    print(p) # 32
f1()

p = 30
def f1():
    global p
    p=60
    print(p) # 60
f1()