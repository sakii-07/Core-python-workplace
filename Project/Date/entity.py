class Student:

    def __init__(self,name,dob,location):
        self.name = name
        self.dob = dob
        self.location = location

    def __str__(self):
        f"name = {self.name}, date of birth = {self.dob}, location = {self.location}"