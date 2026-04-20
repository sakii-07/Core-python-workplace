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