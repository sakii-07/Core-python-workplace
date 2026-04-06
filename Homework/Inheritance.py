# '''
# Hybrid Inheritance → Combination of two or more types of inheritance

# '''
# class GrandParent:
    
#     def m1(self):
#         property = ["farm","Car","House","Gold"]
#         print("Grandparent property - ",property)

# class Parent1 (GrandParent):
    
#     def m2(self):
#         property = ["Flat","Thar","House","Cash"]
#         print("Parent1 property - ",property)

# class Parent2 (GrandParent):
    
#     def m3(self):
#         property = ["Land","BMW","Bussiness","Bank Balance"]
#         print("Parent2 property - ",property)

# class Parent3 (GrandParent):
    
#     def m4(self):
#         property = ["Shop","Mobile"]
#         print("Parent3 property - ",property)

# class Child1 (Parent1):
    
#     def m5(self):
#         property = ["Laptop","Mobile","Bike"]
#         print("Child1  property - ",property)

# class Child2 (Parent2, Parent3):
    
#     def m6(self):
#         property = ["Iphone","Gold Chain","Cash"]
#         print("Child2 property - ",property)

# class SubChlid (Child1):
    
#     def m7(self):
#         property = ["Watch","Books","Bikecycle"]
#         print("Subchlid property - ",property)


# print("---- Grandparent Object ----")
# gp = GrandParent()
# gp.m1() # Calling GrandParent class method
# print(GrandParent.__mro__)
# '''
# ---- Grandparent Object ----
# Grandparent property -  ['farm', 'Car', 'House', 'Gold']
# (<class '__main__.GrandParent'>, <class 'object'>)
# '''

# print("---- Parent1 Object ----")
# p1 = Parent1()
# p1.m1() # Calling GrandParent class method
# p1.m2() # Calling Parent1 class method
# print(Parent1.__mro__)
# '''
# ---- Parent1 Object ----
# Grandparent property -  ['farm', 'Car', 'House', 'Gold']
# Parent1 property -  ['Flat', 'Thar', 'House', 'Cash']
# (<class '__main__.Parent1'>, <class '__main__.GrandParent'>, <class 'object'>)
# '''

# print("---- Parent2 Object ----")
# p2 = Parent2()
# p2.m1() # Calling GrandParent class method
# p2.m3() # Calling Parent2 class method
# print(Parent2.__mro__)
# '''
# ---- Parent2 Object ----
# Grandparent property -  ['farm', 'Car', 'House', 'Gold']
# Parent2 property -  ['Land', 'BMW', 'Bussiness', 'Bank Balance']
# (<class '__main__.Parent2'>, <class '__main__.GrandParent'>, <class 'object'>)
# '''

# print("---- Parent3 Object ----")
# p3 = Parent3()
# p3.m1() # Calling GrandParent class method
# p3.m4() # Calling Parent3 class method
# print(Parent3.__mro__)
# '''
# ---- Parent3 Object ----
# Grandparent property -  ['farm', 'Car', 'House', 'Gold']
# Parent3 property -  ['Shop', 'Mobile']
# (<class '__main__.Parent3'>, <class '__main__.GrandParent'>, <class 'object'>)
# '''

# print("---- Chlid1 Object ----")
# c1 = Child1()
# c1.m1() # Calling GrandParent class method
# c1.m2() # Calling Parent1 class method
# c1.m5() # Calling Child1 class method
# print(Child1.__mro__)
# '''
# ---- Chlid1 Object ----
# Grandparent property -  ['farm', 'Car', 'House', 'Gold']
# Parent1 property -  ['Flat', 'Thar', 'House', 'Cash']
# Child1  property -  ['Laptop', 'Mobile', 'Bike']
# (<class '__main__.Child1'>, <class '__main__.Parent1'>, <class '__main__.GrandParent'>, <class 'object'>)
# '''

# print("---- Child2 Object ----")
# c2 = Child2()
# c2.m1() # Calling GrandParent class method
# c2.m3() # Calling Parent2 class method
# c2.m4() # Calling Parent3 class method
# c2.m6() # Calling Child2 class method
# print(Child2.__mro__)
# '''
# ---- Child2 Object ----
# Grandparent property -  ['farm', 'Car', 'House', 'Gold']
# Parent2 property -  ['Land', 'BMW', 'Bussiness', 'Bank Balance']
# Parent3 property -  ['Shop', 'Mobile']
# Child2 property -  ['Iphone', 'Gold Chain', 'Cash']
# (<class '__main__.Child2'>, <class '__main__.Parent2'>, <class '__main__.Parent3'>, <class '__main__.GrandParent'>, <class 'object'>)
# '''

# print("---- SubChild Object ----")
# cb = SubChlid()
# cb.m1() # Calling GrandParent class method
# cb.m2() # Calling Parent1 class method
# cb.m5() # Calling Child1 class method
# cb.m7() # Calling SubChild class method
# print(SubChlid.__mro__)
# '''
# ---- SubChild Object ----
# Grandparent property -  ['farm', 'Car', 'House', 'Gold']
# Parent1 property -  ['Flat', 'Thar', 'House', 'Cash']
# Child1  property -  ['Laptop', 'Mobile', 'Bike']
# Subchlid property -  ['Watch', 'Books', 'Bikecycle']
# (<class '__main__.SubChlid'>, <class '__main__.Child1'>, <class '__main__.Parent1'>, <class '__main__.GrandParent'>, <class 'object'>)
# '''

# '''
# Multiple Inheritance ----> A class inherits from two or more parent classes.
# '''

class GrandParent1:

    def m6(self):
        property = ["Land","House","Gold","Cash"]
        print("GrandParent1 property - ",property)

class GrandParent2:
    
    def m1(self):
        property = ["Farm","Flat","Mobile"]
        print("GrandParent2 property - ",property)

class Parent1(GrandParent1, GrandParent2):
    
    def m5(self):
        property = ["Flat","Iphone","BMW","Money"]
        print("Parent1 property - ",property)

class Parent2:
    
    def m1(self):
        property = ["House","Thar","Gold","Laptop"]
        print("Parent2 property - ",property)

class Child(Parent1, Parent2):
    
    def m3(self):
        property = ["Iphone","Laptop","Bike","Cash"]
        print("Child property - ",property)

c = Child()
c.m1() # It calls Grandparent2 method
print("MRO of Chlid class - ")
print("\t",Child.__mro__)
'''
GrandParent2 property -  ['Farm', 'Flat', 'Mobile']
MRO of Chlid class - 
         (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.GrandParent1'>,
         <class '__main__.GrandParent2'>, <class '__main__.Parent2'>, <class 'object'>)
'''