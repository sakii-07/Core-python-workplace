'''
self ----> self is a reference variable which is pointing to current object into memory.
            It is exact replacement of object creation 
            self is first parameter in a constructor and instance methods
            self is a name of a variable
            we can write any name of any variable instead of self
            we can access instance variabls and instance method by self keyword


 __new__ :- object created by the __new__ method before the calling init method and give heap memory

Internally PVM send s1 address(memory address) to the self(first argument of the init) automaticlly
'''

class Student:

    def __init__(self,r,n):
        print("Inside the class :",id(self))
        self.roll = r 
        self.name = n

s1 = Student(1,"sakshi")
print("From outside the class :",id(s1))
print("-----"*10)

s2 = Student(2,"sojar")
print("From outside the class :",id(s2))
print("-----"*10)

s3 = Student(1,"sakshi")
print("From outside the class :",id(s3))
print("-----"*10)

s4 = s1
print("From outside the class :",id(s4))
print("-----"*10)

s5 = Student()
print("From outside the class :",id(s5)) # It gives error like TypeError: Student.__init__() missing 2 required positional arguments: 'r' and 'n'
print("-----"*10)


# why follow standard coding practice - readable
'''
class name    ----------------->    Student, MyCar
Attributes    ----------------->    roll, roll_number
function name ----------------->    addition, addTwoNum()
'''

class Student:
    pass

s1 = Student()
print("id of s1 ",id(s1))
s2 = Student()
print("id of s2 ",id(s2))
'''
It always gives different id.
id of s1  2436813065584
id of s2  2436813081168
'''