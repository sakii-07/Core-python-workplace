# '''
# re module ----> Validation, matching, pattern

# 1) match function --> 
#         re.I - Engonre case
#         match.group()
# 2) re.search(path,s,re.I) --  search.group
# 3) re.find()
# '''
import re

# pattern = 'Welcome'
# s = "Welcome to the world of python programming"

# # match function
# match = re.match(pattern,s,re.I)
# if match:
#     print("Match found : ",match.group())
# else:
#     print("No match found")

# # search function
# search = re.search(pattern,s,re.IGNORECASE)
# if search:
#     print("Search found : ", search.group())
# else:
#     print("No match found")

# # findAll function
# findAll = re.findall(pattern),s,re.IGNORECASE
# print("FindAll found : ", findAll)

# # sub function
# pattern = "Python"
# sub_string = re.sub(pattern,"Java",s,flags=re.IGNORECASE)
# print("Substitution found : ",sub_string)

# s2 = ['jay','vijay'|'sakshi','amruta','harsh';'mauli']
# pattern2 = [";,|"]

# split_string = re.split(pattern2,s2)
# print("Split found : ",split_string)

# validate mobile number
# ^ - start of string
# $ - end of the string
# \d - digit
# {10} - exactly 10 digit
# \w - word character (alphanumric + underscore)
# * - zero or more occurances
# + - one or more occurances

# mobile = "my mobile number is 7895643210. my alternate number is 9087654321. my office number is 1234567890."

# mobile_pattern = r"[6-9]\d{9}"

# mobile_number = re.findall(mobile_pattern,mobile)
# print("Mobile number found : ",mobile_number) # Mobile number found :  ['7895643210', '9087654321']

# # Mask 6 digits of mobile number
# pattern = r"\b\d{6}(\d{4})\b"
# masked_mobile = re.sub(pattern, lambda m: '*'*6+m.group(1),mobile)
# print("Original mobile string : ", mobile)
# print("Masked mobile number : ", masked_mobile)
# '''
# Original mobile string :  my mobile number is 7895643210. my alternate number is 9087654321. my office number is 1234567890.
# Masked mobile number :  my mobile number is ******3210. my alternate number is ******4321. my office number is ******7890.
# '''

# Email validation using re
email0 = "sakshi@gmail.com"
email1 = "@sakshijagtap.dailcom"
pattern = r"^[\w]+@+[\w]+\.+[\w]{2,}$"

match = re.match(pattern , email1)

if match:
    print("Email is valid")
else:
    print("Invalid email")
