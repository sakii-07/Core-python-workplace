'''
Hybrid Inheritance → Combination of two or more types of inheritance

'''
class GrandParent:
    
    def m1(self):
        property = ["farm","Car","House","Gold"]
        print("Grandparent property - ",property)

class Parent1 (GrandParent):
    
    def m2(self):
        property = ["Flat","Thar","House","Cash"]
        print("Parent1 property - ",property)

class Parent2 (GrandParent):
    
    def m3(self):
        property = ["Land","BMW","Bussiness","Bank Balance"]
        print("Parent2 property - ",property)

class Parent3 (GrandParent):
    
    def m4(self):
        property = ["Shop","Mobile"]
        print("Parent3 property - ",property)

class Child1 (Parent1):
    
    def m5(self):
        property = ["Laptop","Mobile","Bike"]
        print("Child1  property - ",property)

class Child2 (Parent2, Parent3):
    
    def m6(self):
        property = ["Iphone","Gold Chain","Cash"]
        print("Child2 property - ",property)

class SubChlid (Child1):
    
    def m7(self):
        property = ["Watch","Books","Bikecycle"]
        print("Subchlid property - ",property)


print("---- Grandparent Object ----")
gp = GrandParent()
gp.m1() # Calling GrandParent class method
'''
---- Grandparent Object ----
Grandparent property -  ['farm', 'Car', 'House', 'Gold']
'''

print("---- Parent1 Object ----")
p1 = Parent1()
p1.m1() # Calling GrandParent class method
p1.m2() # Calling Parent1 class method
'''
---- Parent1 Object ----
Grandparent property -  ['farm', 'Car', 'House', 'Gold']
Parent1 property -  ['Flat', 'Thar', 'House', 'Cash']
'''

print("---- Parent2 Object ----")
p2 = Parent2()
p2.m1() # Calling GrandParent class method
p2.m3() # Calling Parent2 class method
'''
---- Parent2 Object ----
Grandparent property -  ['farm', 'Car', 'House', 'Gold']
Parent2 property -  ['Land', 'BMW', 'Bussiness', 'Bank Balance']
'''

print("---- Parent3 Object ----")
p3 = Parent3()
p3.m1() # Calling GrandParent class method
p3.m4() # Calling Parent3 class method
'''
---- Parent3 Object ----
Grandparent property -  ['farm', 'Car', 'House', 'Gold']
Parent3 property -  ['Shop', 'Mobile']
'''

print("---- Chlid1 Object ----")
c1 = Child1()
c1.m1() # Calling GrandParent class method
c1.m2() # Calling Parent1 class method
c1.m5() # Calling Child1 class method
'''
---- Chlid1 Object ----
Grandparent property -  ['farm', 'Car', 'House', 'Gold']
Parent1 property -  ['Flat', 'Thar', 'House', 'Cash']
Child1  property -  ['Laptop', 'Mobile', 'Bike']
'''

print("---- Child2 Object ----")
c2 = Child2()
c2.m1() # Calling GrandParent class method
c2.m3() # Calling Parent2 class method
c2.m4() # Calling Parent3 class method
c2.m6() # Calling Child2 class method
'''
---- Child2 Object ----
Grandparent property -  ['farm', 'Car', 'House', 'Gold']
Parent2 property -  ['Land', 'BMW', 'Bussiness', 'Bank Balance']
Parent3 property -  ['Shop', 'Mobile']
Child2 property -  ['Iphone', 'Gold Chain', 'Cash']
'''

print("---- SubChild Object ----")
cb = SubChlid()
cb.m1() # Calling GrandParent class method
cb.m2() # Calling Parent1 class method
cb.m5() # Calling Child1 class method
cb.m7() # Calling SubChild class method
'''
---- SubChild Object ----
Grandparent property -  ['farm', 'Car', 'House', 'Gold']
Parent1 property -  ['Flat', 'Thar', 'House', 'Cash']
Child1  property -  ['Laptop', 'Mobile', 'Bike']
Subchlid property -  ['Watch', 'Books', 'Bikecycle']
'''