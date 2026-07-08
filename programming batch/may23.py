# Find student how scored above average marks

marks = {"Sakshi":89,"Supriya":90,"Shital":90,"Pranali":56,"Amruta":78,"Divya":84}

students = {}
avg = sum(marks.values())/len(marks)
# print(avg)
for i in marks:
    if marks[i] > avg:
        students[i] = marks[i]

print("count : ",len(students))

# way - 2
marks = [90,67,90,45,90,67,45,89,90,56]
avg = sum(marks)/len(marks)
counts = {}
for i in marks:
    count = 0
    for j in marks:
        if j == i:
            count += 1
    if count > 1:
        if i not in counts:
            counts[i] = count
print(counts)


# find how many students scored same marks 
marks = {"Sakshi":89,"Supriya":90,"Shital":90,"Pranali":56,"Amruta":56,"Divya":56}
count = {}
for i in marks:
    if marks[i] not in count:
        count[marks[i]] = 1
    else:
        count[marks[i]] += 1

for j in count:
    if count[j] > 1:
        print("same marks count : ",count[j],"and their marks",j)


'''
principle sir has problem of mail repeatation.  student are sending mail multiple times to sir. 
Principle sirs assistas  need to delete repeated mail. Find how many repeated mails to delete for 
each students.
'''

mails = ["sakshi@gmail.com","supriya@gmail.com","sakshi@gmail.com","sakshi@gmail.com","supriya@gmail.com","shital@gmail.com"]

repeat_email = {}

for m in mails:
    if m not in repeat_email:
        repeat_email[m] = 1
    else:
        repeat_email[m] += 1

for i in repeat_email:
    if repeat_email[i] > 1:
        print(i,"--->",repeat_email[i]-1)

delete_email = {}
for m in mails:
    count = 0
    for j in mails:
        if m == j:
            count += 1

    if repeat_email[i] > 1:
        # delete_email[i] = count-1
        print(delete_email)

# Way - 2
mails = ["sakshi@gmail.com","supriya@gmail.com","sakshi@gmail.com","sakshi@gmail.com","supriya@gmail.com","shital@gmail.com"]

unique = list(set(mails))

for u in unique:
    if mails.count(u) > 1:
        print(f"{u} delete {mails.count(u)-1}")

# create a empty list
users = []
l1 = list()
print(type(l)) # <class 'list'>
print(type(l1)) # <class 'list'>

name = input("Enter name : ")
users.append(name)

for i in range(5):
    name = input("Enter name : ")
    users.append(name)
print(users)

while(True):
    name = input("Enter name : ")
    users.append(name)
    ch = input("Enter your choice to continue (y/n)").lower()

    if ch == 'n':
        print(users)
        break

d = {}
for i in range(4):
    emp_name = input("Enter employee name : ")
    sal = float(input("Enter salary : "))
    d[emp_name] = sal
print(d)

d = {}
while True:
    emp_name = input("Enter employee name : ")
    sal = float(input("Enter salary : "))

    d[emp_name] = sal

    ch = input("Do you want to add another employee details (y/n) ").lower()

    if ch == 'n':
        break
print(d)

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]


# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     students.append([name, score])

# Get unique scores and sort them
scores = sorted(set(score for name, score in students))
print(scores)

# Second lowest score
second_lowest = scores[1]

# Get names with second lowest score
names = []

for name, score in students:
    if score == second_lowest:
        names.append(name)

# Print names alphabetically
for name in sorted(names):
    print(name)


students = []

name = input()
score  = float(input())
students.append([name,score])

score = sorted(set(score for name ,score in students))
print(score)
second_lowest = score[1]

names = []
for name,score in students:
    if second_lowest == score:
        names.append(name)
for name in sorted(names):
    print(name)
student_marks = {}
for _ in range(int(input("Enter"))):
    name , *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_input = input()
marks = student_marks[query_input]
avg = sum(marks)/len(marks)

print(f"{avg:.2f}")

# print(abs(complex(-1.0,0.0)))
import cmath
comp  = complex(input("Enter complex number : "))
print(comp)

print(abs(comp))
print(cmath.phase(comp))

import math

ab = int(input())
bc = int(input())

angle =math.degrees(math.atan(ab/bc))
print(str(round(angle))+chr(176))
print(100//9)
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    # print((10**i // 9) ** 2)
    print(10**i)
    print(10**i // 9)


for i in range(1,int(input())):
    print(i*(10**i - 1)//9)

from collections import Counter

if __name__ == '__main__':
    s = input()

    count = Counter(s)

    result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    for char, freq in result[:3]:
        print(char, freq)
