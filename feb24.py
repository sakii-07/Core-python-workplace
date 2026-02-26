
'''List 
-- collective datatype
-- hectrogenious collection
-- enclosed by [] sepratred by(,)
-- order
-- mutable
-- allow Duplicates
-- we can featch data using indexing and slicing
-- sequence Datatype'''

l1 = []
print(type(l1))

l2 = [10,20,30]
print(l2)
print(type(l2))

l3 = [10,20,10,10]
print(l3)

l4 = [10, 10.5, "Ritik", 10+20j, True ,[10,20,30],(1,2,3),{3,9,6,6,6},{1:1, 2:4}]

print(l4)

# fetch "Ritik"
print(l4[2])

# fetch {3,9,6}
print(l4[-2][2])
print(l4[-1][1])

l5 = ["10","20","30"]

# Method to add element in list 
# 1. append
# 2. insert
# 3. extend 

# l5.append([100,200,"Name"])

l5 = ["10","20","30"]

l5.insert(2,[1000,2000])  # ['10', '20', 1000, '30']     # ['10', '20', [1000, 2000], '30']

l5.extend([1000])   # ['10', '20', '30', 100, 200, 300]

l5.insert(20, 300)

print(l5)  

print(l5[-1])

'''
list ---> collective datatype
          heterogeneous collection of element
          allow duplicates 
          order preserved
          mutable
          we can fetch data using indexing
'''

l1 = []
print(type(l1)) # <class 'list'>

l2 = [1,2,3,4]
print(l2[1]) # 2

'''
In a list, if it contains another list, tuple, or set, each collection acts as a single element.
We can access sub-elements of list and tuple using indexing, 
but we cannot access sub-elements of set because it does not support indexing.
'''
l3 = [10, 20.23,True, 10+2j, (1,2,3),[2,1,2,1,2],{1:1, 2:4}]
print(l3[-1][2]) # 3

'''
Methods to add element in list
    1. append - we can add element at the -1 position
                we can add multile element
                if we pass list it gives nested list
                we can not store method because its return type is none
    2. insert - add data at specific position
                if we add data at any position then previous value shifted right 
    3. extend - it allows only iterable values not allows single value
'''

'''
    1. append - add element at the end
'''
l4 = [10, 20, 30]
l4.append(100) # [10, 20, 30, 100]
print(l4)

'''
if we use same variable in list for update value then it gives error msg due to
        1. interpreter
        2. garbage collector
        example - 
'''
l5 = [10,20,30]
l5 = l5.append(100) # None
print(l5)

'''
    we can not pass the two values in append method
'''
l4 = [10, 20, 30]
l4.append(100,200) # TypeError: list.append() takes exactly one argument (2 given)
print(l4)

'''
    we can add multiple values by using list, set, tuple or if we can pass list then it gives nested list
'''
l4 = [10, 20, 30]
l4.append([100,200]) # [10, 20, 30, [100, 200]]
print(l4)

l4.append({1:2, 3:4}) # [10, 20, 30, [100, 200], {1: 2, 3: 4}]
print(l4)

l4.append((3,5,2,7)) # [10, 20, 30, [100, 200], {1: 2, 3: 4}, (3, 5, 2, 7)]
print(l4)

'''
    2. insert() - if we add element at any index then present data or previous value shifted right
                  add data at specific position
'''
l5 = [10,20,30]

l5.insert(2,1000) # [10, 20, 1000, 30]
print(l5)

l5.insert(2,[1000,123]) # [10, 20, [1000, 123], 1000, 30]
print(l5)

'''
    3. extend - iterable
                not acceptes single value
                allowes iterable value means list, tuple, set , etc
'''

l6 = [20,30,40]
l6.extend([100,200,300]) # [20, 30, 40, 100, 200, 300]
print(l6)

l6 = [20,30,40]
l6.extend(100) # 'int' object is not iterable
print(l6)

l7 = [10,20,30]
l7.insert(-19,200) # [200, 10, 20, 30] - if any index is not present then negetive index value add at the first postion and positive index value added at last position
print(l7)

l7 = [10,20,30]
l7.insert(len(l7),200) # [10, 20, 30, 200]
print(l7)
