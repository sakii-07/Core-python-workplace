# Immutable data types - int, floate, boolean, string, complex

p = 100
print(type(p), id(p)) # <class 'int'> 140736019607768

p = 99
print(type(p), id(p)) # <class 'int'> 140736019607736

s = "sakshi"
print(type(s), id(s)) # <class 'str'> 2287994949184

s = "sakshi jagtap"
print(type(s), id(s)) # <class 'str'> 2287995035632


f = 10.20
print(type(f), id(f)) # <class 'float'> 2287991501712

f = 50.20
print(type(f), id(f)) # <class 'float'> 2287994690864

b = True
print(type(b), id(b)) # <class 'bool'> 140736018696960

b = False
print(type(b), id(b)) # <class 'bool'> 140736018696992

'''list - List is mutable, heterogeneous colletion of element, insertion is maintained 
and duplicates are allowed. we can fetch data using indexing and slicing and sequence data type
'''
my_list = []
print(type(my_list),id(my_list))

my_list.append(10)
print(id(my_list))

my_list.append(-20.5)
print(id(my_list))

my_list.append("sai")
print(id(my_list))

my_list.append("true")
print(id(my_list))

my_list.append(50)
print(id(my_list))

my_list.append("sai")
print(id(my_list))

print(my_list) # [10, -20.5, 'sai', 'true', 50, 'sai']

my_list[2] = "sai baba"

print(my_list) # [10, -20.5, 'sai baba', 'true', 50, 'sai']