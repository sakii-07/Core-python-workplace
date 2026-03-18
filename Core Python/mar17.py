def gmil_logic(username,password):
    print("Username", username)
    print("Password",password)

    if(username == "ABC" and password == "1234"):
        print("login successful")
    else:
        print("failed to login")

username = input("Enter the username : ")
password = input("Enter the password : ")
gmil_logic(username,password)

# Create a function which accepts number from user and prints its cube

def cube():
    num = int(input("Enter the number : "))
    cube = num ** 3
    print("cube of number is : ", cube)

cube()

# Create a function which accepts list from user and dislay square each element of this list

def square(l1):
    print("list is : ", l1)

    for i in l1:
        print(i*i)
l1 = eval(input("Enter the list of numbers : "))
square(l1)

# Reverse given number using functional program
def rev(num):
    s_num = str(num)
    r_num = " "

    for i in s_num:
        r_num = i + r_num

    rev = int(r_num)
    print("Reverse number : ",rev)

num = int(input("Enter the number : "))
rev(num)