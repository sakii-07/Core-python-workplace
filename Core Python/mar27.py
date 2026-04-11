'''
Comprehension


1) list comprehension
    syntax ---->   new_list = [expression for i in iterable if condition]
'''
# Task - Create a new list of squares of all elemts from given list
# way 1 - using lambda
l = [1,5,7,2,8,8,45,3]
square_list = list(map(lambda x:x*x,l))
print(square_list) # [1, 25, 49, 4, 64, 64, 2025, 9]

# way 2 - using for loop
square_list = []
for i in l:
    square_list.append(i**2)
print(square_list) # [1, 25, 49, 4, 64, 64, 2025, 9]

# way 3 - using list comprehention
square_list = [i*i for i in l]
print(square_list) # [1, 25, 49, 4, 64, 64, 2025, 9]

# filter odd numbers from list using comprehention
odd_list = [i for i in l if i%2==1]
print(odd_list) # [1, 5, 7, 45, 3]

'''
new_list = [expression1 if condition else expression2 for i in iterable]
'''
# Replace all even numbers from given list with "Even" string keep odd numbers as it is in list
new_list = [i if i%2==1 else "Even" for i in l]
print(new_list) # [1, 5, 7, 'Even', 'Even', 'Even', 45, 3]

'''
2) Dictionary comprehension 

    syntax : d = {key:value for i in iterable}
'''
# key=number value=cube of number
d = {i:(i**3) for i in l}
print(d) # {1: 1, 5: 125, 7: 343, 2: 8, 8: 512, 45: 91125, 3: 27}

# list to dict
l = [1,5,7,2,8,8,45,3]
d = {i:i+1 for i in l}
print(d) # {1: 2, 5: 6, 7: 8, 2: 3, 8: 9, 45: 46, 3: 4}

# task - 
# way 1 - using for loop
l1 = [[1,2],[3,4],[5,6],[7,8]]
l2 = []
for i in l1:
    for j in i:
        l2.append(j)
print(l2) # [1, 2, 3, 4, 5, 6, 7, 8]

# way 2 : using list comprehension
l2 = [j for i in l1 for j in i]
print(l2) # [1, 2, 3, 4, 5, 6, 7, 8]
