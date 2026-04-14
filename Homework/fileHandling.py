'''
homework
copy content of one file into another file
'''
try:
    # open source file in read mode
    with open("Homework/data.txt", "r") as src:
        data = src.read()

    # open destination file in write mode
    with open("Homework/data_copy.txt", "w") as dest:
        dest.write(data)

    print("File copied successfully!")

except Exception as e:
    print("Error occurred:", e)

    