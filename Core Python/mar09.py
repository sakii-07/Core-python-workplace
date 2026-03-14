'''
Opeartors :- 

    2) Relatonal(comparison) :-
                    1) > : Checks if the left value is greater than the right value.
                    2) < : Checks if the left value is less than the right value.
                    3) >= : Checks if the left value is greater than or equal to the right value.
                    4) >= : Checks if the left value is less than or equal to the right value.
            Equality operators:
                    1) == : check values of two variable is same or not - Checks whether two values are equal.
                    2) != : Checks whether two values are not equal.
        note : to compare LHS of equation to RHS
               comparison operator always returns boolean(True / False) value.

    3) logical :- used for logical operation on data
                    1) and :- If all the operand are true then and then only op is true.
                    2) or  :- If all the operand are flase then and then only op is false otherwise it always true.
                    3) not :- Inversion operator 

    4) Assignment :- 
                1) = :-assign the value to variable

        composite assignment :- Reuse the same variable
                1) += : Adds a value to the variable and assigns the result to the same variable. Example: a += 10 means a = a + 10.
                2) -= : Subtracts a value from the variable and assigns the result to the same variable. Example: a -= 5 means a = a - 5.
                3) *= : Multiplies the variable by a value and assigns the result to the same variable.Example: a *= 2 means a = a * 2.
                4) /= Divides the variable by a value and assigns the result to the same variable.Example: a /= 2 means a = a / 2.
                5) //= : Performs floor division on the variable and assigns the result to the same variable.Example: a //= 2 means a = a // 2.
                6) %= : Finds the remainder and assigns the result to the same variable.Example: a %= 3 means a = a % 3.
                7) **= : Raises the variable to a power and assigns the result to the same variable.Example: a **= 2 means a = a ** 2.

    5) Bitwise :-
                1) & : Compares the bits of two numbers and returns 1 if both bits are 1, otherwise 0.
                2) | : Compares the bits of two numbers and returns 1 if at least one bit is 1, otherwise 0.
                3) ~ : Inverts the bits of a number, changing 1 to 0 and 0 to 1.
                4) ^ -  ^ compares the binary (bits) of two numbers and returns 1 if bits are different, otherwise 0.
                        if both are same then op is false
                5) >> - Shifts the bits of a number to the right side by a specified number of positions. Formula: s >> r = s / 2^r  eg. 6 >> 2 - shift binary bits of 6 on roght side by two bits
                        if s>>r then use s/2^r
                6) << - Shifts the bits of a number to the left side by a specified number of positions. Formula: s << r = s * 2^r.

    6) Special :-
                1) is - Identity operator - checks memory address of variable is same or not
                2) in - membership operator - The in operator checks whether a value exists in a sequence such as a list, tuple, string, or dictionary.

    7) Ternary :- 
'''

# Example on logical operator 
a = True
b = False
print(a and b) # False

a = True
b = True
print(a and b) # True

a = False
b = False
print(a and b) # False

a = False
b = True
print(a and b) # False

# Example on bitwise operator
print(5 & 7) # 5

print(5 & 3) # 1

print(5 | 7) # 7

print(5 ^ 7) #  2

print(6 >> 2) # 1

print(3 << 2) # 12

# Example on special operator

print("I" in "Insta") # True
print(10 in [35,64,10]) # True

a = 123
b = 123
print(a == b) # True
print(id(a) == id(b)) # True
print(a is b) # True

a = -123
b = -123
print(a == b) # True
print(id(a) == id(b)) # True
print(id(a), id(b))
print(a is b) # True
