'''
File handling in python ----> text and binary(images, video, pdf, audio) files

purpose -->

i) text file --> modes of file
                    1) x  --  create a new file if file already exist then give FileExistsError
                    2) r  --  (read) to read data from file
                            Note : for the read mode file must be present if file is not present then 
                            gives one exception FileNotFound

                        methods ---> 1) read() : It will read all file at a time
                                     2) readline() : Read first line from a file
                                     3) readlines() : Read all lines from a file and return list of lines
                    3) w  --  to write data into file
                            Note : File may present or not if not present it will create new file then write

                            It will override file
                              
                              methods --> 1) write()
                                          2) writelines()

                    4) a  --  (Append) To write date into file
                                Note : File may present or not if not present it will create new file then write
                                       It will add data at the endof file

                    5) r+  --  Read data first and then write

                    6) w+  --  First write data and then read

                    6) a+  --  First append data and then read

ii) Binary files --> for binary files (images, video, pdf, audio) also all modes are same
                        rb,wb,ab,rb+,wb+,ab+
'''
# fd = open("filename.txt", mode="?")

# 1) read() : It will read all file at a time
# data = fd.read()
# for i in data:
#     print(i)

# Example
# try:
#     fd = open("data.txt","r")
#     data = fd.read()

# except FileNotFoundError:
#     print("File not found")
# else:
#     print("File opend successfully")
#     print(data)
# finally:
#     # if 'fd' in locals():
#       fd.close()
#     print("File closed")
# '''
# File opend successfully
# 1,sakshi,89
# 2,sojar,78
# 3,pranjali,68
# File closed
# File opend successfully'''

# read first % characters from files
# data = fd.read(5)
# for i in data:
#     print(i)

# Example
# try:
#     fd = open("data.txt","r")
#     line = fd.read(5)

# except FileNotFoundError:
#     print("File not found")
# else:
#     print("File opend successfully")
#     print(line)
# finally:
#     if 'fd' in locals():
#       fd.close()
#     print("File closed")
# '''
# File opend successfully
# 1,sak
# File closed
# '''
# 2) readline() : Read first line from a file
# data = fd.readline()

# Example
# try:
#     fd = open("data.txt","r")
#     line = fd.readline()

# except FileNotFoundError:
#     print("File not found")
# else:
#     print("File opend successfully")
#     print(line)
# finally:
#     # if 'fd' in locals():
#       fd.close()
#     print("File closed")
# '''
# File opend successfully
# 1,sakshi,89

# File closed
# '''

# 3) readlines() : Read all lines from a file and return list of lines
# lines_list = fd.readlines()

# Example
# try:
#     fd = open("data.txt","r")
#     lines = fd.readlines()

# except FileNotFoundError:
#     print("File not found")
# else:
#     print("File opend successfully")
#     for line in lines:
#         roll,name,marks = line.strip().split(",")
#         print(f"rollNumber : {roll}, name : {name}, marks : {marks}")
# finally:
#     print("This Block always execute")
#     if 'fd' in locals():
#         fd.close()
#     print("File closed")
# '''
# File opend successfully
# rollNumber : 1, name : sakshi, marks : 89
# rollNumber : 2, name : sojar, marks : 78
# rollNumber : 3, name : pranjali, marks : 68
# This Block always execute
# File closed    
# '''
# import os
# print(os.getcwd)

# write operation
try:
    with open("data123.txt","w") as fd:
        fd.write("Atual sir \n")
        # fd.write("This is a test file. \n")
        # fd.write("This is used for test file\n")
        # fd.write("Atual sir \n")
except Exception as e:
    print("Error occurred:", e)

# append operation
try:
    with open("data123.txt","a") as fd:
        fd.write("Atual sir \n")
        fd.write("This is a test file. \n")
        fd.write("This is used for test file\n")
        fd.write("Atual sir \n")
except Exception as e:
    print("Error occurred:", e)

