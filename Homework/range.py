'''
iterate tuple , list and string using range function.
'''

# Iterate Tuple

t = (1,2,3,4,5,"sakshi","Jagtap",2,3,4,5,6,7,8,9,1.3,5.23)
print(t) # (1, 2, 3, 4, 5, 'sakshi', 'Jagtap', 2, 3, 4, 5, 6, 7, 8, 9, 1.3, 5.23)
print(type(t)) # <class 'tuple'>
print(len(t)) # 17

# forword 
for i in range(len(t)):
    print(i,"--->",t[i] )
'''
0 ---> 1
1 ---> 2
2 ---> 3
3 ---> 4
4 ---> 5
5 ---> sakshi
6 ---> Jagtap
7 ---> 2
8 ---> 3
9 ---> 4
10 ---> 5
11 ---> 6
12 ---> 7
13 ---> 8
14 ---> 9
15 ---> 1.3
16 ---> 5.23
'''

# reverse
for i in range(17):
    print(len(t)-1-i,"---->",t[len(t)-1-i])

for i in range(len(t)-1, -1, -1):
    print(i,"---->",t[i])
'''
16 ----> 5.23
15 ----> 1.3
14 ----> 9
13 ----> 8
12 ----> 7
11 ----> 6
10 ----> 5
9 ----> 4
8 ----> 3
7 ----> 2
6 ----> Jagtap
5 ----> sakshi
4 ----> 5
3 ----> 4
2 ----> 3
1 ----> 2
0 ----> 1
'''

# Iterate list

l = [10,20,(1,2,3,4),"saki",20.23,[10,20,30],100]
print(l) # [10, 20, (1, 2, 3, 4), 'saki', 20.23, [10, 20, 30], 100]
print(type(l)) # <class 'list'>

# forword
for i in range(5):
    print(i,"--->",l[i])
'''
0 ---> 10
1 ---> 20
2 ---> (1, 2, 3, 4)
3 ---> saki
4 ---> 20.23
'''

for i in range(len(l)):
    print(i,"--->",l[i])
'''
0 ---> 10
1 ---> 20
2 ---> (1, 2, 3, 4)
3 ---> saki
4 ---> 20.23
5 ---> [10, 20, 30]
6 ---> 100
'''

# reverse
for i in range(len(l)):
    print(len(l)-1-i,"--->",l[len(l)-1-i])

for i in range(len(l)-1, -1, -1):
    print(i,"--->",l[i])
'''
6 ---> 100
5 ---> [10, 20, 30]
4 ---> 20.23
3 ---> saki
2 ---> (1, 2, 3, 4)
1 ---> 20
0 ---> 10
'''

# Iterate String

s = "I love python"
print(s) # I love python
print(type(s)) # <class 'str'>

# forwaord
for i in range(len(s)):
    print(i,"--->",s[i])
'''
0 ---> I
1 --->
2 ---> l
3 ---> o
4 ---> v
5 ---> e
6 --->
7 ---> p
8 ---> y
9 ---> t
10 ---> h
11 ---> o
12 ---> n
'''

# reverse
for i in range(len(s)-1, -1, -1):
    print(i,"--->",s[i])

for i in range(len(s)):
    print(len(s)-1-i,"--->",s[len(s)-1-i])
'''
12 ---> n
11 ---> o
10 ---> h
9 ---> t
8 ---> y
7 ---> p
6 --->
5 ---> e
4 ---> v
3 ---> o
2 ---> l
1 --->
0 ---> I
'''