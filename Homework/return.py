# Create a function which accepts number from user and find given number is even or odd
def evenOrOdd(num):
    if num % 2 == 0:  
        return "Even number"
    else:
        return "odd number"

num = int(input("Enter the number : "))
res = evenOrOdd(num)
print(num,"-->",res)
'''
Enter the number : 23
23 --> odd number
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
        return "Prime number"
    else:
        return "Not prime number"

num = int(input("Enter the number : "))
res = prime(num)
print(num,"-->",res)
'''
Enter the number : 29
29 --> Prime number

Enter the number : 30
30 --> Not prime number
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
        return True
    else:
        return False
    
num = int(input("Enter the number : "))
res = palindrome(num)
if res == True:
    print(num,"--> Palindrome")
else:
    print(num,"--> Not Palindrome")
'''
Enter the number : 121
121 --> Palindrome

Enter the number : 321
321 --> Not Palindrome
'''

# Create a function which accepts number from user and find given number is Armstrong or not
# Armstrong number : is a number that is equal to the sum of its digits raised to a power.
def armstrong(num):
    s_num = str(num)
    sum = 0

    for i in s_num:
        sum = sum + int(i) ** len(s_num)

    if num == sum:
        return "armstrong number"
    else:
        return "Not armstrong number"

num = int(input("Enter the number : "))
res = armstrong(num)
print(num,"-->",res)
'''
Enter the number : 345
345 --> Not armstrong number

Enter the number : 153
153 --> armstrong number
'''

# Create a function which accepts number from user and find factorial of given number
# Factorial : is the product of all positive integers from 1 to a given number.
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact
num = int(input("Enter the number : "))
res = factorial(num)
print(num,"--> factorial -->",res)
'''
Enter the number : 5
5 --> factorial --> 120

Enter the number : 10
10 --> factorial --> 3628800
'''

# Create a function which accepts number from user and find given number is perfect or not
# Perfect number : is a number that is equal to the sum of its proper divisors (excluding itself).
def perfect(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum += i
    if num == sum:
        return "Perfect number"
    else:
        return "Not perfect number"

num = int(input("Enter the number : "))
res = perfect(num)
print(num,"-->",res)
'''
Enter the number : 6
6 --> Perfect number

Enter the number : 10
10 --> Not perfect number
'''

# Create a function which accepts number from user and find given number is strong or not
# Strong number : is a number whose sum of the factorials of its digits is equal to the number itself.
def strongNum(num):
    s_num = str(num)
    sum = 0
    for i in s_num:
        digit = int(i)
        fact = 1
        for j in range(1,digit+1):
            fact = fact * j
        sum += fact
    
    if num == sum:
        return "Strong number"
    else:
        return "Not strong number"

num = int(input("Enter the number : "))
res = strongNum(num)
print(num,"-->",res)
'''
Enter the number : 345
345 --> Not strong number

Enter the number : 145
145 --> Strong number
'''

# Create a function which accepts number from user and find given number is perfect square or not ?
# Perfect square : is a number that is the product of an integer multiplied by itself.
def perfectSquare(num):
    for i in range(1,num+1):
        if i * i == num:
            return "Perfect square"
            break
    else:
        return "Not perfect square"
num = int(input("Enter the number : "))
res = perfectSquare(num)
print(num,"-->",res)
'''
Enter the number : 10
10 --> Not perfect square

Enter the number : 16
16 --> Perfect square

Enter the number : 64
64 --> Perfect square
'''

# Create a function which accepts two string from user and find given string is anagram or not
# Anagram : is a word or string formed by rearranging the letters of another word using all the same letters.
def anagram(str1,str2):
    if sorted(str1) == sorted(str2):
       return "angram string"
    else:
         return "Not angram string"
str1 = input("Enter the first String : ")
str2 = input("Enter the second String : ")
res = anagram(str1,str2)
print(str1,"and",str2,"-->",res)
'''
Enter the first String : silent
Enter the second String : listen
silent and listen --> angram string

Enter the first String : hello
Enter the second String : world
hello and world --> Not angram string
'''
