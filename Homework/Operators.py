# you have one list of student marks create two sublists for even and odd marks student
std = []
std.append(78)
std.append(97)
std.append(90)
std.append(45)
std.append(83)
std.append(67)
std.append(92)
std.append(87)
std.append(67)

print("Student marks : ",std)

even_list = []
odd_list = []

for i in std:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even list : ",even_list)
print("Odd list : ",odd_list)

# Check whether a given year is a leap year.
year = 2003
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else :
    print("not leap year")

# Check whether a number is divisible by both 5 and 11 using logical operators.
num = 55
if (num % 5 == 0) and (num % 11 == 0):
    print("Given number is divisible by both 5 and 11")
else:
    print("Given number is not divisible by both 5 and 11")

# Check Character Type - Take a character and check whether it is: Alphabet, Digit, Special character
ch = input("Enter the character : ")
if (ch >= 'a' and ch <= 'z') or (ch <= 'A' and ch >= 'Z'):
    print("Alphabet")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special character")

# Check Vowel or Consonant Take a character and check whether it is: Vowel or  Consonant
ch = input("Enter the character : ")
if ch in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")

# Write a Python program to separate numbers from a list into four lists: divisible by both 3 and 5, divisible by 3, divisible by 5, and not divisible by either.
num = [56,85,87,90,21,12,42,45,94,19,42,78,55]
both_3_And_5 = []
div_by_3 = []
div_by_5 = []
notDivBy3And5 = []
for i in num:
    if i % 3 == 0 and i % 5 == 0:
        both_3_And_5.append(i)
    elif i % 3 == 0:
        div_by_3.append(i)
    elif i % 5 == 0:
        div_by_5.append(i)
    else :
        notDivBy3And5.append(i)
print("Number divisible by 3 and 5 : ",both_3_And_5)
print("Number divisible by 3 : ",div_by_3)
print("Number divisible by 5 : ",div_by_5)
print("Number not divisible by 3 and 5 : ",notDivBy3And5)
'''
Number divisible by 3 and 5 :  [90, 45]
Number divisible by 3 :  [87, 21, 12, 42, 42, 78]
Number divisible by 5 :  [85, 55]
Number not divisible by 3 and 5 :  [56, 94, 19]
'''

# square of even numbers
even_list = []
for i in range(1,16):
    if i%2==0:
        even_list.append(i**2)
    
print("Even numbers square : ",even_list) # Even numbers square :  [4, 16, 36, 64, 100, 144, 196]

# Given two sets, perform the following operations: Union, Intersection, Difference
s1 = {2,4,6,8}
s2 = {4,6,10,12}

print("Union of s1 and s2 : ", s1.union(s2))
print("Intersection of s1 and s2 : ", s1.intersection(s2))
print("Difference of s1 and s2 : ", s1.difference(s2))

'''
Union of s1 and s2 :  {2, 4, 6, 8, 10, 12}
Intersection of s1 and s2 :  {4, 6}
Difference of s1 and s2 :  {8, 2}
'''

# Given a dictionary of subject marks, calculate: total marks, average marks
marks = {"Math": 80, "Science": 75, "English": 85, "History": 70}

# way-1
total = 0
for sub, mrk in marks.items():
    total = total + mrk

avg = total / len(marks)
print("Total marks : ", total)
print("Average : ", avg)

# Way-2
mrk = marks.values()
total = sum(mrk)
avg = total / len(marks)
print("Total marks : ", total)
print("Average : ", avg)

'''
Total marks :  310
Average :  77.5
'''

# Given a dictionary of student, calculate: total marks, average marks
std = {1 : {"name": "sakshi", "marks" : {"Math": 96, "Science": 90, "English": 70, "History": 80}},
       2 : {"name": "sojar", "marks" : {"Math": 80, "Science": 58, "English": 85, "History": 83}},
       3 : {"name": "pranjali", "marks" : {"Math": 78, "Science": 82, "English": 48, "History": 62}},
       4 : {"name": "Isha", "marks" : {"Math": 67, "Science": 85, "English": 85, "History": 70}}
       }
total = 0
for i in std:
    name = std[i]["name"]
    mrk = std[i]["marks"].values()
    total = sum(mrk)
    avg = total / len(mrk)
    print(name ," : Total --->",total,", Avg : -->",avg)
'''
sakshi  : Total ---> 336 , Avg : --> 84.0
sojar  : Total ---> 306 , Avg : --> 76.5
pranjali  : Total ---> 270 , Avg : --> 67.5
Isha  : Total ---> 307 , Avg : --> 76.75
'''

# Find duplicate 
nums = [4,2,3,2,4,5,6]
duplicate = []

for n in nums:
    if nums.count(n) > 1 and n not in duplicate:
        duplicate.append(n)
print("Duplicate elements:", duplicate) # Duplicate elements: [4, 2]