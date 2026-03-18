# Create a function which accepts number from user and find given number is even or odd
def evenOrOdd(num):
    if num % 2 == 0:  # defines number is even
        print(num,"is a Even number")
    else:
        print(num,"is a Odd number")

num = int(input("Enter the number : "))
evenOrOdd(num)
'''
Enter the number : 12
12 is a Even number
'''

# Create a function which accepts number from user and find given number is prime or not ?
# prime number :  is a number greater than 1 that has only two factors - 1 and itself.
def prime(num):
    count = 0
    for i in range(2,num//2 +1):
        if num%i == 0:
            count += 1
            break
    if count == 0:
        print(num,"is a prime number")
    else:
        print(num,"is not prime number")

num = int(input("Enter the number : "))
prime(num)
'''
Enter the number : 5
5 is a prime number

Enter the number : 90
90 is not prime number
'''

# Create a function which accepts number from user and find given number is palindrome or not
# Palindrome : is a word, number, or sequence that reads the same forward and backward.
def palindrome(num):
    s_num = str(num)
    r_num = " "

    for i in s_num:
        r_num = i + r_num

    rev = int(r_num)
    if num == rev:
        print(num,"is a palindrome number")
    else:
        print(num,"is not palindrome number")
num = int(input("Enter the number : "))
palindrome(num)
'''
Enter the number : 121
121 is a palindrome number

Enter the number : 345
345 is not palindrome number
'''

# Create a function which accepts number from user and find given number is Armstrong or not
# Armstrong number : is a number that is equal to the sum of its digits raised to a power.
def armstrong(num):
    s_num = str(num)
    sum = 0

    for i in s_num:
        sum = sum + int(i) ** len(s_num)

    if num == sum:
        print(num,"is a armstrong number")
    else:
        print(num,"is not a armstrong number")

num = int(input("Enter the number : "))
armstrong(num)
'''
Enter the number : 345
345 is not a armstrong number

Enter the number : 153
153 is a armstrong number
'''

# Create a function which accepts number from user and find factorial of given number
# Factorial : is the product of all positive integers from 1 to a given number.
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print("factorial of give number : ",fact)
num = int(input("Enter the number : "))
factorial(num)
'''
Enter the number : 5
factorial of give number :  120

Enter the number : 10
factorial of give number :  3628800
'''

# Create a function which accepts number from user and find Fibonacci series of given number
# Fibonacci series : is a sequence where each number is the sum of the previous two numbers.
def fabonacci(num):
    a = 0
    b = 1
    for i in range(1,num+1):
        print(a,end=" ")
        c = a+b
        a,b = b,c
num = int(input("Enter the number : "))
fabonacci(num)
'''
Enter the number : 10
0 1 1 2 3 5 8 13 21 34

Enter the number : 15
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
'''

# Create a function which accepts number from user and find given number is perfect or not
# Perfect number : is a number that is equal to the sum of its proper divisors (excluding itself).
def perfect(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum += i
    if num == sum:
        print(num,"is a perfect number")
    else:
        print(num,"is not a perfect number")

num = int(input("Enter the number : "))
perfect(num)
'''
Enter the number : 6
6 is a perfect number

Enter the number : 10
10 is not a perfect number
'''

# Create a function which accepts number from user and find given number is strong or not
# Strong number : is a number whose sum of the factorials of its digits is equal to the number itself.
def strong(num):
    s_num = str(num)
    sum = 0
    for i in s_num:
        digit = int(i)
        fact = 1
        for j in range(1,digit+1):
            fact = fact * j
        sum += fact
    
    if num == sum:
        print(num,"is a strong number")
    else:
        print(num,"is not a strong number")

num = int(input("Enter the number : "))
strong(num)
'''
Enter the number : 23
23 is not a strong number

Enter the number : 145
145 is a strong number
'''

# Create a function which accepts number from user and find given number is perfect square or not ?
# Perfect square : is a number that is the product of an integer multiplied by itself.
def perfectSquare(num):
    for i in range(1,num+1):
        if i * i == num:
            print(num,"is a perfect square")
            break
    else:
        print(num,"is not a perfect square")
num = int(input("Enter the number : "))
perfectSquare(num)
'''
Enter the number : 10
10 is not a perfect square

Enter the number : 16
16 is a perfect square

Enter the number : 64
64 is a perfect square
'''

# Create a function which accepts number from user and find prime number between 1 to 100
def primeNumbers(num):
    for n in range(2,num+1):
        count = 0
        for i in range(2,n//2+1):
            if n%i== 0:
                count += 1
                break
        if count == 0:
            print(n,end=" ")
num = int(input("Enter the number : "))
primeNumbers(num)
'''
Enter the number : 100
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
'''

# Create a function which accepts number from user and find prime number between 1 to 100
def perfectSquares(num):
    for n in range(num+1):
        for i in range(1,n+1):
            if i*i==n:
                print(n,end=" ")
num = int(input("Enter the number : "))
perfectSquares(num)
'''
Enter the number : 200
1 4 9 16 25 36 49 64 81 100 121 144 169 196
'''

# Create a function which accepts two string from user and find given string is anagram or not
# Anagram : is a word or string formed by rearranging the letters of another word using all the same letters.
def anagram(str1,str2):
    if sorted(str1) == sorted(str2):
        print("Given string is angram string")
    else:
        print("Given string is not angram string")
str1 = input("Enter the first String : ")
str2 = input("Enter the second String : ")
anagram(str1,str2)
'''
Enter the first String : listen
Enter the second String : silent
Given string is angram string

Enter the first String : hello
Enter the second String : word
Given string is not angram string
'''

# Print a right-angled pattern of stars.

def ptr(row,col):
    for r in range(1,row):
        for c in range(1,r+1):
            print("*",end=" ")
        print()

row = int(input("Enter the number of rows : "))
col = int(input("Enter the number of coloums : "))
ptr(row,col)
'''
Enter the number of rows : 6
Enter the number of coloums : 6
*
* *
* * *
* * * *
* * * * *

Enter the number of rows : 9
Enter the number of coloums : 9
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
'''

# Write a program to print a right-aligned right-angled triangle pattern using stars
def ptr(row,col):
    n =row-1
    for r in range(1,row):
        print(" "*(n-r),"*"*r,end=" ")
        print()

row = int(input("Enter the number of rows : "))
col = int(input("Enter the number of coloums : "))
ptr(row,col)
'''
Enter the number of rows : 8
Enter the number of coloums : 8
       *
      **
     ***
    ****
   *****
  ******
 *******
'''