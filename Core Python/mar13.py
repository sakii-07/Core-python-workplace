'''
* 
* *
* * *
* * * *
* * * * *
'''
for r in range(1,6):
    print(end="\n") # it prints 5 empty lines

for r in range(1,6):
    for c in range(1,r+1):
        print("*",end=" ")
    print()

'''
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *
'''
n = 5
for r in range(1,n+1):
    for c in range(1,n+1):
        print("*",end=" ")
    print()

'''
* 
* *
* * *
* * * *
* * * * *
'''
n = 5
for r in range(1,n+1):
    for c in range(1,r+1):
        print("*",end=" ")
    print()

n = 5
for r in range(1,n+1):
        print("* "*r,end=" ")
        print()


'''
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
n = 5
for r in range(1,n+1):
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
n = 5
for r in range(1,n+1):
    for c in range(1,r+1):
        print(r,end=" ")
    print()

'''
* * * * * 
* * * *
* * *
* *
*
'''
n = 5
for r in range(n,0,-1):
    for c in range(1,r+1):
        print("*",end=" ")
    print()

'''
* * * * * 
*       *
*       *
*       *
* * * * *
'''
n = 5
for r in range(1,6):
    for c in range(1,6):
        if r==1 or c==1 or r==5 or c==5:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()

'''
*       * 
  *   *
    *
  *   *
*       *
'''
n = 5
for r in range(1,6):
    for c in range(1,6):
        if r+c == 6 or r == c:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()

'''
    * 
   * *
  * * *
 * * * *
* * * * *
'''
n = 5
sp = 5
for r in range(1,n+1):
    for k in range(1,(sp-r)+1):
        print(" ",end="")
    for c in range(1,r+1):
        print("*",end=" ")
    print()

n = 5
for r in range(1,n+1):
        print(" "*(n-r),"* "*r,end=" ")
        print()

'''
     * 
    **
   ***
  ****
 *****
'''
n = 5
for r in range(1,n+1):
        print(" "*(n-r),"*"*r,end=" ")
        print()