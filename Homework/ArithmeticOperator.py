# note / table 

'''    int+int  float+float  True+True  list+list  tuple+tuple  set+set  dict+dict  string+String  False+False  complex+complex  fs+fs
+       yes         yes         yes        yes         yes        no       no           yes            yes            yes          no
-       yes         yes         yes        no          no         yes      no           no             yes            yes          yes
*       yes         yes         yes        no          no         no       no           no             yes            yes          no
/       yes         yes         yes        no          no         no       no           no             no             yes          no     
//      yes         yes         yes        no          no         no       no           no             no             no           no


    int+float  int+True  int+False  int+complex  int+string  int+list  int+tuple  int+set int+fs  int+dict
+      yes       yes        yes         yes         no          no        no        no      no      no
-      yes       yes        yes         yes         no          no        no        no      no      no
*      yes       yes        yes         yes         yes         yes       yes       no      no      no
/      yes       yes        no          yes         no          no        no        no      no      no
//     yes       yes        no          no          no          no        no        no      no      no



    float+int  float+True  float+False  float+complex  float+string  float+list  float+tuple  float+set float+fs  float+dict
+      yes       yes           yes         yes              no           no           no          no        no        no
-      yes       yes           yes         yes              no           no           no          no        no        no
*      yes       yes           yes         yes              no           no           no          no        no        no
/      yes       yes           no          yes              no           no           no          no        no        no
//     yes       yes           no          no               no           no           no          no        no        no


    list+tuple  list+set  list+fs  list+dict  tuple+set  tuple+fs  tuple+dict  set+fs  set+dict  fs+dict   
+       no         no       no        no          no        no         no        no       no        no
-       no         no       no        no          no        no         no        no       no        no
*       no         no       no        no          no        no         no        no       no        no
/       no         no       no        no          no        no         no        no       no        no
//      no         no       no        no          no        no         no        no       no        no

'''
# list + set
l1 = [3,4,5,6,7,8]
d1 = {4:7,8:9,1:2}
print(l1 + d1) # TypeError: can only concatenate list (not "dict") to list
print(l1 - d1) # TypeError: unsupported operand type(s) for -: 'list' and 'dict'
print(l1 * d1) # TypeError: can't multiply sequence by non-int of type 'dict'
print(l1 / d1) # TypeError: unsupported operand type(s) for /: 'list' and 'dict'
print(l1 // d1) # TypeError: unsupported operand type(s) for //: 'list' and 'dict'

# list + fs
l1 = [3,4,5,6,7,8]
s1 = {4,7,8,9,1,2}
fs = frozenset(s1)
print(l1 + fs) # TypeError: can only concatenate list (not "frozenset") to list
print(l1 - fs) # TypeError: unsupported operand type(s) for -: 'list' and 'frozenset'
print(l1 * fs) # TypeError: can't multiply sequence by non-int of type 'frozenset'
print(l1 / fs) # TypeError: unsupported operand type(s) for /: 'list' and 'frozenset'
print(l1 // fs) # TypeError: unsupported operand type(s) for //: 'list' and 'frozenset'

# list + set
l1 = [3,4,5,6,7,8]
s1 = {4,7,8,9,1,2}
print(l1 + s1) # TypeError: can only concatenate list (not "set") to list
print(l1 - s1) # TypeError: unsupported operand type(s) for -: 'list' and 'set'
print(l1 * s1) # TypeError: can't multiply sequence by non-int of type 'set'
print(l1 / s1) # TypeError: unsupported operand type(s) for /: 'list' and 'set'
print(l1 // s1) # TypeError: unsupported operand type(s) for //: 'list' and 'set'

# list + tuple
l1 = [3,4,5,6,7,8]
t1 = (4,7,8,9,1,2)
print(l1 + t1) # TypeError: can only concatenate list (not "tuple") to list
print(l1 - t1) # TypeError: unsupported operand type(s) for -: 'list' and 'tuple'
print(l1 * t1) # TypeError: can't multiply sequence by non-int of type 'tuple'
print(l1 / t1) # TypeError: unsupported operand type(s) for /: 'list' and 'tuple'
print(l1 // t1) # TypeError: unsupported operand type(s) for //: 'list' and 'tuple'

# float + string
print(34.12 * "sakshi")

# int + dict
d1 = {2:5,6:4,8:9}
print(5 + d1) # TypeError: unsupported operand type(s) for +: 'int' and 'dict'
print(5 - d1) # TypeError: unsupported operand type(s) for -: 'int' and 'dict'
print(5 * d1) # TypeError: unsupported operand type(s) for *: 'int' and 'dict'
print(5 / d1) # TypeError: unsupported operand type(s) for /: 'int' and 'dict'
print(5 // d1) # TypeError: unsupported operand type(s) for //: 'int' and 'dict'

# int + fs
s1 = {2,5,6,4,8,9}
fs = frozenset(s1) 
print(3 + fs) # TypeError: unsupported operand type(s) for +: 'int' and 'frozenset'
print(3 - fs) # TypeError: unsupported operand type(s) for -: 'int' and 'frozenset'
print(3 * fs) # TypeError: unsupported operand type(s) for *: 'int' and 'frozenset'
print(3 / fs) # TypeError: unsupported operand type(s) for /: 'int' and 'frozenset'
print(3 // fs) # TypeError: unsupported operand type(s) for //: 'int' and 'frozenset'

# int + set
s1 = {2,5,6,4,8,9}
print(4 + s1) # TypeError: unsupported operand type(s) for +: 'int' and 'set'
print(4 - s1) # TypeError: unsupported operand type(s) for -: 'int' and 'set'
print(4 * s1) # TypeError: unsupported operand type(s) for *: 'int' and 'set'
print(4 / s1) # TypeError: unsupported operand type(s) for /: 'int' and 'set'
print(4 // s1) # TypeError: unsupported operand type(s) for //: 'int' and 'set'

# int + tuple
t1 = (3,5,8,5,9,2,1)
print(32 + t1) # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
print(32 - t1) # TypeError: unsupported operand type(s) for -: 'int' and 'tuple'
print(2 * t1) # (3, 5, 8, 5, 9, 2, 1, 3, 5, 8, 5, 9, 2, 1)
print(32 / t1) # TypeError: unsupported operand type(s) for /: 'int' and 'tuple'
print(32 // t1) # TypeError: unsupported operand type(s) for //: 'int' and 'tuple'


# int + list
l1 = [5,4,3,6,7,9,1]
print(12 + l1) # TypeError: unsupported operand type(s) for +: 'int' and 'list'
print(12 - l1) # TypeError: unsupported operand type(s) for -: 'int' and 'list'
print(12 * l1) # [5, 4, 3, 6, 7, 9, 1, 5, 4, 3, 6, 7, 9, 1, 5, 4, 3, 6, 7, 9, 1, 5, 4, 3, 6, 7, 9, 1, 5, 4, 3, 6, 7, 9, 1, 5, 4, 3, 6, 7, 9, 1, 5, 4, 3, 6, 7, 9, 1, 5, 4, 3, 6, 7, 9, 1, 5, 4, 3, 6, 7, 9, 1, 5, 4, 3, 6, 7, 9, 1, 5, 4, 3, 6, 7, 9, 1, 5, 4, 3, 6, 7, 9, 1]
print(12 / l1) # TypeError: unsupported operand type(s) for /: 'int' and 'list'
print(12 // l1) # TypeError: unsupported operand type(s) for //: 'int' and 'list'

# int + string
print(78 + "sakshi") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(78 - "sakshi") # TypeError: unsupported operand type(s) for -: 'int' and 'str'
print(78 * "sakshi") # sakshisakshisakshisakshisakshisakshi
print(78 / "sakshi") # TypeError: unsupported operand type(s) for /: 'int' and 'str'
print(78 // "sakshi") # TypeError: unsupported operand type(s) for //: 'int' and 'str'

# int + complex
print(23 + (2+9j)) # (25+9j)
print(23 - (2+9j)) # (21-9j)
print(23 * (2+9j)) # (46+207j)
print(23 / (2+9j)) # (0.5411764705882353-2.4352941176470586j)
print(23 // (2+9j)) # TypeError: unsupported operand type(s) for //: 'int' and 'complex'

# int + Flase
print(34 + False ) # 34
print(34 - False ) # 34
print(34 * False ) # 0
print(34 / False ) # ZeroDivisionError: division by zero
print(34 // False ) # # ZeroDivisionError: division by zero

# int + True
print(34 // True ) # 34 

# int + float
print(34 // 17.56) # 1.0

# frozen set+frozen set
f1 = {3,4,5,6,7,8}
f2 = {8,4,5,2,1,3}
fs1 = frozenset(f1)
fs2 = frozenset(f2)
print(fs1 // fs2)

# complex + complex
print((2+3j) // (8+5j))

# False + False
print(False // False)

# string + string
s1 = "sakshi"
s2 = "jagtap"
print(s1 // s2)

# dict + dict
d1 = {1:"sakshi",2:"divya",3:"amruta"}
d2 = {1:8,3:6,5:2}
print(d1 // d2)

# set + set
s1 = {5,9,7,3,8,1}
s2 = {6,9,3,2,6,1}
print(s1 // s2)

# tuple + tuple
t1 = (5,9,3,2,7)
t2 = (4,7,2,9,4)
print(t1 // t2)

# list + list
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
print(l1 // l2)

# True + True
print(True//True)

# int + int
print(89+45)

# float + float
print(78.5//23.2)