'''
3) collections ----> This module is extention of tuple, list, dict data types in python.
                            1) counter
                            2) namedtuple
                            3) defaultdict
                            4) deque
                            5) orderdict

1) counter  -: counter class in collecton module is used to count the number of occurances of each element
'''
import collections

l = [1,2,3,4,5,1,2,3,2,3,1]

count = {}

for i in l:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
print(count) # {1: 3, 2: 3, 3: 3, 4: 1, 5: 1}

count2 = collections.Counter(l)
print(count2) # Counter({1: 3, 2: 3, 3: 3, 4: 1, 5: 1})
print(count2.most_common(3)) # [(1, 3), (2, 3), (3, 3)]

print(collections.Counter("Insagram")) # Counter({'a': 2, 'I': 1, 'n': 1, 's': 1, 'g': 1, 'r': 1, 'm': 1})

'''
2) defaultdict  -: it is used when contsraint not on key
'''

l2 = [1,4,2,1,2,3,1,3]
l2 = "hello all"
d = collections.defaultdict(int)

for i in l2:
    d[i] += 1

print(d) # defaultdict(<class 'int'>, {1: 3, 4: 1, 2: 2, 3: 2})

'''
3) orderedDict ---> 
'''

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d) # {'a': 1, 'b': 2, 'c': 3}

od = collections.OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od) # OrderedDict({'a': 1, 'b': 2, 'c': 3})

'''
4) namedtuple --> It create light weighted tuple
'''
from collections import namedtuple
Student = namedtuple("Student",['name','roll_no','age','city'])
s1 = Student('raj',2,23,'pune')
s2 = Student('pavan',4,19,'mumbai')
s3 = Student('jay',7,21,'pune')

print(s1.name) # raj
print(s2.age) # 19
print(s3.city) # pune

'''
5) deque
'''
from collections import deque
l3 = deque([1,2,3,4,5,1,2,3,4])
print(l3) # deque([1, 2, 3, 4, 5, 1, 2, 3, 4])

l3.pop()
print(l3) # deque([1, 2, 3, 4, 5, 1, 2, 3])

l3.popleft()
print(l3) # deque([2, 3, 4, 5, 1, 2, 3])

l3.append(6)
print(l3) # deque([2, 3, 4, 5, 1, 2, 3, 6])

l3.appendleft(9)
print(l3) # deque([9,2, 3, 4, 5, 1, 2, 3, 6])

l3.rotate(2)
print(l3) # deque([3, 6, 9, 2, 3, 4, 5, 1, 2])

'''
6) ChainMap
'''
from collections import ChainMap

d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}

d = ChainMap(d1,d2)
print(d) # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
print(d['a']) # 1
print(d['d']) # 4

# collections in python 
import collections 

# 1. Counter class in collections module is used to count the number of occurrences of each element 
# in a list or a string. It returns a dictionary-like object where the keys are the elements and 
# the values are the counts.
# l = [1, 2, 3, 4, 5, 1, 2, 3, 4,1,3]

# count = {}

# for i in l:
#     if i in count:
#         count[i] = count[i] + 1
#     else:
#         count[i] = 1

# print(count)

# count2 = collections.Counter("Hello all, welcome to python programming")
# print(count2.most_common(3))

# 2. defaultdict class in collections module is a subclass of the built-in dict class. 
# It provides a default value for a key that does not exist in the dictionary. 
# This means that if you try to access a key that is not present in the dictionary, 
# it will return the default value instead of raising a KeyError.


# l2 = [1,4,2,1,2,3,1,3]
# l2 = "Hello all, welcome to python programming"
# d = collections.defaultdict(int)

# for i in l2:
#     d[i] = d[i]+1

# print(d)

# 3. OrderedDict class in collections module is a subclass of the built-in dict class.
# It maintains the order of the keys as they were inserted into the dictionary.
# Note :-> After Python 3.7, the built-in dict also maintains the insertion order, 
# so the OrderedDict is not necessary for this purpose in modern Python versions. 
# However, it still provides some additional methods that are not available in the regular dict.

# d = {}
# d["a"] = 1
# d["b"] = 2
# d["c"] = 3
# print(d)

# od = collections.OrderedDict()
# od["a"] = 1
# od["b"] = 2
# od["c"] = 3
# print(od)


# 4. namedtuple class in collections module is a factory function 
# that creates a new subclass of the built-in tuple class.
# It allows you to create a tuple with named fields,
#  which can be accessed using dot notation.

# t1= ("Jay", 1, 30,"Pune")
# t2= ("Pavan", 3, 21,"Mubai")
# t3= ("Raj", 6, 26,"Pune")
# print(type(t1)) # <class 'tuple'>

# print(t1[0]) # Jay
# print(t2[1]) # 3

# from collections import namedtuple
# Student = namedtuple("Student", ["name", "roll_no", "age", "city"])
# s1 = Student("Jay", 1, 30, "Pune")
# s2 = Student("Pavan", 3, 21, "Mumbai")
# s3 = Student("Raj", 6, 26, "Pune")

# print(s1.name) # Jay
# print(s2.roll_no) # 3
# print(s3.age) # 26

# print(type(s1)) # <class '__main__.Student'>


# class Student2:
#     def __init__(self, name, roll_no, age, city):
#         self.name = name
#         self.roll_no = roll_no
#         self.age = age
#         self.city = city


# 5. deque class in collections module is a double-ended queue 
# that allows you to add and remove elements from both ends of the queue efficiently.
# It provides methods for adding and removing elements from both ends of the queue,
# as well as methods for rotating the queue and accessing elements by index.


# l = [1, 2, 3, 4, 5]
# print(l) # [1, 2, 3, 4, 5]
# l.append(6)
# print(l) # [1, 2, 3, 4, 5, 6]
# l.pop()
# print(l) # [1, 2, 3, 4, 5]

from collections import deque

d = deque([1, 2, 3, 4, 5])
print(d) # deque([1, 2, 3, 4, 5])
d.append(6)
print(d) # deque([1, 2, 3, 4, 5 , 6])
d.appendleft(7)
print(d) # deque([7, 1, 2, 3, 4, 5 , 6])

d.pop()
print(d) # deque([7, 1, 2, 3, 4
d.popleft()
print(d) # deque([1, 2, 3, 4, 5])

# d.remove(3)
# print(d) # deque([1, 2, 4, 5])
d.rotate(2)
print(d) # deque([4, 5, 1, 2, 3

# Interview question :-> What is the difference between a list and a deque in Python?
# 2 Q. What is differenc ebetween tuple and namedtuple in Python?
# 3 Q. What is the difference between a regular dictionary and an OrderedDict in Python?


# 6. ChainMap class in collections module is a class that groups
# multiple dictionaries together to create a single, updateable view.
# It allows you to search through multiple dictionaries as if they were a single dictionary.
# if a key is not found in the first dictionary, it will look for it in the next dictionary, 
# and so on, until it finds the key or exhausts all the dictionaries.
# if multiple keys are present in multiple dictionaries, 
# the value from the first dictionary will be returned.

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "a": 4}

from collections import ChainMap
cm = ChainMap(d1, d2)
print(cm) # ChainMap({'a': 1, 'b': 2}, {'``c': 3, 'd': 4})
print(cm["a"]) # 1
print(cm["c"]) # 3  