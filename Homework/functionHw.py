#  ##  User Define Function ##
# 1. Write a function to find the maximum number in a list.
def maxNum(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
n = maxNum(20,50)
print(n) # 50

# 2. Write a function that returns the sum of all elements in a list.
def sumNum(a,b):
    return a+b
from functools import reduce
l1 = [1,2,3,4,5,6,7,8,9]
sum = reduce(sumNum,l1)
print(sum) # 45

# 3. Create a function to reverse a list.
def rev(s):
    s_rev = ""
    for i in s:
        s_rev = i + s_rev
    return s_rev

revs = rev("Sakshi")
print(revs) # ihskaS

# 4. Write a function that checks if an element exists in a list.
def chechElement(a):
    l1 = [1,2,3,4,5,6,7,8,9,10]
    for i in l1:
        if i in l1:
            return True
        else:
            return False
print(chechElement(3)) # True

# 5. Write a function to remove duplicates from a list.
def removeDulpicates(l1):
    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2
r = removeDulpicates([21,32,12,1,2,1,2,1,4,2,1])
print(r) # [21, 32, 12, 1, 2, 4]
        
 
# 6. Write a function to count occurrences of each item in a list.
def occurrences(a):
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d
o = occurrences([1,2,3,1,3,4,5,2,3,1])
print(o) # {1: 3, 2: 2, 3: 3, 4: 1, 5: 1}
 

# 7. Write a function that accepts a list and returns a list with only even numbers.
def evenNum(l):
    l1 = []
    for i in l:
        if i%2==0:
            l1.append(i)
    return l1
l = evenNum([1,2,3,45,5,6,1,2,1,3])

# 8. Write a function that returns unique elements from a list using sets.
def uniqueElements(l1):
    s = set(l1)
    return s
unique = removeDulpicates([21,32,12,1,2,1,2,1,4,2,1])
print(unique) # [21, 32, 12, 1, 2, 4]

# 9. Write a function that finds common elements between two lists.
def commanElements(l1,l2):
    comman = []
    for item in l1:
        if item in l2 and item not in comman:
            comman.append(item)
    return comman
comman = commanElements([1,4,7,8,2,9],[2,6,5,4,8,9,3])
print(comman) # [4, 8, 2, 9]

# 10. Write a function to check if a number is prime.
def isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
       
    return True
print(isPrime(70)) # False

# 11. Write a function to find factorial of a number.
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
fact = factorial(5)
print(fact) # 120

# 12. Write a function that counts words of length greater than 3 in a sentence.
def wordCount(s):
    s1 = s.split(" ")
    # print(s1) # ['i', 'love', 'python', 'programming', 'and', 'to', 'write', 'a', 'code']
    count = 0
    for i in s1:
        if len(i) >= 3:
            count += 1
    return count
s = "i love python programming and to write a code"
count = wordCount(s)
print(count) # 6


       ## Nested Function ##

# 1. Write a Python function that defines an inner function to compute the square of a number, and returns the result from the outer function.
def outer(num):
    def square(num):
        return num*num
    return square(num)
square = outer(9)
print(square)

# 2. Create a nested function where the inner function checks if a number is even or odd, and the outer function takes the number as input.
def outer(num):
    def inner(num):
        if num%2==0:
            return "Even"
        else:
            return "Odd"
    return inner(num)
num = outer(46)
print(num) # Even

# 3. Write a function that defines another function to convert temperature from Celsius to Fahrenheit, and returns the converted value.
def outer(cal):
    def convert(temp):
        return (temp * 9/5) + 32
    return convert(cal)
print(outer(30))

# 4. Create an outer function that accepts a list and has an inner function to calculate the sum of even numbers from the list.
def outer(l):
    def sumOfEvenNum(l1):
        sum = 0
        for i in l1:
            if i%2==0:
                sum += i
        return sum
    return sumOfEvenNum(l)

sum = outer([1,2,3,4,5,6,7,8,9])
print(sum) # 20

# 5. Write a program where the outer function takes a string, and the inner function counts the number of vowels in that string.
def outer(s):
    def inner(s):
        count = 0
        for char in s:
            if char in 'aeiou':
                count += 1
        return count
    return inner(s)
print(outer("Sakshi")) # 2

# 6. Make a nested function that returns the factorial of a number  the inner function.
def outer(num):
    def factorial(num):
        fact = 1
        for i in range(1,num+1):
            fact *= i
        return fact
    return factorial(num)
print(outer(5)) # 120

# 7. Create a function that contains another function to reverse a string, and print both original and reversed versions.
def outer(text):
    def reverse(text):
        r_text = ""
        for char in text:
            r_text = char + r_text
        return r_text
    
    rev = reverse(text)
    print("Original String : ", text)
    print("Reversed String : ",rev)

outer("Sakshi")
'''
Original String :  Sakshi
Reversed String :  ihskaS
'''

# 8. Build a function where the inner function finds the maximum element of a list, and the outer function calls it.
def outer(l):
    def maxElement(l1):
        max = l1[0]
        for i in l1:
            if max < i:
                max = i
        return max
    return maxElement(l)
maxElement = outer([1,3,95,6,7,8,90])
print(maxElement) # 95
            
# 9. Implement a nested function that checks if a string is a palindrome inside the outer function.
def outer(s):
    def isPalindrome(s):
        rev_string = ""
        for char in s:
            rev_string = char + rev_string
        if s == rev_string:
            return True
        return False
    return isPalindrome(s)
print(outer('nayan')) # True