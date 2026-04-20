'''
Build in modules ----> 1) math 
                       2) datetime
                       3) re
                       4) json (javascript object notation)
                       5) collection

1) math  -:  for mathematical operations on data we can use math module with python
             There are many inbuild functions in math module

Q. How to use math module?
import math                      
'''
import math
print("Enter the radius of circle : ")
radius = float(input())
area = math.pi + radius ** 2
print("The are of circle : ", area)

num = 25
print("The square root of 25 is ", math.sqrt(num))

num = 27
print("The cube root of 25 is ", math.cbrt(num))

res = math.factorial(5)
print("The factorial of 5 is ", res)

print("The log of 5 is ", math.log(5))

print("The sin of 90 is ", math.sin(90))

print("The 3 power 2 is ", math.pow(3,2))

'''
4
The are of circle :  19.141592653589793
The square root of 25 is  5.0
The cube root of 25 is  3.0
The cube factorial of 5 is  120
The cube log of 5 is  1.6094379124341003
The cube sin of 90 is  0.8939966636005579
'''

'''
2) datetime  -:  time stamp

methods ---> 1) today()  properties - 1) day 2) month 3) year
            
'''

from datetime import date 
today = date.today()
print("Todays date is : ",today)

day = today.day
print("The current day is : ",day)

month = today.month
print("The current day is : ",month)


yaer = today.year
print("The current day is : ",yaer)

dob = date(2004,6,1)
print(type(dob))
age = today.year - dob.year
print("Your age in years is : ",age)

from entity import Student
from datetime import date, datetime

t1 = datetime.now()
student_db = []
s1 = Student("sakshi",date(2004,6,1),"Pune",datetime.now())
s2 = Student("sojar",date(1980,6,1),"Sangola",datetime.now())
s3 = Student("pranjali",date(1992,6,1),"Solapur",datetime.now())

student_db.append(s1)
student_db.append(s2)
student_db.append(s3)

for student in student_db:
    if student.dob.year > 1990:
        print(student.name)

t2 = datetime.now()
print("Time required to complete : ", t2-t1)
'''
sakshi
pranjali
Time required to complete :  0:00:00.000705
'''