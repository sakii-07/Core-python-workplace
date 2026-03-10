''''
Tuple methods ----> 1) count()
                    2) index()
'''

'''
Set ----> Set is mutable, heterogenious collection of immutable element where insertion is not maintained and 
          duplicates are allowed

methods ----> 1) add()
              2) remove()
              3) union()
              4) interseption()
'''
# # how to create empty set :- varName = set()
# v = set()
# print(type(v)) # <class 'set'>
# print(v) # set()

# how to add data in list :- using add() method
st  = set()
st.add(10)
st.add("sakshi")
st.add(20)
st.add(34.14)
st.add(10)
st.add(False)
st.add(10)
print(st) # {False, 34.14, 'sakshi', 10, 20}
print(len(st)) # 5

# index is not present
print(st[0]) # TypeError: 'set' object is not subscriptable

t = (10,20,30)
st.add(t)
print(st) # {False, 34.14, 10, (10, 20, 30), 20, 'sakshi'}

l = [10,20,20]
st.add(l)
print(st) # TypeError: cannot use 'list' as a set element (unhashable type: 'list')

s2 = {10,20,20}
st.add(s2)
print(st) # TypeError: cannot use 'set' as a set element (unhashable type: 'set')

# how to access data from set - using for loop
for i in st :
    print(i)

st.remove(10)
print(st) # {False, 34.14, 20, 'sakshi'}

st1 ={100,2,3.3,4,5,6,7,8,9}
st2 = {1.1,2,4,5, 2.2, 3.3, "saki"} 

# using methods
st3 = st1.union(st2)
print(st3) # {1.1, 2, 3.3, 100, 5, 4, 6, 7, 8, 9, 2.2, 'saki'}

st3 = st1.intersection(st2)
print(st3) # {2, 3.3, 4, 5}

# using operators
print(st1 | st2) # {1.1, 2, 3.3, 100, 5, 4, 6, 7, 8, 9, 2.2, 'saki'}
print(st1 & st2) # {2, 3.3, 4, 5}

l1 = [91,20,99,30,40,88,30,91,67,45,90,91,36,87,78]

s = set(l1)
unique_list = list(s)
print(s) # {40, 10, 20, 30}

# Find max element from fiven data set
print(max(l1)) # 99

topper = l1[0]
for i in l1 :
    if i > topper :
        topper = i
print("Topper = ",topper) # Topper =  99

# Find second max element from fiven data set
s = set(l1)
unique_marks = list(s)
um = sorted(unique_marks)
print("topper = ",um[-1]) # topper =  99
sec_topper = um[-2]
print(sec_topper) # 91


topper = l1[0]
for i in l1 :
    if i > topper :
        topper = i
print("Topper = ",topper) # Topper =  99

# count how many second toppers in class

count = 0
for i in l1 :
    if i == sec_topper:
        count =count +1
print(count) # 3



