'''
Higher order function :-
            1) map - used to mapping data and lnght of the both sequence is always same
            2) filter
            3) reduced
'''
# add grace marks in original list of marks 
# way 1
marks = [67,46,90,67,89,90,36,47]
grace_marks = []
for i in marks:
    grace_marks.append(i+5)
print("grace marks :",grace_marks)

# way 2 
def grace(l):
    l2 = []
    for i in l:
        l2.append(i+5)
    return l2
gracemarks = grace(marks)

# way 3
def add(m):
    return m+5
def grace(l):
    l2 = []
    for i in l:
        l2.append(add(i))
    return l2
gracemarks = grace(marks)

# way-4
# by using map function
grace_marks = list(map(add,marks))
print(grace_marks)

# Task - map original marks with grace marks but dont give marks to student who scores more than 90.
def addGrace(m):
    if m >= 90:
        return m
    else:
     return m+5
grace_marks = list(map(addGrace,marks))
print(grace_marks)

'''
2) filter - used to filter the elements from sequence as per condition
'''
original_marks = [78,89,90,67,98,90,56,73,82]
topper_marks = []
def top_marks(m):
    if m >= 90:
        return True
    else:
        return False
topperList = list(filter(top_marks,original_marks))
print(topperList)

# task - filters all odd marks from original marks sequence
original_marks = [78,89,90,67,98,90,56,73,82]

odd_marks = []
def oddMarks(m):
    if m%2==1:
        return True
    else:
        return False
    
oddMarksList = list(filter(oddMarks,original_marks))
print(oddMarksList)

'''
3) reduce function -  it is used to reduce sequence to single element
'''

# sum of all element
original_marks = [78,89,90,67,98,90,56,73,82]

def addTwo(a,b):
    return (a+b)

from functools import reduce
res = reduce(addTwo,original_marks,initial=0)
print("sum of all ",res) # sum of all  723

res1 = reduce(addTwo,original_marks,initial=1000)
print("sum of all ",res1) # sum of all  1723

# Find max in list
original_marks = [78,89,90,67,98,90,56,73,82]

def get_max(a,b):
    if a>b:
        return a
    else :
        return b 

import functools
res = reduce(get_max,original_marks,initial=0)
print("maximum of all ",res) # maximum of all  98

# Find max in list
original_marks = [78,89,90,67,98,90,56,73,82]

def get_min(a,b):
    if a>b:
        return b
    else :
        return a

from functools import reduce
res = reduce(get_min,original_marks)
print("minimum of all ",res) # minimum of all  56