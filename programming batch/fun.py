num = [1,2,3,4,5,6]

square_list = list(map(lambda x:x**2,num))
print("Square list : ",square_list)

even_numbers = list(filter(lambda x: x%2==0,num))
print("Even numbers : ",even_numbers)

from functools import reduce
total = reduce(lambda x,y:x+y,num)
print("Total : ",total)

# recursion
def factorial(n):

    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
fact = factorial(5)
print("Factorial",fact)