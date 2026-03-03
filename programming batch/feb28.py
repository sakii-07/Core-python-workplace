# print patter for 5 by 5

# # outer loop for row
# for r in range (1,6):
#     # inner loop for column
#     for i in range (1,6):
#         print("*",end=" ")
#     print()

# # print patter for 10 by 6
# for a in range (1, 11):
#     for b in range (1,7):
#         print("*",end=" ")
#     print()

# # print patter for 6 by 3
# for a in range (1, 7):
#     for b in range (1,4):
#         print("*",end=" ")
#     print()

# # print patter for 5 by 5
# for a in range (1, 6):
#     for b in range (1,6):
#         print("*",end=" ")
#     print()

''' print :-
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
'''
# for i in range (1,6):
#     for r in range (1,6):
#         print(r,end=" ")
#     print()


''' print :-
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''
# for i in range (1,6):
#     for r in range (1,6):
#         print(i,end=" ")
#     print()

'''
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
'''
# for i in range (1,6):
#     for r in range (5,0,-1):
#         print(r,end=" ")
#     print()


'''
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''
# for i in range (1,6):
#     for r in range (5,0,-1):
#         print(i,end=" ")
#     print()

'''
5 5 5 5 5 
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
'''
# for i in range (5,0,-1):
#     for r in range (1,6):
#         print(i,end=" ")
#     print()

'''
 ord() - it will convert charcter to number or unicode or ascii value. 
        If the argument is a one-character string, return the Unicode code
        point of that character.
 '''
# t1 = '*'
# print(t1) # *
# a1 = ord(t1)
# print(a1) # 42

'''
chr() :- it converts number into character
         Return a Unicode string of one character
'''
# t2 = 97
# print(97) # 97
# a2 = chr(t2)
# print(a2) # a

# print(chr(101)) # e

# print(ord('A'))
'''
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
'''
# for i in range(1,6):
#     for r in range (65,70):
#         print(chr(r), end=" ")
#     print()

# ch1 = 'A'
# for i in range(1,6):
#     code = ord(ch1)
#     for r in range (1,6):
#         print(chr(code), end=" ")
#         code =code+1
#     print()

''' 7. 
a b c d e 
a b c d e
a b c d e
a b c d e
a b c d e
'''
# ch1 = 'a'
# for i in range (1,6):
#     code = ord(ch1)
#     for r in range (1,6):
#         print(chr(code),end=" ")
#         code = code + 1
#     print()

'''
a b c d e 
f g h i j
k l m n o
p q r s t
u v w x y
'''
# ch1 = 'a'
# code = ord(ch1)
# for i in range (1,6):
#     for r in range (1,6):
#         print(chr(code),end=" ")
#         code = code + 1
#     print()

'''
A A A A A 
B B B B B
C C C C C
D D D D D
E E E E E
'''
# ch1 = 'A'
# code = ord(ch1)
# for i in range(1,6):
#     for r in range(1,6):
#         print(chr(code),end=" ")
#     code = code + 1
#     print()


'''
E E E E E 
D D D D D
C C C C C
B B B B B
A A A A A
'''
# ch1 = 'E'
# code = ord(ch1)
# for i in range(1,6):
#     for r in range(1,6):
#         print(chr(code),end=" ")
#     code = code - 1
#     print()

'''
E D C B A 
E D C B A
E D C B A
E D C B A
E D C B A
'''
# ch1 = 'E'
# for i in range(1,6):
#     code = ord(ch1)
#     for r in range(1,6):
#         print(chr(code),end=" ")
#         code = code - 1
#     print()

'''
* * $ * * 
* * $ * *
* * $ * *
* * $ * *
* * $ * *
'''
# for r in range(1,6):
#     for c in range(1,6):
#         if c == 3:
#             print("$", end=" ")
#         else :
#             print("*", end=" ")
#     print()

'''
* * * * * 
* * * * *
$ $ $ $ $
* * * * *
* * * * *
'''
# for r in range(1,6):
#     for c in range (1,6):
#         if r == 3:
#             print("$", end=" ")
#         else:
#             print("*", end=" ")
#     print()

'''
* * $ * * 
* * $ * *
$ $ $ $ $
* * $ * *
* * $ * *
'''
# for r in range(1,6):
#     for c in range (1,6):
#         if r == 3 or c == 3:
#             print("$", end=" ")
#         else:
#             print("*", end=" ")
#     print()

