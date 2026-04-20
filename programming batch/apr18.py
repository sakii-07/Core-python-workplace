'''
WAP to find the sum of all numbers from 1 to 10.
'''
num = int(input("Enter the number : "))
sum = 0 
for i in range(1,num+1):
    sum += i
print("sum of all numbers from 1 to 10 : ", sum)
'''
Enter the number : 10
sum of all numbers from 1 to 10 :  55
'''

'''
WAP to find the sum of all even numbers from 1 to 10.
'''
num = int(input("Enter the number : "))
sum = 0 
for i in range(1,num+1):
   if i%2 == 0:
        sum += i
print("sum of all even numbers from 1 to 10 : ", sum)
'''
Enter the number : 10
sum of all even numbers from 1 to 10 :  30
'''

'''
WAP to find the sum of all odd numbers from 1 to 10.
'''
num = int(input("Enter the number : "))
sum = 0 
for i in range(1,num+1):
   if i%2 != 0:
        sum += i
print("sum of all odd numbers from 1 to 10 : ", sum)
'''
Enter the number : 10
sum of all odd numbers from 1 to 10 :  25
'''

'''
WAP to callate the lenght of an iterable (like string or list) without using buildin fuctions
''' 
iterable = eval(input("Enter the iterable : "))
# l1 = [2,3,4,5,1,2,3,5,6,7,8,9,3,4]
lenght = 0
for num in iterable:
    lenght += 1

print("Lenght of iterable : ",lenght) # Lenght of iterable :  14

students = ["ishwar","rajesh","krishna",'om','ram',"pavan"]
std = {}
for name in students:
    count = 0
    for character in name:
        count += 1
    std[name]= count
print(std) # {'ishwar': 6, 'rajesh': 6, 'krishna': 7, 'om': 2, 'ram': 3, 'pavan': 5}

# Dictionary comprehention
std_db = {name:len(name) for name in students}
print(std_db)

# WAP to count uppercase char
name= 'pavAnKumAr'
count = 0
# way 1
for char in name:
    if char == char.upper():
        count += 1
print(count) # 3

# way 2
for char in name:
    if char.isupper():
        count += 1
print(count) # 3

students = ["iShwaR","RaJesH","kRiShNa",'OM','RaM',"Pavan"]
std = {}
for name in students:
    count = 0
    for char in name:
        if char.isupper():
            count += 1
    std[name] = count
print(std) # {'iShwaR': 2, 'RaJesH': 3, 'kRiShNa': 3, 'OM': 2, 'RaM': 2, 'pavan': 1}

# WAP to count how many vowels (a,e,i,o,u) are present in a given string
string = input("Enter the string : ")
count = 0
for char in string:
    if char.lower() in 'aeiou':
        count += 1
print(count) # Enter the string : sakshi     2

# WAP to count even number and odd number 
numbers = [10,20,30,11,21,45,33,78,14,27,89]
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Count of even numbers : ",even) # Count of even numbers :  5
print("Count of odd numbers : ",odd) # Count of odd numbers :  6


# WAP to find the frequency of each character in a tring (how many times each character occcurs)

name = input("Enter the string : ")

fre_count = {}
for char in name:
    if char not in fre_count:
        count = 1
        fre_count[char] = count
    else:
        fre_count[char] += 1
print(fre_count)

# WAP to reverse a strng using a loop (without using slicing)
string = input("Enter the String : ")
r_str = ""
for char in string:
    r_str = char + r_str
print(r_str)

students = ["ishwar","rajesh","krishna",'om','ram',"pavan"]
revs = {}
for name in students:
    rev = ''
    for char in name:
        rev = char + rev
    revs[name] = rev
print(revs) # {'ishwar': 'rawhsi', 'rajesh': 'hsejar', 'krishna': 'anhsirk', 'om': 'mo', 'ram': 'mar', 'pavan': 'navap'}

# WAP to check given string is palindrome or not.
string = input("Enter the string : ")
rev = ''
for char in string:
    rev = char + rev
if string == rev:
    print("Palindrome")
else:
    print("Not palindrome")

###        Functional Programming

# WAP to prnt number from given range
start = int(input("Enter the start number : "))
end = int(input("Enter the end number : "))

def numRange(start,end):
    for i in range(start,end+1):
        print(i,end=" ")

numRange(start,end) # 20 21 22 23 24 25 26 27 28 29 30 

# WAP to print sum of given range
def sum(start,end):
    sum = 0
    for num in range(start,end+1):
        sum += num
    print(sum)

sum(23,90) # 3842

# WAP to print sum of even numbers
def sumOfEvenNumber(start,end):
    sum = 0
    for num in range(start,end+1):
        if num%2 == 0:
            sum += num
    print("Sum of even numbers -: ",sum)
sumOfEvenNumber(23,78) # Sum of even numbers -:  1428

# WAP to print sum of odd numbers
def sumOfOddNumber(start,end):
    sum = 0
    for num in range(start,end+1):
        if num%2 != 0:
            sum += num
    print("Sum of odd numbers -: ",sum)
sumOfOddNumber(34,56) # Sum of odd numbers -:  495

# WAP to print sum of given range
def sumOfOddNumber(start,end):
    sum = 0
    if  start < end:
        for num in range(start,end+1):       
            sum += num
    else:
        for num in range(start,end-1,-1):       
            sum += num
    print("Sum -: ",sum)
sumOfOddNumber(56,34) # Sum -:  1035

# WAP to check whether a given number is prime or not

num = int(input("Enter the number : "))

def checkPrime(num):
    count = 0
    for i in range(2, num//2+1):
        if num%i == 0:
            count += 1
            break
    
    if count == 0:
        print("Prime")
    else:
        print("Not prime")

# checkPrime(num)

def printPrimeNum(number):

    for num in range(2,number+1):
        count = 0
        for i in range(2,num//2+1):
            if num%i == 0:
                count += 1
                break
                
        if count == 0:
            print(num,end=" ")

printPrimeNum(100)

#  way 2
def isprime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def printPrimeNum(number):
    prime_list = []
    for num in range(2,number+1):
        if isprime(num):
            prime_list.append(num)
    print(prime_list)
printPrimeNum(100)

# way 3
def printPrimeNum(number):
    prime_list = []
    for num in range(2,number+1):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            prime_list.append(num)
    
    return prime_list
primeNumber = printPrimeNum(10)
print(primeNumber)

# WAP check the given number is perfect or not
def isperfect(num):
    sum = 0
    for i in range(1,num):
        if num%i==0:
            sum += i

    if num == sum:
        return True
    else:
        return False
    
isperfect(7)