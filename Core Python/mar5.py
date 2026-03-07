movie_db = {}

dhurandar_cast = ["Ranveer Singh", "Akshaye Khanna", "Sanjay Dutt", "R. Madhavan", "Arjun Rampal", "Sara Arjun", "Rakesh Bedi", "Gaurav Gera", "Danish Pandor"]
chhaava_cast = ["Vicky Kaushal", "Rashmika Mandanna", "Akshaye Khanna", "Ashutosh Rana", "Divya Dutta", "Rajesh Sharma"] 
salaar_cast = ["Prabhas","Prithviraj Sukumaran", "Shruti Haasan", "Jagapathi Babu", "Bobby Simha", "Sriya Reddy"]
singham_again_cast = ["Ajay Devgn", "Kareena Kapoor Khan", "Deepika Padukone", "Ranveer Singh", "Akshay Kumar", "Tiger Shroff"]

movie_db["Chhaava"] = chhaava_cast
movie_db["Dhurandar"] = dhurandar_cast
movie_db["Salaar"] = salaar_cast
movie_db["Singham_again"] = singham_again_cast

# print(movie_db["Chhaava"])

# Task 1 :- Display first actor name from dhurandar movie

# # using get method
# l = movie_db.get("Dhurandar")
# print(l[0]) # Ranveer Singh

# # using indexing
# print(movie_db["Dhurandar"][0]) # Ranveer Singh

# # Display the sirname of first actor name form dhurandar
# print(movie_db["Dhurandar"][0][8:]) # Singh

# # Display the first actor name in reverse
# print(movie_db["Dhurandar"][0][::-1]) # hgniS reevnaR

# # Display the 'r' letter of "Ranveer Singh"
# print(movie_db["Dhurandar"][0][6]) # r

# Task 2 - Display names of all actors and actress on console one by one
# for movie,actor in movie_db.items():
#     print(movie,"---->")
#     for name in actor:
#         print("\t",name)
#     print("---"*20)
    # print("=="*20)
'''
Chhaava ---->
         Vicky Kaushal
         Rashmika Mandanna
         Akshaye Khanna
         Ashutosh Rana
         Divya Dutta
         Rajesh Sharma
------------------------------------------------------------
Dhurandar ---->
         Ranveer Singh
         Akshaye Khanna
         Sanjay Dutt
         R. Madhavan
         Arjun Rampal
         Sara Arjun
         Rakesh Bedi
         Gaurav Gera
         Danish Pandor
------------------------------------------------------------
Salaar ---->
         Prabhas
         Prithviraj Sukumaran
         Shruti Haasan
         Jagapathi Babu
         Bobby Simha
         Sriya Reddy
------------------------------------------------------------
Singham_again ---->
         Ajay Devgn
         Kareena Kapoor Khan
         Deepika Padukone
         Ranveer Singh
         Akshay Kumar
         Tiger Shroff
------------------------------------------------------------
'''

# for movie,actor in movie_db.items():
#     print(movie,"---->")
#     for name in actor:
#         n = name.split()
#         print("\t",name,":-")
#         for i in n:
#             print("\t\t",i)
#     print("---"*20)
'''
Chhaava ---->
         Vicky Kaushal :-
                 Vicky
                 Kaushal
         Rashmika Mandanna :-
                 Rashmika
                 Mandanna
         Akshaye Khanna :-
                 Akshaye
                 Khanna
         Ashutosh Rana :-
                 Ashutosh
                 Rana
         Divya Dutta :-
                 Divya
                 Dutta
         Rajesh Sharma :-
                 Rajesh
                 Sharma
------------------------------------------------------------
Dhurandar ---->
         Ranveer Singh :-
                 Ranveer
                 Singh
         Akshaye Khanna :-
                 Akshaye
                 Khanna
         Sanjay Dutt :-
                 Sanjay
                 Dutt
         R. Madhavan :-
                 R.
                 Madhavan
         Arjun Rampal :-
                 Arjun
                 Rampal
         Sara Arjun :-
                 Sara
                 Arjun
         Rakesh Bedi :-
                 Rakesh
                 Bedi
         Gaurav Gera :-
                 Gaurav
                 Gera
         Danish Pandor :-
                 Danish
                 Pandor
------------------------------------------------------------
Salaar ---->
         Prabhas :-
                 Prabhas
         Prithviraj Sukumaran :-
                 Prithviraj
                 Sukumaran
         Shruti Haasan :-
                 Shruti
                 Haasan
         Jagapathi Babu :-
                 Jagapathi
                 Babu
         Bobby Simha :-
                 Bobby
                 Simha
         Sriya Reddy :-
                 Sriya
                 Reddy
------------------------------------------------------------
Singham_again ---->
         Ajay Devgn :-
                 Ajay
                 Devgn
         Kareena Kapoor Khan :-
                 Kareena
                 Kapoor
                 Khan
         Deepika Padukone :-
                 Deepika
                 Padukone
         Ranveer Singh :-
                 Ranveer
                 Singh
         Akshay Kumar :-
                 Akshay
                 Kumar
         Tiger Shroff :-
                 Tiger
                 Shroff
------------------------------------------------------------
'''

# for movie,actor in movie_db.items():
#     print(movie,"---->")
#     for name in actor:
#         n = name.split()
#         print("\t",name,":-")
#         for i in n:
#             print("\t\t",i)
#             for j in i:
#                 print("\t\t\t",j)
#     print("---"*20)
'''
Chhaava ---->
         Vicky Kaushal :-
                 Vicky
                         V
                         i
                         c
                         k
                         y
                 Kaushal
                         K
                         a
                         u
                         s
                         h
                         a
                         l
------------------------------------------------------------
'''
# count = 0
# for movie,actor in movie_db.items():
#     print(movie,"---->")
#     for name in actor:
#         # n = name.split()
#         # print("\t",name,":-")
#         for i in name:
#             # print("\t\t",i)
#             for j in i:
#                 if j == 'a':
#                     count = count + 1
#         if count > 2:
#             print(name)
#     print("---"*20)


# level 2 = {int,dict{rollno,values}}

div_A = {1 : {"name":"jay","sub":["maths","phy","chem"],"marks":[89,71,99]},
         2 : {"name":"pavan","sub":["maths","phy","chem"],"marks":[66,55,77]},
         3 : {"name":"kiran","sub":["maths","phy","chem"],"marks":[89,99,99]},
         }

# for roolNo, student in div_A.items():
#     name = student["name"]
#     mark = student["marks"]

#     avg = sum(mark)/ len(mark)
#     print(name,avg)

# for roolNo, student in div_A.items():
#     for key,values in student:
#         print(key,"---->",values)

for rollNo, student in div_A.items():
    mark = student.get("marks")
    avg = sum(mark)/len(mark)
    print(rollNo,"--->",student.get("name"),"--->",avg)
'''
1 ---> jay ---> 86.33333333333333
2 ---> pavan ---> 66.0
3 ---> kiran ---> 95.66666666666667
'''


