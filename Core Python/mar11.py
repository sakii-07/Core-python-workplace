'''
DRY - donot repeat yourself (py )
loop - to repetative task
2) Iterative statement
                  1) for loop - Entry control loop - If we know number of iteration in advance
                    syntax - for varname in sequence :
                                 body of for loop
    Note - py internally finds the lenght of sequence

                  2) while loop - If we don't know number of iteration in advance
'''

# WAP to print 1 to 5 on console using for loop
for i in range(1,6):
    print(i) # 1 2 3 4 5

for i in range(101,106):
    print(i-100)

for i in [1,2,3,4,5]:
    print(i)

for i in (1,2,3,4,5):
    print(i)

# WAP to print 100 to 5 on console using for loop
for i in range(100,4,-1):
    print(i)

# WAP to print all odd number from 23 to 67 on console using for loop
for i in range(23,68,2):
    print(i)

for i in range(23,68):
    if i % 2 != 0:
        print(i)

for i in range(23,68):
    if i % 2 == 1:
        print(i)


# prime number - the number is divisible by 1 and itself
# way-1
num = 7
count = 0

for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count == 2 :
    print(num, "is a prime number")
else :
    print(num, "is a not prime number")

# way-2
num = 7
count = 0

for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count == 0 :
    print(num, "is a prime number")
else :
    print(num, "is a not prime number")

# way-3
num = 7
count = 0

for i in range(2,num//2 + 1):
    if num % i == 0:
        count += 1
if count == 0 :
    print(num, "is a prime number")
else :
    print(num, "is a not prime number")

# way-4
num = 7
count = 0

for i in range(2,num//2 + 1):
    if num % i == 0:
        count += 1
        break
if count == 0 :
    print(num, "is a prime number")
else :
    print(num, "is a not prime number")