'''
$ * * * $ 
$ * * * $
$ * * * $
$ * * * $
$ * * * $
'''
# for r in range(1,6):
#     for c in range (1,6):
#         if c == 1 or c == 5:
#             print("$", end=" ")
#         else:
#             print("*", end=" ")
#     print()

'''
$ $ $ $ $ 
* * * * *
* * * * *
* * * * *
$ $ $ $ $
'''
# for r in range(1,6):
#     for c in range (1,6):
#         if r == 1 or r == 5:
#             print("$", end=" ")
#         else:
#             print("*", end=" ")
#     print()

'''
$ $ $ $ $ 
$ * * * $
$ * * * $
$ * * * $
$ $ $ $ $
'''
# for r in range(1,6):
#     for c in range (1,6):
#         if c == 1 or c == 5 or r == 1 or r==5:
#             print("$", end=" ")
#         else:
#             print("*", end=" ")
#     print()

'''
$ * * * * 
* $ * * *
* * $ * *
* * * $ *
* * * * $
'''
# for r in range(1,6):
#     for c in range (1,6):
#         if c == r:
#             print("$", end=" ")
#         else:
#             print("*", end=" ")
#     print()

'''
* * * * $ 
* * * $ *
* * $ * *
* $ * * *
$ * * * *
'''
# for r in range(1,6):
#     i = 5
#     for c in range (1,6):
#         if r == i:
#             print("$", end=" ")
#         else:
#             print("*", end=" ")
#         i = i - 1
#     print()

'''
$ * * * $
* $ * $ *
* * $ * *
* $ * $ *
$ * * * $
'''
# for r in range(1,6):
#     i = 5
#     for c in range (1,6):
#         if c == r or r == i:
#             print("$", end=" ")
#         else:
#             print("*", end=" ")
#         i = i - 1
#     print()

# for r in range(1,6):
#     for c in range (1,6):
#         if c == r or r+c==6:
#             print("$", end=" ")
#         else:
#             print("*", end=" ")
#     print()

'''
* 
* *
* * *
* * * *
* * * * *
'''
# for r in range(1,6):
#     for c in range(1,r+1):
#         print("*",end=" ")
#     print()

'''
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
# for r in range(1,6):
#     for c in range(1,r+1):
#         print(c,end=" ")
#     print()


'''
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
# for r in range(1,6):
#     for c in range(1,r+1):
#         print(r,end=" ")
#     print()

'''
5 
4 4
3 3 3
2 2 2 2
1 1 1 1 1
'''
# for r in range(5,0,-1):
#     for c in range(5,r-1,-1):
#         print(r,end=" ")
#     print()

'''
5 
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''
# for r in range(5,0,-1):
#     for c in range(5,r-1,-1):
#         print(c,end=" ")
#     print()


'''
A 
A B
A B C
A B C D
A B C D E
'''
# ch1 = 'A'
# for r in range (1,6):
#     code = ord(ch1)
#     for c in range (1,r+1):
#         print(chr(code),end=" ")
#         code =code+1
#     print()

'''
A 
B B
C C C
D D D D
E E E E E
'''
# ch1 = 'A'
# code = ord(ch1)
# for r in range (1,6):
#     for c in range (1,r+1):
#         print(chr(code),end=" ")
#     code =code+1
#     print()

'''
E 
D D
C C C
B B B B
A A A A A
'''
# ch1 = 'E'
# code = ord(ch1)
# for r in range (5,0,-1):
#     for c in range (5,r-1,-1):
#         print(chr(code),end=" ")
#     code =code-1
#     print()

'''
E 
F F
G G G
H H H H
I I I I I
'''
# ch1 = 'E'
# code = ord(ch1)
# for r in range (5,0,-1):
#     for c in range (5,r-1,-1):
#         print(chr(code),end=" ")
#     code =code+1
#     print()

'''
E 
E D
E D C
E D C B
E D C B A
'''
# ch1 = 'E'
# for r in range (1,6):
#     code = ord(ch1)
#     for c in range (1,r+1):
#         print(chr(code),end=" ")
#         code =code-1
#     print()
'''
* * * * * 
* * * *
* * *
* *
*
'''
# for r in range(5,0,-1):
#     for c in range(1,r+1):
#         print("*",end=" ")
#     print()

'''
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
'''
# for r in range(5,0,-1):
#     for c in range(1,r+1):
#         print(c,end=" ")
#     print()

'''
5 5 5 5 5 
4 4 4 4
3 3 3
2 2
1
'''
# for r in range(5,0,-1):
#     for c in range(1,r+1):
#         print(r,end=" ")
#     print()

'''
A B C D E 
A B C D
A B C
A B
A
'''
# ch1 = 'A'
# for r in range(5,0,-1):
#     code = ord(ch1)
#     for c in range(1,r+1):
#         print(chr(code),end=" ")
#         code = code+1
#     print()

'''
A A A A A 
B B B B
C C C
D D
E
'''
# ch1 = 'A'
# code = ord(ch1)
# for r in range(5,0,-1):
#     for c in range(1,r+1):
#         print(chr(code),end=" ")
#     code = code+1
#     print()

'''
1 1 1 1 1 
2 2 2 2
3 3 3
4 4
5
'''
# # with third variable
# i =1
# for r in range(5,0,-1):
#     for c in range(1,r+1):
#         print(i,end=" ")
#     i = i+1
#     print()

# # without third variable
# for r in range(1,6):
#     for c in range(5,r-1,-1):
#         print(r,end=" ")
#     print()

'''
        * 
      * *
    * * *
  * * * *
