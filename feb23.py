# reversing of words
str1 = "Welcome Python"
# op = "Python Welcome"

s = str1.split() # ['Welcome', 'Python']
print(s)

s.reverse() # ['Python', 'Welcome']
print(s)

op_str = " ".join(s)
print(op_str) # Python Welcome


# WAP  t check give string is palindrome or not 

str2 = "sakshi"

r_str = " "

for ch in str2 :
    r_str = ch + r_str
print(r_str) # ihskas 

if str2 == r_str :
    print("Palindrome")
else : 
    print("Not palindrome") # Not palindrome


# WAP to check give string is palindrome or not using indexing 
str3 = "ritik"

if str3 == str3[::-1] :
    print("Palindrome")
else : 
    print("Not palindrome")


# WAP  t check give string is palindrome or not for digit using string
num1 = 123

c_str1 = str(num1)
r_str = ""

for i in c_str1 :
    r_str = i + r_str

num = int(r_str)

if c_str1 == num:
    print("digit palindrome")
else : 
    print("not palindrome")


# WAP to check armstrong number

num2 = input("Enter the number :")
i_num2 = int(num2)
l_num2 = len(num2)
s_num2 = 0

for i in num2:
    s_num2 = s_num2 + int(i) ** l_num2

if(i_num2 == s_num2):
    print("armstrong number")
else:
    print("not armstrong")








