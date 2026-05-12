# ïƒ˜Sum the elements of a list: Given the list [1, 2, 3, 4, 5], write a for loop that sums all the elements.
l = [1, 2, 3, 4, 5]

sum = 0 

# way - 1
for i in l:
    sum += i
print("Total : ", sum) # Total : 15

# way - 2
i = 0
while i < len(l):
    sum += l[i]
    i += 1
print(sum) # 15

# ïƒ˜Double each element in a list: Given the list [2, 4, 6, 8], write a for loop that doubles each element and prints the result.
l = [2, 4, 6, 8]

# Way - 2
for i in l:
    print(i*2,end=" ") # 4 8 12 16

# Way - 2
i = 0
while i < len(l):
    print(l[i]*2,end=" ") # 4 8 12 16
    i += 1

# Way - 3
l1 = list(map(lambda a:a*2,l))
print(l1) # [4, 8, 12, 16]

# ïƒ˜Create a new list by adding 10 to each number in the original list: Given the list [5, 10, 15, 20], create a new list where each element is increased by 10 using a for loop.
l = [5, 10, 15, 20]
l2 = []
for i in l:
    l2.append(i+10)
print(l2) # [15, 20, 25, 30]

# ïƒ˜Find the sum of elements in a set: Given the set {10, 20, 30, 40, 50}, write a for loop to find the sum of all elements in the set.
s = {10, 20, 30, 40, 50}
sum = 0
for i in s:
    sum += i
print(sum) # 150

# ïƒ˜Remove duplicates from a list using a set: Given the list [1, 2, 2, 3, 4, 4, 5], convert it to a set and print the unique elements.
l1 = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(l1))
print(unique) # [1, 2, 3, 4, 5]

# ïƒ˜Find the sum of all values in a dictionary: Given the dictionary {'a': 1, 'b': 2, 'c': 3}, write a for loop to find the sum of all values.
d = {'a': 1, 'b': 2, 'c': 3}
sum = 0
for i in d:
    sum += d[i]
print(sum) # 6

# ïƒ˜ Print keys and values in reverse order: Given the dictionary {'apple': 5, 'banana': 3, 'cherry': 8}, write a for loop that prints the keys and their values in reverse order.
d = {'apple': 5, 'banana': 3, 'cherry': 8}

for k,v in reversed(d.items()):
    print(k," : ",v)
'''
cherry  :  8
banana  :  3
apple  :  5
'''  

# ïƒ˜ Count the length of each string in a dictionary: Given the dictionary {'name': 'Alice', 'city': 'New York', 'country': 'USA'}, write a for loop that prints the length of each string value.
d = {'name': 'Alice', 'city': 'New York', 'country': 'USA'}
count = {}
for i in d:
    count[i] = len(d[i])
print(count) # {'name': 5, 'city': 8, 'country': 3}

# ïƒ˜Find the sum of elements in a tuple: Given the tuple (1, 2, 3, 4, 5), write a for loop to find the sum of all elements in the tuple.
t = (1, 2, 3, 4, 5)
sum = 0
for i in t:
    sum += i
print(sum) # 15

# ïƒ˜Create a new tuple where each element is squared: Given the tuple (1, 2, 3, 4), write a for loop to create a new tuple where each element is squared and print the result.
t = (1, 2, 3, 4)
t1 = ()
for i in t:
    t1 += (i**2,)
print(t1) # (1, 4, 9, 16)

# ïƒ˜Create a new list with the squares of elements from a tuple: Given the tuple (1, 2, 3, 4), create a new list where each element is the square of the elements from the tuple using a for loop.
t = (1, 2, 3, 4)
l1 = list(map(lambda a:a**2,t))
print(l1) # [1, 4, 9, 16]