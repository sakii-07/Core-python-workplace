# note / table 

'''   
| Operator | int+int | float+float | True+True | list+list | tuple+tuple | set+set    | dict+dict | string+string | False+False | complex+complex | fs+fs |
| -------- | ------- | ----------- | --------- | --------- | ----------- | ---------- | --------- | ------------- | ----------- | --------------- | ----- |
| +        | yes     | yes         | yes       | concat    | concat      | no         | no        | concat        | yes         | yes             | no    |
| -        | yes     | yes         | yes       | no        | no          | difference | no        | no            | yes         | yes             | yes   |
| *        | yes     | yes         | yes       | no        | no          | no         | no        | no            | yes         | yes             | no    |
| /        | yes     | yes         | yes       | no        | no          | no         | no        | no            | no          | yes             | no    |
| //       | yes     | yes         | yes       | no        | no          | no         | no        | no            | no          | no              | no    |
| %        | yes     | yes         | yes       | no        | no          | no         | no        | no            | no          | no              | no    |
| **       | yes     | yes         | yes       | no        | no          | no         | no        | no            | yes         | yes             | no    |


| Operator | int+float | int+True | int+False | int+complex | int+string | int+list | int+tuple | int+set | int+fs | int+dict |
| -------- | --------- | -------- | --------- | ----------- | ---------- | -------- | --------- | ------- | ------ | -------- |
| +        | yes       | yes      | yes       | yes         | no         | no       | no        | no      | no     | no       |
| -        | yes       | yes      | yes       | yes         | no         | no       | no        | no      | no     | no       |
| *        | yes       | yes      | yes       | yes         | yes        | yes      | yes       | no      | no     | no       |
| /        | yes       | yes      | no        | yes         | no         | no       | no        | no      | no     | no       |
| //       | yes       | yes      | no        | no          | no         | no       | no        | no      | no     | no       |
| %        | yes       | yes      | no        | no          | no         | no       | no        | no      | no     | no       |
| **       | yes       | yes      | yes       | yes         | no         | no       | no        | no      | no     | no       |


| Operator | float+int | float+True | float+False | float+complex | float+string | float+list | float+tuple | float+set | float+fs | float+dict |
| -------- | --------- | ---------- | ----------- | ------------- | ------------ | ---------- | ----------- | --------- | -------- | ---------- |
| +        | yes       | yes        | yes         | yes           | no           | no         | no          | no        | no       | no         |
| -        | yes       | yes        | yes         | yes           | no           | no         | no          | no        | no       | no         |
| *        | yes       | yes        | yes         | yes           | no           | no         | no          | no        | no       | no         |
| /        | yes       | yes        | no          | yes           | no           | no         | no          | no        | no       | no         |
| //       | yes       | yes        | no          | no            | no           | no         | no          | no        | no       | no         |
| %        | yes       | yes        | no          | no            | no           | no         | no          | no        | no       | no         |
| **       | yes       | yes        | yes         | yes           | no           | no         | no          | no        | no       | no         |


| Operator | list+tuple | list+set | list+fs | list+dict | tuple+set | tuple+fs | tuple+dict | set+fs | set+dict | fs+dict |
| -------- | ---------- | -------- | ------- | --------- | --------- | -------- | ---------- | ------ | -------- | ------- |
| +        | no         | no       | no      | no        | no        | no       | no         | no     | no       | no      |
| -        | no         | no       | no      | no        | no        | no       | no         | no     | no       | no      |
| *        | no         | no       | no      | no        | no        | no       | no         | no     | no       | no      |
| /        | no         | no       | no      | no        | no        | no       | no         | no     | no       | no      |
| //       | no         | no       | no      | no        | no        | no       | no         | no     | no       | no      |
| %        | no         | no       | no      | no        | no        | no       | no         | no     | no       | no      |
| **       | no         | no       | no      | no        | no        | no       | no         | no     | no       | no      |


'''

