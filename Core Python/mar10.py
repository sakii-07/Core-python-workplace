'''
Flow control statments ----> 
                    1) conditional statement
                                1) if
                                2) if - else
                                3) if-elif-else
                    2) Iterative statement
                                1) for loop
                                2) while loop
                    3) transfer statement
                                1) pass
                                2) break
                                3) continue

                                
1) conditional statement
                 1) if - used to check half condition
                        syntax - if conditon:    ----> operators : comparision, logical, special
                                    block code (statements)

                 2) if - else : To check complete condition or one full condition
                        syntax : if condition :         ----> if condition is true then if body executes
                                     body of if
                                 else :                 ----> if condition is false then else body executes
                                     body of else

                 3) if-elif-else : To check multiple conditions 
                        syntax : if cond1:
                                    statements
                                 elif cond2:
                                    statemnts
                                 elif condN:
                                    statements
                                 else:
                                    statements
'''

# WAP to print given number is even or odd
num = -12
if num % 2 == 0 :
    print(F"Given number : {num} is even")
else:
    print(F"Given number : {num} is odd")

# you have a number if the number is divisible by 3 display "FIZZ"
# if the number is divisible by 5 display "BUZZ"
# if the number is divisible by 3 and 5 both display "FIZZBUZZ"

num = 16
if (num % 3 == 0) and (num % 5 == 0):
    print("FIZZBUZZ")
elif num % 3 == 0 :
    print("FIZZ")
elif num % 5 == 0 :
    print("BUZZ")
else:
    print("not divisible by 3 and 5")








