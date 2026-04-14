'''
Exception handling ---> Exception is unwanted event  / erroe which occures at the time of execution of code
                        Runtime errors
                        Due to exeception our program gets abnormally terminted(AT)
                        Normal Termination of code required. (NTO)

Q. What is exception handling?
-> providing alternative path to the rest of code so we have NT.
   we can handle exception in python by using following keyword
            1) try
            2) except
            3) else
            4) finally
            5) raise

1) try block ----> write your riskey code here
                   his block execute always

2) except block ----> If there is exception in try block then this block will execute
                      write your alternative logic here

3) else block ---> If there is no exception thenn this block will execute.

4) finally block ---> clean up activity
                      This block executes always
'''
print("Start of code")
try:
    num1 = int(input("Enter the number : "))
    print(num1)

    if num1==0:
        obj = ZeroDivisionError("Canno divide by zero")
        raise obj
    
    print(78/num1)

except ValueError:
    print("Please enter the valid naumber")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:  # always use in exceptional cases
    print("An error occured : ",e)

else:
    print("No error occured")

finally:
    print("End of the code")

'''
Custom Exception ---> 
'''

class StudentNotFount(Exception):
    def __init__(self, message):
        self.message = message

print("Start of code")
name = "sakshi"
try:
    if name == "sakshi":
        raise StudentNotFount("Student not found on database")

except StudentNotFount as s:
    print("Error : ", s.message)
    
print("End of the code")


class HumPadhaiNaiKarte(Exception):
    def __init__(self, message):
        self.message = message


print("Start of code")
marks = 38
try:
    if marks < 40:
        raise HumPadhaiNaiKarte("Marks are less than 40. Please study harder !")
    else:
        print("Congratulation! You passed the exam.")

except HumPadhaiNaiKarte as e:
    print("Error : ", e.message)
    
print("End of the code")