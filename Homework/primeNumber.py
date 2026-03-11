# WAP to check given number is prime or not ?

# prime number way - 1
num = 190
count = 0

for i in range(1,num+1):
    if num % i == 0:
        count += 1

if count == 2:
    print(num,"is a prime number")
else:
    print(num,"is not prime number") # 190 is not prime number

# prime number way - 2
num = 29
count = 0

for i in range(2,num):
    if num % i == 0:
        count += 1

if count == 0:
    print(num,"is a prime number") # 29 is a prime number
else :
    print(num,"is a not prime number")

# prime number way - 3
num = 67
count = 0

for i in range(2,num // 2 +1):
    if num % i == 0:
        count += 1

if count == 0:
    print(num,"is a prime number") # 67 is a prime number
else :
    print(num,"is a not prime number")

# prime number way - 4
num = 98
count = 0

for i in range(2,num//2 + 1):
    if num % i == 0:
        count += 1
        break         

if count == 0:
    print(num,"is a prime number")
else :
    print(num,"is not a prime number") # 98 is not a prime number


# find prime number between 1 to 20

# way - 1
for num in range(1,20):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num)

# way - 2
for num in range(2,21):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count == 0:
        print(num)

# way - 3
for num in range(2,21):
    count = 0
    for i in range(2,num//2 +1):
        if num % i == 0:
            count += 1
    if count == 0:
        print(num)
'''
2
3
5
7
11
13
17
19
'''

# way - 4
for num in range(10,31):
    count = 0
    for i in range(2,num//2 + 1):
        if num % i == 0:
            count += 1
            break
    if count == 0:
        print(num)
'''
11
13
17
19
23
29
'''

# fabonnaci series
n = 10

a = 0
b = 1
for i in range(n):
    print(a)
    c = a+b
    a,b = b,c