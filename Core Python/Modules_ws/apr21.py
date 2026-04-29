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