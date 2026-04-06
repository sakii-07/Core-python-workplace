# emp_datails = {
#     101:{'name':'pavan','department':'operation','salary':12000},
#     102:{'name':'sakshi','department':'development','salary':78004},
#     103:{'name':'sojar','department':'testing','salary':67034},
#     104:{'name':'pranjali','department':'operation','salary':20000},
#     105:{'name':'amruta','department':'testing','salary':25000}
# }

# # department vise total salary
# total_salary = {}
# for i in emp_datails:
#     dep = emp_datails[i]['department']
#     sal = emp_datails[i]['salary']

#     if dep in total_salary:
#         total_salary[dep] =total_salary[dep]+sal 
#     else:
#         total_salary[dep]=sal

# print(total_salary)

# # deparment vise avgg salary
# avg_salary = {}
# count = {}
# for i in emp_datails:
#     dep = emp_datails[i]['department']
#     sal = emp_datails[i]['salary']

#     if dep in emp_datails:
#         avg_salary[dep] = avg_salary[dep] + sal
#         count[dep] += 1
#     else:
#         avg_salary[dep] = sal
#         count[dep] = 1

# for dep,total in avg_salary.items():
#     avg_salary[dep] = total / count[dep]

# print(avg_salary)

# numbers = [1,3,4,5,6,7,8,34,56,67,34,78,56,46]
# # print thr list of all even numbers and odd numbers
# even_list = []
# odd_list = []
# for i in numbers:
#     if i%2==0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print("Even list : ",even_list)
# print("Odd list : ",odd_list)


# # print list of name of eligible and not eligible voters
# voter = {"sakshi":45,'kiran':23,'sujay':67,'pavan':21,'jay':11,'prakash':47,'rajesh':15}
# eligible = []
# not_eligible = []

# for name,age in voter.items():
#     if age >= 18:
#         eligible.append(name)
#     else:
#         not_eligible.append(name)

# print("Eligible voters : ",eligible)
# print("Not Eligible voters : ",not_eligible)

# # Find maximun number
# numbers = [10,40,50,30,77,55,1,90,3]
# max_num = numbers[0]

# for i in numbers:
#     if max_num < i:
#         max_num = i
    
# print("Maximum number : ",max_num)

# # Find miniimun number
# numbers = [10,40,50,30,77,55,1,90,3]
# min_num = numbers[0]

# for i in numbers:
#     if min_num > i:
#         min_num = i
    
# print("Minimum number : ",min_num) # Miniimum number :  1


# # 
# users = {'sakshi':'sakshi123','sojar':'sojar123','pranjali':'pranjali'}

# user = input("Enter the Username : ")
# p = input("Enter the Password : ")

# # way - 1
# for username,password in users.items():

#     if user == username and p == password:
#         print("Login successfull")
#         break
#     else:
#         print("Invalid creadintails")
#         break

# # way - 2
# if username in users and users[password] == password:
#     print("Login successfull")
# else:
#     print("Invalid creadintails")

# # find max salary
# emp_salary = {'sakshi':67000,'pranjali':45000,'sojar':24000,'amruta':78000}
# max_sal = 0
# max_name = ''
# for name , salary in emp_salary.items():

#     if salary > max_sal:
#         max_sal = salary
#         max_name = name

# print(max_name)

# find department vise maximum salary 
emp_datails = {
    101:{'name':'pavan','department':'operation','salary':12000},
    102:{'name':'sakshi','department':'development','salary':78004},
    103:{'name':'sojar','department':'testing','salary':67034},
    104:{'name':'pranjali','department':'operation','salary':20000},
    105:{'name':'amruta','department':'testing','salary':25000}
}

max_dep = {}
for i in emp_datails:
    dep = emp_datails[i]['department']
    sal = emp_datails[i]['salary']
    max_sal = 0
     
    if dep not in max_dep:
        max_dep[dep] = sal

        if sal > max_sal:
            max_sal = sal
    else:
        if sal > max_sal:
            max_sal = sal

print(max_dep)

    


