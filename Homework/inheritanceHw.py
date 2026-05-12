										##  Practices Question on Inheritance  ##

'''1. 	Create a class Person with variables: name, age, gender, address.
 	Create a constructor and methods to display the data.
 	Inherit it in a class Student with additional variables: rollNo, branch, percentage.
 	Add appropriate methods to Student to display all details.'''
class Person:
    def __init__(self,n,a,g,ad):
        self.name = n 
        self.age = a 
        self.gender = g 
        self.address = ad
    
    def display_person(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Gender : ",self.gender)
        print("Address : ",self.address)

class Student(Person):
    def __init__(self, r, b, p):
        self.rollNo = r
        self.branch = b
        self.percentage = p

    def display(self):
        p = Person("Sakshi",21,'F',"Sohale")
        p.display_person()
        print("Roll no : ",self.rollNo)
        print("Branch : ", self.branch)
        print("Percentage : ",self.percentage)
s = Student(10,"CSE",90)
s.display()
'''
Name :  Sakshi
Age :  21
Gender :  F
Address :  Sohale
Roll no :  10
Branch :  CSE
Percentage :  90
'''

'''2.     Create a class Vehicle with variables: brand, model, color, price.
 	Create a constructor and display method.
	Create a subclass Car which adds: fuelType, transmission.
 	Create another subclass ElectricCar which adds: batteryCapacity, chargingTime.
 	Call constructors and methods at each level to print complete car info.'''
class Vehicle:
    def __init__(self,b,m,c,p):
        self.brand = b
        self.model = m
        self.color = c
        self.price = p

    def display_vehicle(self):
        print("Brand name : ",self.brand)
        print("Model : ",self.model)
        print("Color : ",self.color)
        print("Price : ",self.price)
    
class Car(Vehicle):
    def __init__(self,f,t):
        self.fuelType = f 
        self.transmission = t

    def display_car(self):
        v = Vehicle("Toyota","Fortuner","Black",150000000)
        v.display_vehicle()
        print("Fual type : ",self.fuelType)
        print("Transmission : ",self.transmission)

c = Car("Petrol",'Manual')
# print("Car information : ")
# c.display_car()

class ElectricCar(Vehicle):
    def __init__(self,b,c):
        self.batteryCapacity = b
        self.chargingTime = c

    def display(self):
        v = Vehicle("Tesla","Model 3","White",150000000)
        v.display_vehicle()
        print('battery Capacity : ',self.batteryCapacity)
        print('charging Time : ',self.chargingTime)

e = ElectricCar("75 kWh","6 Hours")
print("Eletric car information ")
e.display()

'''3.   Create a base class Animal with variables: name, type, age, color.
      Add a constructor and methods to show info and makeSound().
      Create Dog and Cat classes that inherit Animal.
      Override makeSound() method in both child classes with specific messages.'''
class Animal:
    def __init__(self,n,t,a,c):
        self.name = n
        self.type = t
        self.age = a
        self.color = c

    def show_info(self):
        print("Name :", self.name)
        print("Type :", self.type)
        print("Age :", self.age)
        print("Color :", self.color)

    def makeSound(self):
        print("Animal makes sound")

class Dog(Animal):
    def makeSound(self):
        print("Dog barks: Woof Woof")

class Cat(Animal):
    def makeSound(self):
        print("Cat meows: Meow Meow")

d = Dog("Tommy", "Pet", 3, "Brown")
print("Dog Information :- ")
d.show_info()
d.makeSound()

print('----'*15)

c1 = Cat("Kitty", "Pet", 2, "White")
print("Cat Information :-")
c1.show_info()
c1.makeSound()
'''
Dog Information :- 
Name : Tommy
Type : Pet
Age : 3
Color : Brown
Dog barks: Woof Woof
------------------------------------------------------------
Cat Information :-
Name : Kitty
Type : Pet
Age : 2
Color : White
Cat meows: Meow Meow
'''

'''4. 	Create base class Appliance with brand, power_rating, weight, color, warranty.
	Child WashingMachine adds capacity, type (front/top load).
	Child SmartWashingMachine adds WiFi_enabled, voice_controlled.
	Each class should have display methods and constructors.'''
class Appliance:
    def __init__(self,b,p,w,c,wr):
        self.brand = b
        self.power_rating = p
        self.weight = w
        self.color = c
        self.warranty = wr

    def display(self):
        print("Brand : ",self.brand)
        print("power_rating : ",self.power_rating)
        print("weight : ",self.weight)
        print("color : ",self.color)
        print("warranty : ",self.warranty)

class WashingMachine(Appliance):
    def __init__(self, b, p, w, c, wr,cp,t):
        super().__init__(b, p, w, c, wr)
        self.capacity = cp
        self.type = t

    def display(self):
       super().display()
       print("capacity : ",self.capacity)
       print("type : ",self.type)
    
class SmartWashingMachine(WashingMachine):
    def __init__(self, b, p, w, c, wr, cp, t,we,v):
        super().__init__(b, p, w, c, wr, cp, t)
        self.WiFi_enabled = we
        self.voice_controlled = v

    def display(self):
        super().display()
        print("WiFi_enabled : ",self.WiFi_enabled)
        print("voice_controlled : ",self.voice_controlled)

obj = SmartWashingMachine(
    "LG",        # brand
    "2000W",     # power rating
    "65kg",      # weight
    "Silver",    # color
    "5 Years",   # warranty
    "8kg",       # capacity
    "Fully Automatic",  # type
    True,        # WiFi enabled
    True         # voice controlled
)

obj.display()

'''
Brand :  LG
power_rating :  2000W
weight :  65kg
color :  Silver
warranty :  5 Years
capacity :  8kg
type :  Fully Automatic
WiFi_enabled :  True
voice_controlled :  True
'''

'''5.Class Employee has emp_id, name, department, salary, contact.
	Class Manager adds team_size, project_name.
	Class Developer adds skills, experience_years.
	Use methods like show_details(), update_salary(amount), and print_role().'''
class Employee:
    def __init__(self,e,n,d,s,c):
        self.emp_id = e
        self.name = n
        self.department = d
        self.salary = s
        self.contact = c

    def showDetails(self):
        print("emp_id : ",self.emp_id)
        print("name : ",self.name)
        print("department : ",self.department)
        print("salary : ",self.salary)
        print("contact : ",self.contact)

    def update_salary(self,amount):
        self.salary +=  amount
        print("Updated Salary : ",self.salary)

    def print_role(self):
        print("Role : Employee")

class Manager(Employee):
    def __init__(self, e, n, d, s, c,t,p):
        super().__init__(e, n, d, s, c)
        self.team_size = t
        self.project_name = p

    def showDetails(self):
        super().showDetails()
        print("team_size : ",self.team_size)
        print("project_name : ",self.project_name)

    def print_role(self):
        print("Role : Manager")

class Developer(Employee):
    def __init__(self, e, n, d, s, c,sk,ey):
        super().__init__(e, n, d, s, c)
        self.skills = sk
        self.experience_years = ey

    def showDetails(self):
        super().showDetails()
        print("skills : ",self.skills)
        print("experience_years : ",self.experience_years)

    def print_role(self):
        print("Role : Develper")

m = Manager(101,"Sakshi","CSE",50000,'1234567890',10,"Ecommerce Website")
m.showDetails()
m.print_role()

m.update_salary(15000)

'''
emp_id :  101
name :  Sakshi
department :  CSE
salary :  50000
contact :  1234567890
team_size :  10
project_name :  Ecommerce Website
Role : Manager
Updated Salary :  65000
'''    