# String data type

s = "Instagram"
print(s) # print complete string
print(type(s))
print("Lengh of the given string ", len(s))

# print the element on specific index
print(s[0])
print(s[2]) 
print(s[-9])
print(s[-1])
print("s[len(s)-1] :",s[len(s)-1])
print("middle character",s[len(s)//2]) # middle character

# print(s[12]) # Throws error - IndexError: string index out of range
# print(s[-12])

# Task 1

# Accept any string from console
str = input("Enter the any string ")

# 1. display length of the string 
print("length of give string : ", len(str))

# 2. display first and last index of string
print("first index of given string : ", 0) # display first index
print("last index of given string using str[len(str)-1] : ", len(str)-1) # display last index

# 3. accept any index from user and display character present at that index
index = int(input("Enter index number : "))
print("Character index at given index : ", str[index])