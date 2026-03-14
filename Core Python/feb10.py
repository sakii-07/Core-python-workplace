# Binary representation of any number use 0b or 0B
v = 0b0110
print(v) # gives decimal number
print(type(v))

# Octal reprentation of any number
num = 0o1231
print(num) # gives decimal number
print(type(num))

# hexadecimal numbers
a = 0xFace
print(a) # gives decimal number
print(type(a))

# conversion - build in functions

d = 19
r1 = bin(d)
# print(r1) # 0b10011
print(type(r1)) # <class 'str'>

r2 = oct(d)
print(r2) # 0o23

r3 = hex(d)
print(r3) # 0x13

r4 = bin(6) # 0b110
print(r1 + r4) # 0b100110b110 (concat the r1 and r4)

# int()
i1 = int("0b1",2)
i2 = int("0b0110",2)
i3 = i1 + i2
r5 = bin(i3)
print(r5) # 0b111

# complex(real part, complex part) 
c4 = complex(0o1234, 0xFace)
print(c4) # (668+64206j)

# Homework
# 1.accept decimal numbers from console and convert that into binary,ocat,hexadecimal number system and display back on terminal
num = int(input("Enter the any decimal number "))
# Binary conversion
r1 = bin(num)
print("binary : ",r1)

# Octal conversion
r2 = oct(num)
print("Octal : ",r2)

# Hexadecimal conversion
r3 = hex(num)
print("Hexadecimal : ",r3)


# 2. accept binary, octal or hexadecimal and conver it into decimal number display on terminal 
number = input("Enter the any binary, octal or hexadecimal number (with 0b, 0o, 0x) : ")
base = int(input("Enter the base for binary 2, octal 8, hexadecimal 16 : "))
decimal = int(number,base)
print("Decimal number is : ",decimal)