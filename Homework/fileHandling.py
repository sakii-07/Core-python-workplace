'''
homework
copy content of one file into another file
'''
def copy_file(src_file, dest_file):

    try:
    # open source file in read mode
        with open(src_file, "r") as src:
            data = src.read()

        # open destination file in write mode
        with open(dest_file, "w") as dest:
            dest.write(data)

        print("File copied successfully!")

    except Exception as e:
        print("Error occurred:", e)

# taking input from user
source = input("Enter source file path: ")
destination = input("Enter destination file path: ")

# passing arguments to function
copy_file(source, destination)
'''
Enter source file path: Homework/data.txt
Enter destination file path: Homework/copy_data1.txt
File copied successfully!
'''   