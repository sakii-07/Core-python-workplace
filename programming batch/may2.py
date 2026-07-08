''' Pattern '''

'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
for r in range(1,6):
    for c in range(1,6):
        print("*",end=" ")
    print()

'''
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
'''
for r in range(1,6):
    for c in range(1,6):
        print(c, end=" ")
    print()

'''
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
'''
for r in range(1,6):
    for c in range(5,0,-1):
        print(c,end=" ")
    print()

'''
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
'''
for r in range(1,6):
    for c in range(1,6):
        print(r,end=" ")
    print()

'''
5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1 
'''
for r in range(5,0,-1):
    for c in range(1,6):
        print(r,end=" ")
    print()

'''
* * $ * * 
* * $ * * 
* * $ * * 
* * $ * * 
* * $ * * 
'''
for r in range(1,6):
    for c in range(1,6):
        if c == 3:
            print("$", end=" ")
        else:
            print("*",end=" ")
    print()

'''
* * * * * 
* * * * * 
$ $ $ $ $ 
* * * * * 
* * * * * 
'''
for r in range(1,6):
    for c in range(1,6):
        if r == 3:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

'''
* * $ * * 
* * $ * * 
$ $ $ $ $ 
* * $ * * 
* * $ * *
'''
for r in range(1,6):
    for c in range(1,6):
        if r == 3 or c == 3:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

'''
* * * * * 
* * * * * 
* * $ * * 
* * * * * 
* * * * * 
'''
for r in range(1,6):
    for c in range(1,6):
        if r == 3 and c == 3:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

'''
$ * * * * 
* $ * * * 
* * $ * * 
* * * $ * 
* * * * $ 
'''
for r in range(1,6):
    for c in range(1,6):
        if r == c:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

'''
* * * * $ 
* * * $ * 
* * $ * * 
* $ * * * 
$ * * * * 
'''
# way - 1
for r in range(1,6):
    for c in range(1,6):
        if r+c == 6:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

# way - 2
k = 5
for r in range(1,6):
    for c in range(1,6):
        if c == k:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()
    k -= 1

# way - 3
for r in range(1,6):
    for c in range(5,0,-1):
        if r == c:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

# way - 4
for r in range(5,0,-1):
    for c in range(1,6):
        if r == c:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

'''
$ * * * $ 
* $ * $ * 
* * $ * * 
* $ * $ * 
$ * * * $
'''
for r in range(1,6):
    for c in range(1,6):
        if r+c == 6 or r == c:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

'''
$ $ $ $ $ 
* * * * * 
* * * * * 
* * * * * 
$ $ $ $ $ 
'''
for r in range(1,6):
    for c in range(1,6):
        if r == 1 or r == 5:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

'''
$ $ $ $ $ 
$ * * * $ 
$ * * * $ 
$ * * * $ 
$ $ $ $ $ 
'''
for r in range(1,6):
    for c in range(1,6):
        if r == 1 or r == 5 or c ==1 or c == 5:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

c = chr(871)
print(c)

o = ord("%")
print(o)

'''
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E
'''
ch = 'A'
for r in range(1,6):
    code = ord(ch)
    for c in range(1,6):
        print(chr(code),end=" ")
        code += 1
    print()

'''
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E
'''
ch = 'A'
code =  ord(ch)
for r in range(1,6):
    for c in range(1,6):
        print(chr(code),end=" ")
    code += 1
    print()

'''
E D C B A 
E D C B A 
E D C B A 
E D C B A 
E D C B A
'''
ch = 'E'
for r in range(1,6):
    code = ord(ch)
    for c in range(1,6):
        print(chr(code), end=" ")
        code -= 1
    print()

'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
for r in range(1,6):
    for c in range(1,r+1):
        print("*",end=" ")
    print()

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
for r in range(1,6):
    for c in range(1,r+1):
        print(c,end=" ")
    print()

'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''
for r in range(1,6):
    for c in range(1,r+1):
        print(r,end=" ")
    print()

'''
A 
A B 
A B C 
A B C D 
A B C D E 
'''
ch = 'A'
for r in range(1,6):
    code = ord(ch)
    for c in range(1,r+1):
        print(chr(code),end=" ")
        code += 1
    print()

'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
sp = 5
for r in range(1,6):
    for c in range(1,(sp-r)+1):
        print(" ",end=" ")
    for k in range(1,r+1):
        print("*",end=" ")
    print()

'''
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
'''
sp = 5
for r in range(1,6):
    for c in range(1,(sp-r)+1):
        print(" ",end=" ")
    for k in range(1,r+1):
        print(k,end=" ")
    print()

'''
        A 
      A B 
    A B C 
  A B C D 
A B C D E 
'''
ch = 'A'
sp = 5
for r in range(1,6):
    code = ord(ch)
    for c in range(1,(sp-r)+1):
        print(" ",end=" ")
    for k in range(1,r+1):
        print(chr(code),end=" ")
        code += 1
    print()

'''
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5 
'''
sp = 5
for r in range(1,6):
    for c in range(1,(sp-r)+1):
        print(" ",end=" ")
    for k in range(1,r+1):
        print(r, end=" ")
    print()

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''
for r in range(5,0,-1):
    for c in range(1,r+1):
        print("*",end=" ")
    print()

sp = 6
for r in range(1,6):
    print("* "*(sp-r))

'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
for r in range(5,0,-1):
    for c in range(1,r+1):
        print(c,end=" ")
    print()

'''
A B C D E 
A B C D 
A B C 
A B 
A 
'''
ch = 'A'
for r in range(5,0,-1):
    code = ord(ch)
    for c in range(1,r+1):
        print(chr(code),end=" ")
        code += 1
    print()

'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
sp = 5
for r in range(1,6):
    for c in range(1,(sp-r)+1):
        print("",end=" ")
    for d in range(1,r+1):
        print("*",end=" ")
    print()

'''
    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5
'''
sp = 5
for r in range(1,6):
    for c in range(1,(sp-r)+1):
        print("",end=" ")
    for d in range(1,r+1):
        print(d,end=" ")
    print()

'''
    A 
   A B 
  A B C 
 A B C D 
A B C D E 
'''
ch = 'A'
sp = 5
for r in range(1,6):
    code = ord(ch)
    for c in range(1,(sp-r)+1):
        print("",end=" ")
    for k in range(1,r+1):
        print(chr(code),end=" ")
        code += 1
    print()

'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''
sp = 0
for r in range(5,0,-1):
    for c in range(1,sp+1):
        print("",end=" ")
    for d in range(1,r+1):
        print("*",end=" ")
    sp += 1
    print()

'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''
n = 5
# Upper part
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

# Lower part
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)