# f1 = input("Which file we want to copy : ")
# new_file = f1.split('.')[0] + "_copy.txt"
# with open(f1,'r') as file1, open(f1.replace(".txt","_copy.txt"),'w') as file2:
#     data = file1.read()
#     file2.write(data)
#     print(f"Data copied into {new_file}")

f1 = input("Which file want to process : ")
word = input("Which word want to count : ")
with open(f1,'r') as file1:
    data = file1.read()
    # print(type(data))
print(data.count(word))
    