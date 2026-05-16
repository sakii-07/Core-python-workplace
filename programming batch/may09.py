# write a program to print 1 to 10 numbers
def numFrom_1To10():
    for i in range(1,11):
        print(i,end=" ")

# numFrom_1To10() # 1 2 3 4 5 6 7 8 9 10 

# write a program to count even numbers from give range
def countEvenInGivenRange(start,end):
    count = 0
    for i in range(start,end+1):
        if i%2 == 0:
            count += 1
    return count

start = int(input("Enter the start range : "))
end = int(input("Enter the last range : "))
count = countEvenInGivenRange(start,end)
print(count) # 11

'''
Enter the start range : 20
Enter the last range : 50
16
'''
start = int(input("Enter the start range : "))
end = int(input("Enter the last range : "))
count = 0
while(start <= end):
    if start%2==0:
        count += 1
    start += 1

print(count)

# Write a program to count numbers which is divisible by 4 and 7 of given range
def divisibleBy4And7(start,end):
    count = 0
    for num in range(start,end+1):
        if num%4==0 and num%7==0:
            count += 1
    return count
    
start = int(input("Enter the start range : "))
end = int(input("Enter the last range : "))

count = divisibleBy4And7(start,end)
print(count)
'''
Enter the start range : 1
Enter the last range : 1000
35
'''


start = int(input("Enter the start range : "))
end = int(input("Enter the last range : "))
count = 0
i = start
while(i <= end):
    if i%4==0 and i%7==0:
        count += 1
    i += 1

print(count)

# WAP to accept value from user and add into list
l = eval(input("Enter the list : "))

list_1 = []
i = 1

while i<=10:
    num = int(input("Enter the number : "))
    list_1.append(i)
    i += 1

# WAP to print value from list
print(list_1)

for val in l:
    print(val,end=" ")

i = 0
while i<len(list_1):
    print(list_1[i], end=" ")
    i += 1

# WAP to count number divisible by 5 in list
count = 0
for num in l:
    if num%5 == 0:
        count += 1

print("Count -: ",count)

# WAP to insert only odd numbers in list
l1 = eval(input("Enter the odd numbers list : "))
l2 = []

for num in l1:
    if num%2==1:
        l2.append(num)

print("Odd numbers list : ",l2)
'''
Enter the odd numbers list : [12,34,13,45,79,78,91,23]
Odd numbers list :  [13, 45, 79, 91, 23]
'''

# Way - 2
list_2 = []
lenght = int(input("Enter the lenght of list"))
num = int(input("Enter the number : "))
i = 1
while i<= lenght:
    if i%2==1:
        list_2.append(i)
        i += 1
print(list_2)

# WAP to print sum of 1 to 10 numbers
sum = 0
for i in range(1,10):
    sum += i
print(sum)

# WAP to print multiplication of numbers from given range
a = int(input("Enter the start range : "))
b = int(input("Enter the last range : "))
mul = 1
for i in range(a,b+1):
    mul *= i
print(mul)
'''
Enter the start range : 4
Enter the last range : 8
6720
'''

# WAP to check whether the no is prime or not
def isPrime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

num = int(input("Enter the number : "))
print(isPrime(num))
    
# WAP to count prime number from 1 to 100
a = int(input("Enter the start range "))
b = int(input("Enter the last range "))
count = 0
for i in range(a,b+1):
    if isPrime(i):
        count += 1
print(count)

# WAP to print divisor of given number
num = 25
for i in range(1,num+1):
    if num%i == 0:
        print(i,end=" ")

i = 1
while i<=28:
    if num%i == 0:
        print(i,end=" ")

# sum of divisor
num = 25
sum = 0
for i in range(1,num+1):
    if num%i == 0:
        sum += i
print(sum)

# perfect number
num = 28
sum = 0
for i in range(1,num):
    if num%i==0:
        sum += i

if num == sum:
    print("perfect number")
else:
    print("Not perfect number")

# perfect number betweebn 1 to 100
for num in range(1,101):
    sum = 0
    for i in range(1,num):
        if num%i==0:
            sum += i
    if num == sum:
        print(num, end=" ")

# WAP to print power of number 
num = int(input("Enter the number "))
power = int (input("Enter the power of number "))

res = num ** power
print(res)

# WAP to print each digit of number
n = 1345
n_str = str(n)
for i in n_str:
    print(int(i), end=" ")

# way - 2
# WAP to print each digit of number without using str
num = 1234
while num > 0:
    digit = num % 10
    print(digit, end=" ")
    num = num // 10

# WAP to count digt in number
a = 345
count = 0
while a > 0:
    digit = a%10
    count += 1
    a = a // 10
print(count)

# Write a program to print sum of digit of number
num = 1234
num_str = str(num)
sum = 0
for i in num_str:
    sum += int(i)
print(sum)

# way - 2
num = 123456
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print(sum)

# Armstrong number
num = 153
n = num
sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** 3
    num = num // 10
if sum == n:
    print("Armstrong number")
else:
    print("Not armstrong number")

# factorial of number
num = int(input("Enter the number "))
fact = 1
for i in range(1,num+1):
    fact *= i
print("Factoral : ",fact)

# WAP to print each factorial of digit of number
num = 5
while num > 0:
    n = num%10
    fact = 1
    for i in range(1,n+1):
        fact *= i
        print(fact, end=" ")
    num = num // 10

#WAP to print sum of factorial of digit of number
num = 67
sum = 0
while num > 0:
    n = num%10
    fact = 1
    for i in range(1,n+1):
        fact *= i
    sum += fact
    num = num // 10
print(sum)

# WAP to check wether the given number is palindrome or not
num = 121
n_str = str(num)
r_str = ""
for i in n_str:
    r_str = i + r_str
n = int(r_str)
if num == n:
    print("Palindrome")
else:
    print("Not palindrome")

# Strong number
num = 145
no = num
sum = 0
while num > 0:
    n = num%10
    fact = 1
    for i in range(1,n+1):
        fact *= i
    sum += fact
    num = num // 10
if no == sum:
    print("Strong number")
else:
    print("Not strong number")