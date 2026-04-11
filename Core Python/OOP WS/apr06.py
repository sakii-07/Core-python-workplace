'''
OOPs pillars----> there are four pillars in oop
            1) Inheritance
            2) Polimorphism
            3) Encapculation
            4) Abstraction

1) Inheritance -----> It is one of the pillar of oop.
                      Aquiring all properties of base class into derived/child class is called inheritance
                      Base class is also known as parent , super class
                      Derived class is also known as chlid class or subclass
                      we can save memory 
                      Less redundancy of code / less duplication of code
                      we can save time time to complete project
                      we can achieve method oveerriding by inheritance
                      There are few types of inheritacance
                                1) simple/single
                                2) multilevel
                                3) Hierachical
                                4) multiple
                                5) hybrid
                                6) cyclic

1) simple/single ----> One parent and one child kind of inheritance.

'''
class Parent:

    def m1(self):
        property = ["Cash","Gold","Farm","Car","House"]
        print(property)

class Child(Parent):

    def m2(self):
        prop = ["Cash","Bike"]
        print(prop)

saki = Child()
saki.m1()
saki.m2()
'''
['Cash', 'Gold', 'Farm', 'Car', 'House']
['Cash', 'Bike']
'''

s = Parent()
s.m1()
s.m2() # Parent class can not access child class properties
'''
['Cash', 'Gold', 'Farm', 'Car', 'House']

Traceback (most recent call last):
  File "e:\Github\Core-python-workplace\Core Python\OOP WS\apr6.py", line 49, in <module>
    s.m2()
    ^^^^
AttributeError: 'Parent' object has no attribute 'm2'. Did you mean: 'm1'?
'''

'''
2) Multilevel inheritance --->  Inheritance in levels is called multilevel
'''
class GrandParent:

    def m1(self):
        pro = ["Farm","Farm House"]
        print(pro)

class Parent(GrandParent):

    def m2(self):
        property = ["Cash","Gold","Farm","Car","House"]
        print(property)

class Child(Parent):

    def m3(self):
        prop = ["Cash","Bike"]
        print(prop)

saki = Child()
saki.m1()
saki.m2()
saki.m3()

print(Child.__mro__) # (<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.GrandParent'>, <class 'object'>)
'''
['Farm', 'Farm House']
['Cash', 'Gold', 'Farm', 'Car', 'House']
['Cash', 'Bike']
'''
'''
 3) Hierachical Inheritance ---> One parent and multiple childs kind of inheritance.
'''

class Parent:

    def m1(self):
        pro = ["Farm","Farm House"]
        print(pro)

class Child1(Parent):

    def m2(self):
        property = ["Cash","Gold","Farm","Car","House"]
        print(property)

class Child2(Parent):

    def m3(self):
        prop = ["Cash","Bike"]
        print(prop)

class Child3(Parent):

    def m4(self):
        prop = ["Cash","Bike","Gold","BMW"]
        print(prop)

jay = Child1()
jay.m1()
jay.m2()

viru = Child2()
viru.m1()
viru.m3()

gabbar = Child3()
gabbar.m1()
gabbar.m4()

'''
4) Multiple Inheritance ---> One child and multiple parents kind of inheritance.
'''
class Parent1:

    def m1(self):
        pro = ["Farm","Farm House"]
        print(pro)

class Parent2:

    def m2(self):
        property = ["Cash","Gold","Farm","Car","House"]
        print(property)

class Child(Parent2,Parent1):

    def m3(self):
        prop = ["Cash","Bike"]
        print(prop)

# If both parent have different methods then child access the all proprtes or method
jay = Child()
jay.m1()
jay.m2()

# if both parent have the same method then child access the first parent method
jay = Child()
jay.m1()

print(Child.__mro__) # (<class '__main__.Child'>, <class '__main__.Parent2'>, <class '__main__.Parent1'>, <class 'object'>)
print(Parent1.__mro__) # (<class '__main__.Parent1'>, <class 'object'>)
'''
Q. why object is parent of all class
In Python, `object` is the parent of all classes because it provides a common base that gives every 
class default methods and ensures consistency in how objects behave.
'''