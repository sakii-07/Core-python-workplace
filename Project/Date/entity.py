from datetime import date
class Student:

    def __init__(self,name,dob,location,timestamp):
        self.name = name
        self.dob = dob
        self.location = location
        self.created_at_timestamp = timestamp

    def __str__(self):
        f"name = {self.name}, date of birth = {self.dob}, location = {self.location}, timestamp = {self.created_at_timestamp}"

if __name__ == "__main__":
    print("This is the student class")
    s2 = Student("divya",date(1992,8,20),"sohale")
    print(s2)