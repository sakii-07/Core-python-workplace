'''
3) Polymorphism ---> It is one of the important pillar of OOP
                     Same name entity behaves differently at different time is called polymorphism
                     poly --> many
                     morphs --> forms
                     we have two types of polymorphism
                                1) overloading
                                        i) operator overloading
                                2) overrinding
                                        i) method overriding
                                        ii) variable overriding
'''
# examples
print(10+20)
print("Ten"+"Twenty")

len("Insta")
len([1,2,3,4])

class Book:

    def __init__(self,t,p):
        self.title = t 
        self.price = p

    # def __add__(self,other):
    #     return self.price + other.price
    
    def __add__(self,other):
        return self.title + other.title
    
    def __sub__(self,other):
        return self.price - other.price

b1 = Book("Core python",250)
b2 = Book("Advance python",450)
b3 = Book("abcd")
print(b1 + b2) # TypeError: unsupported operand type(s) for +: 'Book' and 'Book'
print(b1 + b2) # 700 - After opeartor overloading
print(b1 - b2) # -200

###
n1 = 10
n2 = 20
print(n1+n2)
print(n1.__add__(n2))

'''
method / constructor overloading ----> multiple same name constuctors or method in a class with diff parameters
                                       is called method overloading

python doesnt sopport method/constuctor overloading because of python is dynamically type 
programming language there is no need of method or constuctor overloading.
most recent constructor / ethod will always run.
'''

class Book:

    def __init__(self,t,p):
        self.title = t 
        self.price = p

    def __init__(self,t):
        self.title = t 

    def __init__(self,t,p,a):
        self.title = t 
        self.price = p
        self.author = a

    def m1(self):
        print(000)

    def m1(self,n1):
        print(111)

b1 = Book("Core python",250,"xyz")
# print(b1.author) # xyz
# b2 = Book("Advance python") # TypeError: Book.__init__() missing 2 required positional arguments: 'p' and 'a'
'''
2) overriding
        i) method overriding --> Re-defining parent class method into chlid class is called 
        mathod overriding.                               
'''
class Parent:
    def property(self):
        print(["Gold","Land","house"])

    def marry(self):
        print("Girl A")

class Child:
    def property2(self):
        print(["Bike","Cash"])

    def marry(self):
        super().marry()
        print("Girl B")

c = Child()
c.marry() # Girl B

'''
variable overriding ---> 
'''
class Parent:
    language = "Java"

class Child:
    language = "Python"

c = Child()
print(c.language) # Python