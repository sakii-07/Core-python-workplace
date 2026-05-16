# Task - 1
class Person:

    def __init__(self,n,a):
        self.name = n
        self.address = a

class Student:

    def __init__(self,r,m):
        self.rollNo = r
        self.marks = m

class Scollership():

    p = Person("Sakshi","sohale") 
    s = Student(1,85)

    if(s.marks > 80):
        print("Eligible for scollership")
    else:
        print("Not eligible for scollership")

# Task - 2
from abc import ABC, abstractmethod
class JBK(ABC):

    def show(self):
        print("Hii, good evening..")

    @abstractmethod
    def addition(self,a,b):
        pass

class Example(JBK):

    def addition(self, a, b):
        return a+b

e = Example()
add = e.addition(10,20)
# print(add)

# e.show()
