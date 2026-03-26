'''
1) positional argument : position of arguments is important.
'''
def subTwo(n1,n2):
    return n1-n2
a = 10
b = 20
res1 = subTwo(a,b)
res2 = subTwo(b,a)
print(res1) # -10
print(res2) # 10

'''
2) keyword argument: positon of the argument is not important
                     we pass the data in the form of keynad value.
'''
def subTwo(n1,n2):
    return n1-n2
a = 10
b = 20
res1 = subTwo(n2 = a,n1 =  b)
print(res1) # 10

'''
3) Default arguments : we can pass deafault values to function

Note : deafault arguments must be at last position in the function defination
'''
def registerEmp(eid,ename,sal,dept,c_name):
    print(eid,ename,sal,dept,c_name)

registerEmp(101,"sakshi",23000,"QA","tcs") # 101 sakshi 23000 QA Tcs

def registerEmp(eid,ename,sal,dept,c_name="Tcs"):
    print(eid,ename,sal,dept,c_name)

registerEmp(101,"sakshi",23000,"QA") # 101 sakshi 23000 QA Tcs

def registerEmp(eid,ename,sal=12000,dept,c_name):
    print(eid,ename,sal,dept,c_name)

registerEmp(101,"sakshi","QA","tcs") # SyntaxError: parameter without a default follows parameter with a default

def registerEmp(ename,sal,dept,c_name="Tcs",eid=None):
    print(eid,ename,sal,dept,c_name)

registerEmp("sakshi",23000,"QA",eid=101) # 101 sakshi 23000 QA Tcs
registerEmp("sakshi",23000,"QA",c_name="Wipro",eid=102) # 102 sakshi 23000 QA Wipro

'''
4) variable lenght (arbitary) argument
                    1) positional arbitary argument :- data is passed in tuple format
                    2) keyword argument :- data is passed in dictionary(key,value) format
'''

def subTwo(n1,n2):
    return n1-n2
subTwo(10) # TypeError: subTwo() missing 1 required positional argument: 'n2'
subTwo(10,20,30) # subTwo() takes 2 positional arguments but 3 were given

# positional arbitary arguments
def addition(*args):
    print(args,type(args))
    print(args[0],args[1])
    s = 0
    for i in args:
        s += i
    return s
res = addition(10,20,30)
print("sum :",res)
res1 = addition(10,20,30,7,6,4,3)
print("sum :",res1)
'''
(10, 20, 30) <class 'tuple'>
10 20
sum : 60
(10, 20, 30, 7, 6, 4, 3) <class 'tuple'>
10 20
sum : 80
'''

# keyword arbitry arguments
def addition(**kwargs):
    print(kwargs,type(kwargs))
    print(kwargs.get('n1'))
    print(kwargs.keys())
    
addition(n1=10,n2=20,n3=30)
'''
{'n1': 10, 'n2': 20, 'n3': 30} <class 'dict'>
10
dict_keys(['n1', 'n2', 'n3'])
'''
