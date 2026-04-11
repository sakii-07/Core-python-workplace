'''
Abstraction ----> It is one of the pillar of OOP.
                  Showing required information to user and hiding implementation/compllexity of code is called abstraction.
                  Used for data hiding/security.
                  we can achieve abstraction by two ways :
                            1) Abstract class
                            2) Interface
non abstract method --> method with code/implementationmp
1) Abstract class ---> Abstract class is a class with abstract method as well as non abstract method

Q. what is abstract method?
-> Method without code/body/implementation is called abstract method

Q. How to create abstract class and abtract method in python
->By using ABC class and @abstractmethod decorator

'''
from abc import ABC, abstractmethod
class Demo(ABC):
    # non abstract method / concrete method
    def m1(self):
        print(111)

    @abstractmethod
    def m2(self,a,b):
        pass

class Example(Demo):
    def m2(self,a,b):
        print(a,b)

e = Example()
e.m1() # 111
e.m2(10,20) # 10 20

'''
2) Interface ---> Interface is an abstract class with all abstract method in  it.


I to C design pattern --> 
        I --> Interface
        C --> Class

'''