* * * * *
'''
# sp = 5
# for r in range(1,6):
#     for k in range(1,(sp-r)+1):
#         print(" ",end=" ")
#     for c in range(1,r+1):
#         print("*",end=" ")
#     print()

'''
        1 
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
'''
# sp = 5
# for r in range(1,6):
#     for k in range(1,(sp-r)+1):
#         print(" ",end=" ")
#     for c in range(1,r+1):
#         print(c,end=" ")
#     print()

'''
        1 
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
'''
# sp = 5
# for r in range(1,6):
#     for k in range(1,(sp-r)+1):
#         print(" ",end=" ")
#     for c in range(1,r+1):
#         print(r,end=" ")
#     print()

'''
        A 
      A B
    A B C
  A B C D
A B C D E
'''
# sp = 5
# ch1 = 'A'
# for r in range(1,6):
#     code = ord(ch1)
#     for k in range(1,(sp-r)+1):
#         print(" ",end=" ")
#     for c in range(1,r+1):
#         print(chr(code),end=" ")
#         code = code+1
#     print()

'''
        A 
      B B
    C C C
  D D D D
E E E E E
'''
# sp = 5
# ch1 = 'A'
# code = ord(ch1)
# for r in range(1,6):
#     for k in range(1,(sp-r)+1):
#         print(" ",end=" ")
#     for c in range(1,r+1):
#         print(chr(code),end=" ")
#     code = code+1
#     print()

'''
    * 
   * *
  * * *
 * * * *
* * * * *
'''
# sp = 5
# for r in range(1,6):
#     for k in range(1,(sp-r)+1):
#         print(" ",end="")
#     for c in range(1,r+1):
#         print("*",end=" ")
#     print()

'''
    1 
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
'''
# sp = 5
# for r in range(1,6):
#     for k in range(1,(sp-r)+1):
#         print(" ",end="")
#     for c in range(1,r+1):
#         print(c,end=" ")
#     print()

'''
    A 
   A B
  A B C
 A B C D
A B C D E
'''
# sp = 5
# ch1 = 'A'
# for r in range(1,6):
#     code = ord(ch1)
#     for k in range(1,(sp-r)+1):
#         print(" ",end="")
#     for c in range(1,r+1):
#         print(chr(code),end=" ")
#         code = code + 1
#     print()

'''
* * * * * 
 * * * *
  * * *
   * *
    *
'''
# sp =5
# for r in range(5,0,-1):
#     for k in range(1,(sp-r)+1):
#         print(" ",end="")
#     for c in range(1,r+1):
#         print("*",end=" ")
#     print()

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
sp =5
for r in range(1,6):
    for k in range(1,(sp-r)+1):
        print(" ",end="")
    for c in range(1,r+1):
        print("*",end=" ")
    print()
for r in range(5,0,-1):
    for k in range(1,(sp-r)+1):
        print(" ",end="")
    for c in range(1,r+1):
        print("*",end=" ")
    print()