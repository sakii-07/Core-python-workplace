'''
None data type :- 
'''

'''
Operators :- used for data processing
            1) Arithmentic
            2) Relatonal(comparison)
            3) logical
            4) assignment
            5) bitwise
            6) special

1) Arithmentic opeartor in python :->
                + : add two or more numbers and returns the sum of the values.
                - : subtract one number from another and returns the difference between the values.
                * : multiply two numbers and returns the product of the values.
                / : divide one number by another and it always returns the result in float (decimal) form.
                //: divide two numbers and returns only the integer part of the result, removing the decimal part.
                % : return the reminder of devision
                **: raise a number to the power of another number.
    Note :
        division :- output of division opeartor is always in float
        eg. 6/3 = 2.0
        floor division :- output of floor division is always integer - integer part of q
                          use with range function
        eg. 10 // 3 = 3
        %(modulus) :- return the reminder of devision
        eg. 5 % 2 = 1
            6 % 2 = 0
'''

# division operator
print(10/3) # 3.3333333333333335

# floor division operator
print(10//3) # 3

s ="Instagram"
for i in range(len(s)//2):
    print(s[i])

# modulus operator
print(5%2) # 1
print(6%2) # 0

# find given number is even or odd using list 
l = [45,34,56,78,89,37,23,12,80,10]
even_list = []
odd_list = []
for i in l:
    result = i % 2
    if result == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list) # [34, 56, 78, 12, 80, 10]
print(odd_list) # [45, 89, 37, 23]





