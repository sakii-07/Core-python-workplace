'''
OOPs programmig
'''
details = {}

stud_name = input("Enter the name of student : ")
mark = {}
details[stud_name]=mark

num = int(input("Enter the total number of subjects "))
for i in range(num):
    s_name = input("Enter the subjcet name : ")
    marks = int(input("Enter the marks : "))
    mark[s_name]=marks
print("student dictionary : ",details)

mrk_list = [mark.values()]
total = len(mrk_list)*100
sum = sum(mrk_list)
print("total marks : ",total)


percent = (sum/total)*100
print("Percentage of marks :",percent)

if percent >= 40:
    print("student result : pass ")
else:
    print("student result : fail ")