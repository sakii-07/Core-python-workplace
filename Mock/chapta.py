# import random
# def chapta(num):
#     for i in range(1,num+1):
#         captcha = random.randint(1000, 9999)
#         print(captcha)

# # print("CAPTCHA: ")
# # chapta(10) 


# def randomString(num):
#     for i in range(1,num+1):
#         chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    
#         result = ""
        
#         for i in range(2):
#             result =result+ random.choice(chars)+str(random.randint(1,9))
            
#         print(result)

# # randomString(10)

try:
    a = 10
    b = a/0

except ZeroDivisionError as e:
    e = "num is 0"
    print(e )

# class numerror(Exception):
#     def __init__(self, msg):
#         self.msg

# num = 9
# try:
#     if num> 10:
#         raise numerror("Number must be greater than 10")

# except numerror as n:
#     print(n)
