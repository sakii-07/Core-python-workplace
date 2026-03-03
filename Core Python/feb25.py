'''
List methods : 4) dir() - returns a list of all attributes, functions and methods of an object.
'''
l1 = []
print(dir(l1)) # ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
               # 'pop', 'remove', 'reverse', 'sort']

'''
5) clear() - remove all elements from a collection.
'''

l1 = [10,20,30,40]

l2 = l1.copy()
print("l1 :  " , l1)
print("l2 :  " ,l2)

l3 = l1
print("l3 :  " , l3)


print(l1.count(10))  # 1

print(l1.index(30))  # 2

print(l1.index(300))   # ValueError: 300 is not in list



print(l1.pop())  # 40

print(l1.pop(2))  #  30

print(l1.pop(-3))  #  20

l1.remove(10)

l1.remove(100) # ValueError: list.remove(x): x not in list
print("before : ",  l1)

l1.reverse() # [40, 30, 20, 10]

print(reversed(l1))  # <list_reverseiterator object at 0x0000019F9BC942B0>

print("use reversed class : ",list(reversed(l1))) # [40, 30, 20, 10]

l2 = [1,2,3,5,1,6,4,9]
print(sorted(l2))

l2.sort()

del l2[2]

del l2 
 
# print("after : ",l2)

str1 = "RitIK"

print(sorted(str1))

print(list(reversed(str1)))

# even numbers
l1 = [45,54,12,78,11,40,20]
for i in l1 :
    if(i % 2 == 0) :
        print(i) 

# even number in list
l1 = [45,54,12,78,11,40,20]
l2 = []
for i in l1 :
    if(i % 2 == 0) :
        l2.append(i)
print(l2) # [54, 12, 78, 40, 20]

# sum of even numbers
l1 = [45,54,12,78,11,40,20]
l2 = []
sum = 0
for i in l1 :
    if(i % 2 == 0) :
        l2.append(i)
        sum = sum + i
print(l2)
print(sum) # 204

# sum of even number in list
l1 = [45,54,12,78,11,40,20]
l2 = []
sum = 0
even_list = []
for i in l1 :
    if(i % 2 == 0) :
        l2.append(i)
        sum = sum + i
        even_list.append(sum)
print(l2) # [54, 12, 78, 40, 20]
print(sum) # 204
print(even_list) # [54, 66, 144, 184, 204]