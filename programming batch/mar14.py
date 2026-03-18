num = eval(input("Enter the list : "))
print(num)

print("Enen number : ")
for i in num:
    if i%2==0:
        print(i)

# find maximum number between four numbers
a,b,c,d = eval(input("Enter the four numbers : "))
max_num = a

if b>max_num:
    max_num=b
if c>max_num:
    max_num=c
if d>max_num:
    max_num=d
print(max_num)

# ATM withdrawal

balance = int(input("Enter the balance : "))
amount = int(input("Enter the withdrawal amount : "))

if amount <= balance:
    balance = balance - amount
    print("Remaining balance is : ", balance)
else:
    print("Insufficient balance")

# login system
username = "saki"
pass1 = "saki@12"
user = input("Enter the username : ")
pass2 = input("Enter the password : ")

if username == user and pass1 == pass2:
    print("Login successful")
else:
    print("Invalid credentials")

# find lenght of iterable without using build functions
l1 = [1,2,3,4,2,5,6,7,8,9]
lenght = 0

for i in l1:
    lenght += 1

print("Lenght of give string : ",lenght)

# reverse string
s = "sakshi"
ch = " "

for i in s:
    ch = i + ch 
print("reverse string is : ",ch)

# count of even and odd numbers in list
l1 = [1,2,3,4,2,5,6,7,8,9]
e_count = 0
o_count = 0

for i in l1:
    if i%2==0:
        e_count += 1
    else:
        o_count += 1
print("even count : ",e_count)
print("odd count : ",o_count)
	
# prime number between 1 to 1000
prime = []
for i in range(2,1001):
    count = 0
    for n in range(2,i//2 + 1):
        if i%n == 0:
            count += 1
            break
    if count == 0:
        prime.append(i)
print(prime)

# strong number

num = 145
s_num = str(num)
sum_num = 0
fact1 = []
for i in s_num:
    n = int(i)
    fact = 1
    for j in range(1,n+1):
        fact = fact*j

    fact1.append(fact)
    sum_num += fact
print(fact1)
if num == sum_num:
    print("strong number")
else:
    print("not strong number")

# perfect square
num = 64

for i in range(1,num+1):
    if i*i == num:
        print("perfect square")
        break
else:
    print("Not perfect square")

# perfect square between 1 to 100
sq = []
for i in range(1,101):
    for n in range(1,i+1):
        if n*n == i:
            sq.append(i)
            break
print(sq)

# palindrome
num = 121
s_num = str(num)
r_num = ""
for i in s_num:
    r_num = i+r_num
rev = int(r_num)
if num == rev:
    print("palindrome")
else:
    print("not palindrome")

# fabonaci series
num = 10
a=0
b=1
for i in range(1,num+1):
    print(a)
    c=a+b
    a,b=b,c

# remove duplicates from list
# way - 1
l1 = [1,2,3,4,5,6,3,4,5,6,5,6,7,8,4,9]
unique = []

for i in l1:
    if i not in unique:
        unique.append(i)
print(unique)

# way - 2
l1 = [1,2,3,4,5,6,3,4,5,6,5,6,7,8,4,9]
unique = list(set(l1))
print(unique)