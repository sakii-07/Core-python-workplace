'''
oop ----> Rules and regulations

ex. python,java,cpp

Rules --> we can convert anything in world in code.

name           ------------------->      class

secifications/ ------------------->      attributes/variables
features

functions/     ------------------->      methods
opeartions

class - class is collection of attributes and methods.
        class is like a blue print to create object.
        class is logical entity.
        we don't need memory for exection.

Q. how to create class?
class Student:
    def init(inputs):
        pass
        
Object ---> instance of class
            it is physical entity
            memory is required

refernace variable ---> It is a variable which is pointing to object.
                        we can access attributes and methods of that object using ref var.
'''

# task 1 - user story             salary
# Stuent has age and location ------------------->   python code
class Student:
    pass
#    # method
#     def __init__(self,a,l):
#         self.age = a
#         self.loc = l

s1 = Student()
print(s1)
print(type(s1))
print(id(s1))
'''
<__main__.Student object at 0x000001982B778D70>
<class '__main__.Student'>
1753075912048

s1 datatype is Student 
Student is class
s1 is an object name of Student class
'''
