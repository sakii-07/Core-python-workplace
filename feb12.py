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

print(s[12]) # Throws error - IndexError: string index out of range
print(s[-12])