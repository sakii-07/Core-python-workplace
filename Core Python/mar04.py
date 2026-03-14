'''
Dictionary :- Dictionary is mutable, heterogenious collection of element where order is not 
              maintained(before python 3.7) , now it is ordered (after 3.7+) and values are stored 
              in key-value pair. 

              Keys are unique in nature, values may be duplicate.

              key : value

              key must be immutable datatype, values may mutable or immutable.

              immutable datatypes :- int, float, complex, bool, string,    tuple, frozen set

Q. how to create empty dict?
  varname = {}

Q. how to add data into dictionary?
--> var[key] = value # {key : value}

methods of dictionary ----> 1) get() - access single element in dictionary
                            2) keys() - returns the all keys of dictionary
                            3) values() - returns the all values of dictionary
                            4) items() - returns the all keys and value of dictionary
'''
# level o dictionary - dict student roll no and name
stud_db = {}
stud_db[1]="sakshi"
stud_db[2]="amruta"
stud_db[3]="divya"
stud_db[4]="pranjali"
stud_db[5]="sojar"
print(stud_db) # {1: 'sakshi', 2: 'amruta', 3: 'divya', 4: 'pranjali', 5: 'sojar'}

'''
Q. how to access single element in dictionary?
--> by using key or get method
'''
# using key value
v1 = stud_db[1]
print(v1) # sakshi

# using get method
v2 = stud_db.get(3)
print(v2) # divya

v1 = stud_db[30]
print(v1) # KeyError: 30

# using get method
v2 = stud_db.get(30)
print(v2) # None

'''
keys() :- keys() will return all keys from dictionary
'''

# Iterating over key
# way 1 : to display key
for i in stud_db:
    print(i)

# way 2 : to display key
for i in stud_db.keys():
    print(i)
'''
1
2
3
4
5
''' 
'''
values() :- values() will return all values from dictionary
'''
# way 1 : dislpay all values
for i in stud_db:
    print(i,"-->",stud_db.get(i))

# way 2 : display all values
for i in stud_db:
    print(stud_db.values())

for i in stud_db.values():
    print(i)
'''
1 --> sakshi
2 --> amruta
3 --> divya
4 --> pranjali
5 --> sojar
'''

# way 3 :- display keys as well as values
for k in stud_db:
    print(k,stud_db[k])
  
'''
items() meethod :- return all key and values in tuple
'''
for k in stud_db.items():
  print(k)
'''
(1, 'sakshi')
(2, 'amruta')
(3, 'divya')
(4, 'pranjali')
(5, 'sojar')
'''
for t in stud_db.items():
  k,v = t
  print(k,"---->",v)

for k,v in stud_db.items():
  print(k,"---->",v)
'''
1 ----> sakshi
2 ----> amruta
3 ----> divya
4 ----> pranjali
5 ----> sojar
'''