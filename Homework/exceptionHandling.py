'''create Poratal for pune RTO.Accept age from user for liencence
create two custom Exception
1. AgeToolLowError  --> age<18
2. AgeToolHighError --> age > 75'''

class AgeToolLowError(Exception):
    def __init__(self, message):
        self.message = message

class AgeToolHighError(Exception):
    def __init__(self, message):
        self.message = message

try:
    age = int(input("Enter the age : "))
    if age < 18:
        raise AgeToolLowError("Age must be grater than 18")
    elif age > 75:
        raise AgeToolHighError("Age must be less than 18")
    else:
        print("Welcome to RTO portal pune")

except ValueError:
    print("Please enter the valid age (must be in number)")

except AgeToolLowError as a:
    print("Error : ", a.message)

except AgeToolHighError as a:
    print("Error : ", a.message)

finally:
    print("Thank you..!")
    