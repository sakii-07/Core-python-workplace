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


import re

# match function 

pattern = "Python"
s = "Welcome to the world of Python programming. Python is a versatile language."
s2 = "jay,pavan;vijay|sanjay,kumar,Rajesh"

# match = re.match(pattern, s , re.IGNORECASE)
# if match:
#     print("Match found:", match.group())
# else:
#     print("No match found.")

# search function 
# search = re.search(pattern, s , re.IGNORECASE)
# if search:
#     print("Search found:", search.group())
# else:   
#      print("No search found.")

# findall function
# findall = re.findall(pattern, s , re.IGNORECASE)
# print("Findall found:", findall)

#sub function
# sub_string = re.sub(pattern, "JAVA", s , flags=re.IGNORECASE)
# print("Substitution found:", sub_string)

# split function

# pattern2 = r"[,;|]"

# split_string = re.split(pattern2, s2)
# print("Split found:", split_string)

# validate mobile number
# ^ - start of the string
# $ - end of the string
# \d - digit
# {10} - exactly 10 digits
# \w - word character (alphanumeric + underscore)
# * - zero or more occurrences
# + - one or more occurrences

# Mask first 6 digits of 10-digit mobile numbers in a string
# def mask_mobile_numbers(text):
#     # Regex to find 10-digit numbers
#     pattern = r"(\d{6})(\d{4})"
#     # Replace first 6 digits with ******
#     return re.sub(pattern, lambda m: '*'*6 + m.group(2), text)

# Example usage
# if __name__ == "__main__":
#     test_str = "Contact me at 9876543210 or 1234567890."
#     masked = mask_mobile_numbers(test_str)
#     print("Masked string:", masked)


# mobile = """my mobile number is 7876543210. my alternate number is 9876543210.
#             my office number is 1234567890."""

# # mobile_pattern = r"[6-9]\d{9}"
# pattern = r"(\d{4})(\d{6})"
# # mobile_numbers = re.findall(mobile_pattern, mobile)
# # print("Mobile numbers found:", mobile_numbers)

# # Mask 6 digits of mobile numbers


# masked_mobile = re.sub(pattern, lambda m:  m.group(1)+'*'*6, mobile)
# print("Original mobile string:", mobile)
# print("Masked mobile numbers:", masked_mobile)


# Email Validations using re 

email0 = "atul@thekiranacademy.com"
email1 = "atul123@thekiranacademy.com"
email2 = "@thekiranacademy.atulcom"
email3 = ".com@thekiranacademyatul"

# pattern = r"^[\w]+@+[\w]+\.[\w]{2,}$"

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


match = re.match(pattern,email3)

if match:
    print("Email is valid")

else:
    print("Invalid Email")