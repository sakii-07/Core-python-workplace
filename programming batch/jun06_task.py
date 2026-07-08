## Test management system 
students = {101:'sakshi',102:'shital',103:'amruta',104:'paranali'}

marks = {101:{'test1':78,'test2':46,'test3':90},
        102:{'test1':89,'test2':75,'test3':83},
        103:{'test1':67,'test2':39,'test3':82},
        104:{'test1':97,'test2':49,'test3':61}}

## TAsk -1 : Display all students
# for roll, name in students.items():
#     print("Roll No : ",roll," | ","Name : ",name)

## Task 2 : add marks for a test
# roll_no = int(input("Enter the roll number : "))
# testname = input("Enter the test name : ")
# mk = int(input("Enter the marks : "))

# mks = {}
# mks[testname] = mk
# marks[roll_no] = mks

## Display marks of particular student

# roll = int(input("Enter roll number : "))
# name = input("Student name : ")

# for t,m in marks[roll].items():
#     print(t,m)