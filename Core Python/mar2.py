'''
1) frozen set ----> frozen set is exactly same as set the only difference is set is mutable and
                 fs is immutable

                 Frozen set is immutable , collection of immutable elements where order is not maintained 
                 and duplicates are not allowed

                 fixed in size

                 unique + fixed value
'''
'''
Q. how to create frozen set.
use frozenset()

There is no    1) add
              2) remove
              3) insert methods
'''
# s ={1,3,4,6,7,8} # set
# s.add("saki")

# fs = frozenset(s) # frozenset
# print(fs) # frozenset({1, 3, 4, 6, 7, 8, 'saki'})
# print(type(fs)) # <class 'frozenset'>
# # fs.add("saki") # AttributeError: 'frozenset' object has no attribute 'add'

'''
2) Range data type ----> Range is one data type in python
                         Used to create sequence of integers in python.

Q. how to create range in python?
--> varName = range()

-- returns integer

'''
# r = range(5)
# print(r) # range(0, 5)
# print(type(r)) # <class 'range'>

# a = 10
# b = str(a)
# print(type (b)) # <class 'str'>

'''
we can create range in pyhon using following ways
    1) r = range(n) - it will return range from 0 to n-1
    eg. r = range(5)
        range 0 o 4

    2) r = range(start, end)
        eg. r = range(55,96)
            range 55 to 95
    
    3) r = range(start,end,step_size)
        eg. r = range(2,21,2)
            range 2 to 20 and step sixe is 2
        --->2,4,6,8,10,12,14,16,18,20

            r = range(100,1,-1) 

            r = range(5,51,5)

Q. how to iterate range in python?
--> using for loop
'''

# for i in 10:
#     print(i) # TypeError: 'int' object is not iterable

# for i in '10':
#     print(i) # string is sequence and iterable so it prints each character one by one

# r = range(0,5)
# for i in r:
#     print(i) # 0 1 2 3 4

# for i in range(5):
#     print(i)  # 0 1 2 3 4

# N = 9
# for i in range(N):
#     print(i)  # 0 1 2 3 4 5,6,7,8

# s = "Instagram"
# N = len(s)
# for i in range(N):
#     print(i) # 0 1 2 3 4 5,6,7,8

# s = "Instagram"
# for i in range(len("Instagram")):
#     print(i," ----> ",s[i])
'''
0  ---->  I
1  ---->  n
2  ---->  s
3  ---->  t
4  ---->  a
5  ---->  g
6  ---->  r
7  ---->  a
8  ---->  m
'''

# s = "Instagram"
# for i in range(len(s)-1,-1, -1):
#     print(i," ----> ",s[i])

# s = "Instagram"
# for i in range(len(s)):
#     print(len(s)-1-i," ----> ",s[len(s)-1-i])
'''
8  ---->  m
7  ---->  a
6  ---->  r
5  ---->  g
4  ---->  a
3  ---->  t
2  ---->  s
1  ---->  n
0  ---->  I
'''

