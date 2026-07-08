# 1. Even odd checker
# write a program that takes a number as input and checks whether it is even or odd.
num = int(input("Enter the number : "))

if num%2==0:
    print("Even")
else:
    print("Odd")

# 2. positive,negative,zero
num = int(input("Enter the number : "))

if num > 0:
    print("Positive")
elif (num < 0):
    print("Negative")
else:
    print("Zero")

# 3. voting eligibility

age = int(input("Enter the age : "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligile to vote")

# 4. Maximum of two numbers
num1 = eval(input("Enter the fisrt number : "))
num2 = eval(input("Enter the second number : "))

if num1>num2:
    print(f'{num1} is greater number')
else:
    print(f'{num2} is greater number')

# 5. Miniimum of two numbers
# take two numbers from the user and find which one smaller
num1 = eval(input("Enter the fisrt number : "))
num2 = eval(input("Enter the second number : "))

if num1<num2:
    print(f'{num1} is minimum number')
else:
    print(f'{num2} is minimum number')


# write a program to check the number is divisible by 4 and 7
num = eval(input("Enter the number : "))

if num%4==0 and num%7==0:
    print(f'{num} is divisile by 4 and 7')
else:
    print(f'{num} is not divisile by 4 and 7')
'''
Enter the number : 28
28 is divisile by 4 and 7

Enter the number : 23
23 is not divisile by 4 and 7
'''

# accept the range user and count the number divisible by 4 and 7
start = int(input("Enter the start range : "))
end = int(input("Enter the last range : "))
count = 0
for i in range(start,end+1):

    if i%4==0 and i%7==0:
        count += 1

print("count of number divisible by 4 and 7 : ",count)
'''
Enter the start range : 1
Enter the last range : 100
count of number divisible by 4 and 7 :  3
'''

'''
accept the number from user
 if number is divisible by 3 - mango
 if number is divisible by 5 - apple
 if number is divisible by 3 and 5 - mango and apple
 autherwise print number
'''

num = int(input("Enter the number : "))

if num%3==0 and num%5==0:
    print("Mango and Apple")
elif num%3==0:
    print("Mango")
elif num%5==0:
    print("Apple")
else:
    print(num)

'''
Pass and fail
    ask the user for their marks. if marks are greater than or equal to 40 print pass , else print fail
'''
mark = eval(input("Enter the marks : "))

if mark >= 40:
    print("Pass")
else:
    print("Fail")

'''
Grade calculator
take marks as input and assign grades :
90 and above - A
75-89 -> B
60 - 74 -> C
40-59 -> D
belof 40 -> fail
'''
mark = eval(input("Enter the marks : "))

if mark >= 90:
    print("A")
elif mark >= 75 and mark < 90:
    print("B")
elif mark >= 60 and mark < 75:
    print("C")
elif mark >= 40 and mark < 60:
    print("D")
else:
    print("Fail")

'''
ATM wihdrawal
ask the user to enter the balance and withdrawal amount . if withdrawal amount <= balance,deduct 
it and print ramaining balance ,else print "Insufficient balance"
'''
bal = eval(input("Enter the balance : "))
wd = eval(input("Enter the Withdrawal amount : "))

if wd <= bal:
    bal = bal - wd
    print("Remaining balance : ",bal)
else:
    print("Insufficent balance")
'''
Enter the balance : 4000
Enter the Withdrawal amount : 2000
Remaining balance :  2000

Enter the balance : 500
Enter the Withdrawal amount : 600
Insufficent balance

Enter the balance : 500
Enter the Withdrawal amount : 500
Remaining balance :  0
'''

'''
Login system
store a username and password. Take input from user. if both match, print "login successfull",
else print "Invalid credintials"
'''
username = "sakshi"
password = "sakshi123"

user = input("Enter the Username : ")
p = input("Enter the Password : ")

if user == username and p == password:
    print("Login successfull")
else:
    print("Invalid creadintails")