'''
Types of variable in class :- 
                1) Instance 
                2) class/ static
                3) local

1) Instance variable :- These variables are written with self keyword.
                        seperate copy per object is created.

            example : class Student:
                        def __init__(self,r,n):
                            self.roll=r
                            self.name=n
                      s1 = Student(1,"sakshi")

                      roll and name are the instance variable

2) Class variable :- variable which is declared inside class and outside the constructor is called class variable
                     Also called as static variable.
                     singe copy is created and shared with all the objects.
                     It is used for memory saving purpose
                     Static/Class variable we can acess by object reference as well as class name.
                     Class name is always recommended

                      example : class Student:
                                    collage = "pune"
                                    def __init__(self,r,n):
                                        self.roll=r
                                        self.name=n
                                s1 = Student(1,"sakshi")

                      roll and name are the instance variables.
                      collage is the static/class variable.
                      r,n : hold the value for sometimes and pass to the instance variables-local variables.

3) local :- Local variables are the varaibles which are created to hold some data temporary
'''

class Student:

    collage = "TKA"

    def __init__(self,r,n):
        self.roll=r
        self.name=n

s1 = Student(1,"sakshi")
s2 = Student(2,"sojar")

print(s1.collage) # TKA
s1.collage = "pune"
print(s1.collage) # pune
print(s2.collage) # TKA
print(s1.roll) # 1
Student.collage = "pune"
print(Student.collage) # pune
print(s2.collage) # pune

'''
Method ----> Method is a function which is return inside a class
             we can pass parameters to mathod and can have return from method
             method is like a function,bunch of code, sub program which when invoked process data and return value
             there are three types method
                    1)Instance method
                    2)Class method
                    3)Static method

1)Instance method :- Instance method is a method which is used to process instance variable
                     First parameter of instance method is always self.
'''
class Student:

    collage = "TKA"

    def __init__(self,r,n):
        self.roll=r
        self.name=n

    def getRoll(self):
        return self.roll
    
    def setName(self,nn):
        self.name = nn

s1 = Student(1,"sakshi")
print(s1.name) # sakshi
r = s1.getRoll()
print(r) # 1
s1.setName("sojar")
print(s1.name) # sojar
s2 = Student(2,"sojar")

import this
# print(this)

'''
2) class method :- Class method is a method which is used to process class variables
                     First parameter of class method is always cls.
                     @classmethod decorator is used.
                     we can call class method by object ref as well as class name. class name is recommended.

3) local method :-   Local method is a method which is used to process local variables
                     @staticmethod decorator is used.
                     we can call class method by object ref. 
'''