# int + float
print(10 + 3.5)   # 13.5
print(10 - 3.5)   # 6.5
print(10 * 3.5)   # 35.0
print(10 / 3.5)   # 2.857142857142857
print(10 // 3.5)  # 2.0
print(10 % 3.5)   # 3.0
print(10 ** 3.5)  # 3162.2776601683795

# int + Flase
pprint(34 + False)   # 34
print(34 - False)   # 34
print(34 * False)   # 0
print(34 / False)   # ZeroDivisionError: division by zero
print(34 // False)  # ZeroDivisionError: division by zero
print(34 % False)   # ZeroDivisionError: division by zero
print(34 ** False)  # 1

# int + complex
print(23 + (2+9j))   # (25+9j)
print(23 - (2+9j))   # (21-9j)
print(23 * (2+9j))   # (46+207j)
print(23 / (2+9j))   # (0.5411764705882353-2.4352941176470586j)
print(23 // (2+9j))  # TypeError: unsupported operand type(s) for //: 'int' and 'complex'
print(23 % (2+9j))   # TypeError: unsupported operand type(s) for %: 'int' and 'complex'
print(23 ** (2+9j))  # complex number result

# int + string
# multiplication (*) between an integer and a string repeats the string, but other arithmetic operators are not supported between int and str.
print(78 + "sakshi")   # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(78 - "sakshi")   # TypeError: unsupported operand type(s) for -: 'int' and 'str'
print(78 * "sakshi")   # sakshi repeated 78 times
print(78 / "sakshi")   # TypeError: unsupported operand type(s) for /: 'int' and 'str'
print(78 // "sakshi")  # TypeError: unsupported operand type(s) for //: 'int' and 'str'
print(78 % "sakshi")   # TypeError: unsupported operand type(s) for %: 'int' and 'str'
print(78 ** "sakshi")  # TypeError: unsupported operand type(s) for **: 'int' and 'str'

# int + True
print(34 + True)    # 35
print(34 - True)    # 33
print(34 * True)    # 34
print(34 / True)    # 34.0
print(34 // True)   # 34
print(34 % True)    # 0
print(34 ** True)   # 34

# int + list
# multiplication (*) between an integer and a list repeats the list, but other arithmetic operators are not supported between int and list.
l1 = [5,4,3,6,7,9,1]
print(12 + l1)   # TypeError: unsupported operand type(s) for +: 'int' and 'list'
print(12 - l1)   # TypeError: unsupported operand type(s) for -: 'int' and 'list'
print(12 * l1)   # list repeated 12 times
print(12 / l1)   # TypeError: unsupported operand type(s) for /: 'int' and 'list'
print(12 // l1)  # TypeError: unsupported operand type(s) for //: 'int' and 'list'
print(12 % l1)   # TypeError: unsupported operand type(s) for %: 'int' and 'list'
print(12 ** l1)  # TypeError: unsupported operand type(s) for **: 'int' and 'list'

# int + tuple
t1 = (3,5,8,5,9,2,1)

print(32 + t1)   # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
print(32 - t1)   # TypeError: unsupported operand type(s) for -: 'int' and 'tuple'
print(2 * t1)    # (3, 5, 8, 5, 9, 2, 1, 3, 5, 8, 5, 9, 2, 1)
print(32 / t1)   # TypeError: unsupported operand type(s) for /: 'int' and 'tuple'
print(32 // t1)  # TypeError: unsupported operand type(s) for //: 'int' and 'tuple'
print(32 % t1)   # TypeError: unsupported operand type(s) for %: 'int' and 'tuple'
print(32 ** t1)  # TypeError: unsupported operand type(s) for **: 'int' and 'tuple'

# int + dict
d1 = {2:5,6:4,8:9}

print(5 + d1)   # TypeError: unsupported operand type(s) for +: 'int' and 'dict'
print(5 - d1)   # TypeError: unsupported operand type(s) for -: 'int' and 'dict'
print(5 * d1)   # TypeError: unsupported operand type(s) for *: 'int' and 'dict'
print(5 / d1)   # TypeError: unsupported operand type(s) for /: 'int' and 'dict'
print(5 // d1)  # TypeError: unsupported operand type(s) for //: 'int' and 'dict'
print(5 % d1)   # TypeError: unsupported operand type(s) for %: 'int' and 'dict'
print(5 ** d1)  # TypeError: unsupported operand type(s) for **: 'int' and 'dict'

# int + set
s1 = {2,5,6,4,8,9}

print(4 + s1)   # TypeError: unsupported operand type(s) for +: 'int' and 'set'
print(4 - s1)   # TypeError: unsupported operand type(s) for -: 'int' and 'set'
print(4 * s1)   # TypeError: unsupported operand type(s) for *: 'int' and 'set'
print(4 / s1)   # TypeError: unsupported operand type(s) for /: 'int' and 'set'
print(4 // s1)  # TypeError: unsupported operand type(s) for //: 'int' and 'set'
print(4 % s1)   # TypeError: unsupported operand type(s) for %: 'int' and 'set'
print(4 ** s1)  # TypeError: unsupported operand type(s) for **: 'int' and 'set'

# int + frozenset
s1 = {2,5,6,4,8,9}
fs = frozenset(s1)

print(3 + fs)   # TypeError: unsupported operand type(s) for +: 'int' and 'frozenset'
print(3 - fs)   # TypeError: unsupported operand type(s) for -: 'int' and 'frozenset'
print(3 * fs)   # TypeError: unsupported operand type(s) for *: 'int' and 'frozenset'
print(3 / fs)   # TypeError: unsupported operand type(s) for /: 'int' and 'frozenset'
print(3 // fs)  # TypeError: unsupported operand type(s) for //: 'int' and 'frozenset'
print(3 % fs)   # TypeError: unsupported operand type(s) for %: 'int' and 'frozenset'
print(3 ** fs)  # TypeError: unsupported operand type(s) for **: 'int' and 'frozenset'

# float + string
print(34.12 + "sakshi")   # TypeError: unsupported operand type(s) for +: 'float' and 'str'
print(34.12 - "sakshi")   # TypeError: unsupported operand type(s) for -: 'float' and 'str'
print(34.12 * "sakshi")   # TypeError: can't multiply sequence by non-int of type 'float'
print(34.12 / "sakshi")   # TypeError: unsupported operand type(s) for /: 'float' and 'str'
print(34.12 // "sakshi")  # TypeError: unsupported operand type(s) for //: 'float' and 'str'
print(34.12 % "sakshi")   # TypeError: unsupported operand type(s) for %: 'float' and 'str'
print(34.12 ** "sakshi")  # TypeError: unsupported operand type(s) for **: 'float' and 'str'

# list + tuple
l1 = [3,4,5,6,7,8]
t1 = (4,7,8,9,1,2)

print(l1 + t1)   # TypeError: can only concatenate list (not "tuple") to list
print(l1 - t1)   # TypeError: unsupported operand type(s) for -: 'list' and 'tuple'
print(l1 * t1)   # TypeError: can't multiply sequence by non-int of type 'tuple'
print(l1 / t1)   # TypeError: unsupported operand type(s) for /: 'list' and 'tuple'
print(l1 // t1)  # TypeError: unsupported operand type(s) for //: 'list' and 'tuple'
print(l1 % t1)   # TypeError: unsupported operand type(s) for %: 'list' and 'tuple'
print(l1 ** t1)  # TypeError: unsupported operand type(s) for **: 'list' and 'tuple'

# list + set
l1 = [3,4,5,6,7,8]
s1 = {4,7,8,9,1,2}

print(l1 + s1)   # TypeError: can only concatenate list (not "set") to list
print(l1 - s1)   # TypeError: unsupported operand type(s) for -: 'list' and 'set'
print(l1 * s1)   # TypeError: can't multiply sequence by non-int of type 'set'
print(l1 / s1)   # TypeError: unsupported operand type(s) for /: 'list' and 'set'
print(l1 // s1)  # TypeError: unsupported operand type(s) for //: 'list' and 'set'
print(l1 % s1)   # TypeError: unsupported operand type(s) for %: 'list' and 'set'
print(l1 ** s1)  # TypeError: unsupported operand type(s) for **: 'list' and 'set'

# list + frozenset
l1 = [3,4,5,6,7,8]
s1 = {4,7,8,9,1,2}
fs = frozenset(s1)

print(l1 + fs)   # TypeError: can only concatenate list (not "frozenset") to list
print(l1 - fs)   # TypeError: unsupported operand type(s) for -: 'list' and 'frozenset'
print(l1 * fs)   # TypeError: can't multiply sequence by non-int of type 'frozenset'
print(l1 / fs)   # TypeError: unsupported operand type(s) for /: 'list' and 'frozenset'
print(l1 // fs)  # TypeError: unsupported operand type(s) for //: 'list' and 'frozenset'
print(l1 % fs)   # TypeError: unsupported operand type(s) for %: 'list' and 'frozenset'
print(l1 ** fs)  # TypeError: unsupported operand type(s) for **: 'list' and 'frozenset'

# list + dict
l1 = [3,4,5,6,7,8]
d1 = {4:7,8:9,1:2}

print(l1 + d1)   # TypeError: can only concatenate list (not "dict") to list
print(l1 - d1)   # TypeError: unsupported operand type(s) for -: 'list' and 'dict'
print(l1 * d1)   # TypeError: can't multiply sequence by non-int of type 'dict'
print(l1 / d1)   # TypeError: unsupported operand type(s) for /: 'list' and 'dict'
print(l1 // d1)  # TypeError: unsupported operand type(s) for //: 'list' and 'dict'
print(l1 % d1)   # TypeError: unsupported operand type(s) for %: 'list' and 'dict'
print(l1 ** d1)  # TypeError: unsupported operand type(s) for **: 'list' and 'dict'

# int + int 
a = 89
b = 45
print(a + b)   # 134
print(a - b)   # 44
print(a * b)   # 4005
print(a / b)   # 1.9777777777777779
print(a // b)  # 1
print(a % b)   # 44
print(a ** b)  # 115889228885477265973573640... (very large number)

# float + float
print(78.5 + 23.2)   # 101.7
print(78.5 - 23.2)   # 55.3
print(78.5 * 23.2)   # 1821.2
print(78.5 / 23.2)   # 3.3836206896551726
print(78.5 // 23.2)  # 3.0
print(78.5 % 23.2)   # 8.899999999999999
print(78.5 ** 23.2)  # 1.33e+43

# True + True
print(True + True)   # 2
print(True - True)   # 0
print(True * True)   # 1
print(True / True)   # 1.0
print(True // True)  # 1
print(True % True)   # 0
print(True ** True)  # 1

# False + False
print(False + False)   # 0
print(False - False)   # 0
print(False * False)   # 0
print(False / False)   # ZeroDivisionError
print(False // False)  # ZeroDivisionError
print(False % False)   # ZeroDivisionError
print(False ** False)  # 1

# complex + complex
print((2+3j) + (8+5j))   # (10+8j)
print((2+3j) - (8+5j))   # (-6-2j)
print((2+3j) * (8+5j))   # (1+34j)
print((2+3j) / (8+5j))   # (0.39622641509433965+0.1320754716981132j)
print((2+3j) // (8+5j))  # TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
print((2+3j) % (8+5j))   # TypeError: unsupported operand type(s) for %: 'complex' and 'complex'
print((2+3j) ** (8+5j))  # (complex result)

# string + string
s1 = "sakshi"
s2 = "jagtap"

print(s1 + s2)   # sakshijagtap
print(s1 - s2)   # TypeError
print(s1 * s2)   # TypeError
print(s1 / s2)   # TypeError
print(s1 // s2)  # TypeError
print(s1 % s2)   # TypeError
print(s1 ** s2)  # TypeError

# list + list
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

print(l1 + l2)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l1 - l2)   # TypeError: unsupported operand type(s) for -: 'list' and 'list'
print(l1 * l2)   # TypeError: can't multiply sequence by non-int of type 'list'
print(l1 / l2)   # TypeError: unsupported operand type(s) for /: 'list' and 'list'
print(l1 // l2)  # TypeError: unsupported operand type(s) for //: 'list' and 'list'
print(l1 % l2)   # TypeError: unsupported operand type(s) for %: 'list' and 'list'
print(l1 ** l2)  # TypeError: unsupported operand type(s) for **: 'list' and 'list'

# tuple + tuple
t1 = (5,9,3,2,7)
t2 = (4,7,2,9,4)

print(t1 + t2)   # (5, 9, 3, 2, 7, 4, 7, 2, 9, 4)
print(t1 - t2)   # TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
print(t1 * t2)   # TypeError: can't multiply sequence by non-int of type 'tuple'
print(t1 / t2)   # TypeError: unsupported operand type(s) for /: 'tuple' and 'tuple'
print(t1 // t2)  # TypeError: unsupported operand type(s) for //: 'tuple' and 'tuple'
print(t1 % t2)   # TypeError: unsupported operand type(s) for %: 'tuple' and 'tuple'
print(t1 ** t2)  # TypeError: unsupported operand type(s) for **: 'tuple' and 'tuple'

# set + set
s1 = {5,9,7,3,8,1}
s2 = {6,9,3,2,6,1}

print(s1 + s2)   # TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(s1 - s2)   # {8, 5, 7} - returns elements present in s1 but not in s2
print(s1 * s2)   # TypeError: unsupported operand type(s) for *: 'set' and 'set'
print(s1 / s2)   # TypeError: unsupported operand type(s) for /: 'set' and 'set'
print(s1 // s2)  # TypeError: unsupported operand type(s) for //: 'set' and 'set'
print(s1 % s2)   # TypeError: unsupported operand type(s) for %: 'set' and 'set'
print(s1 ** s2)  # TypeError: unsupported operand type(s) for **: 'set' and 'set'

# dict + dict
d1 = {1:"sakshi",2:"divya",3:"amruta"}
d2 = {1:8,3:6,5:2}

print(d1 + d2)   # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print(d1 - d2)   # TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
print(d1 * d2)   # TypeError: unsupported operand type(s) for *: 'dict' and 'dict'
print(d1 / d2)   # TypeError: unsupported operand type(s) for /: 'dict' and 'dict'
print(d1 // d2)  # TypeError: unsupported operand type(s) for //: 'dict' and 'dict'
print(d1 % d2)   # TypeError: unsupported operand type(s) for %: 'dict' and 'dict'
print(d1 ** d2)  # TypeError: unsupported operand type(s) for **: 'dict' and 'dict'

# frozenset + frozenset
f1 = {3,4,5,6,7,8}
f2 = {8,4,5,2,1,3}

fs1 = frozenset(f1)
fs2 = frozenset(f2)

print(fs1 + fs2)   # TypeError: unsupported operand type(s) for +: 'frozenset' and 'frozenset'
print(fs1 - fs2)   # frozenset({6, 7}) - returns elements present in fs1 but not in fs2
print(fs1 * fs2)   # TypeError
print(fs1 / fs2)   # TypeError
print(fs1 // fs2)  # TypeError
print(fs1 % fs2)   # TypeError
print(fs1 ** fs2)  # TypeError

'''
| Type                                | +  -  *  /  //  **  %            | 
| ----------------------------------- | -------------------------------- | 
| Numbers (int, float, bool, complex) | mostly yes                       | 
| list / tuple                        | only `+` with same type (concat) |   
| string                              | `+` (concat), '*' with string    |  
| set / frozenset                     | `-` allowed (diffrence)          |   
| dict                                | arithmetic operators not allowed |   
'''