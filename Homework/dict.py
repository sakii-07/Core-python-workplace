'''
create dictionary of 2025 movies - level 1 dict
'''
movie_db = {}

chhaava_cast = ["Vicky Kaushal", "Rashmika Mandanna", "Akshaye Khanna", "Ashutosh Rana", "Divya Dutta", "Rajesh Sharma"] 

dhurandar_cast = ["Ranveer Singh", "Akshaye Khanna", "Sanjay Dutt", "R. Madhavan", "Arjun Rampal", "Sara Arjun", "Rakesh Bedi", "Gaurav Gera", "Danish Pandor"]

salaar_cast = ["Prabhas", "Prithviraj Sukumaran", "Shruti Haasan", "Jagapathi Babu", "Bobby Simha", "Sriya Reddy"]

singham_again_cast = ["Ajay Devgn", "Kareena Kapoor Khan", "Deepika Padukone", "Ranveer Singh", "Akshay Kumar", "Tiger Shroff"]

movie_db["Chhaava"] = chhaava_cast
movie_db["Dhurandar"] = dhurandar_cast
movie_db["Salaar"] = salaar_cast
movie_db["Singham_again"] = singham_again_cast

# Display the complete dictionary
print(movie_db)
'''
{'Chhaava': ['Vicky Kaushal', 'Rashmika Mandanna', 'Akshaye Khanna', 'Ashutosh Rana', 'Divya Dutta',
 'Rajesh Sharma'], 'Dhurandar': ['Ranveer Singh', 'Akshaye Khanna', 'Sanjay Dutt', 'R. Madhavan', 
 'Arjun Rampal', 'Sara Arjun', 'Rakesh Bedi', 'Gaurav Gera', 'Danish Pandor'],
'Salaar': ['Prabhas', 'Prithviraj Sukumaran', 'Shruti Haasan', 'Jagapathi Babu', 'Bobby Simha', 
'Sriya Reddy'], 'Singham_again': ['Ajay Devgn', 'Kareena Kapoor Khan', 'Deepika Padukone', 'Ranveer Singh',
 'Akshay Kumar', 'Tiger Shroff']}
'''
# Display the all keys of dictionary
for k in movie_db.keys():
    print(k)
'''
Chhaava
Dhurandar
Salaar
Singham_again
'''

# Display the all values of dictionary
for v in movie_db.values():
    print(v)
'''
['Vicky Kaushal', 'Rashmika Mandanna', 'Akshaye Khanna', 'Ashutosh Rana', 'Divya Dutta', 'Rajesh Sharma']
['Ranveer Singh', 'Akshaye Khanna', 'Sanjay Dutt', 'R. Madhavan', 'Arjun Rampal', 'Sara Arjun', 'Rakesh Bedi', 'Gaurav Gera', 'Danish Pandor']
['Prabhas', 'Prithviraj Sukumaran', 'Shruti Haasan', 'Jagapathi Babu', 'Bobby Simha', 'Sriya Reddy']
['Ajay Devgn', 'Kareena Kapoor Khan', 'Deepika Padukone', 'Ranveer Singh', 'Akshay Kumar', 'Tiger Shroff']
'''

# Display the all items (key with value) of dictionary
for t in movie_db.items():
    print(t)
'''
('Chhaava', ['Vicky Kaushal', 'Rashmika Mandanna', 'Akshaye Khanna', 'Ashutosh Rana', 'Divya Dutta', 'Rajesh Sharma'])
('Dhurandar', ['Ranveer Singh', 'Akshaye Khanna', 'Sanjay Dutt', 'R. Madhavan', 'Arjun Rampal', 'Sara Arjun', 'Rakesh Bedi', 'Gaurav Gera', 'Danish Pandor'])
('Salaar', ['Prabhas', 'Prithviraj Sukumaran', 'Shruti Haasan', 'Jagapathi Babu', 'Bobby Simha', 'Sriya Reddy'])
('Singham_again', ['Ajay Devgn', 'Kareena Kapoor Khan', 'Deepika Padukone', 'Ranveer Singh', 'Akshay Kumar', 'Tiger Shroff'])
'''

# Display the all keys and values of dictionary
for k,v in movie_db.items():
    print(k,"--->",v)
'''
Chhaava ---> ['Vicky Kaushal', 'Rashmika Mandanna', 'Akshaye Khanna', 'Ashutosh Rana', 'Divya Dutta', 'Rajesh Sharma']
Dhurandar ---> ['Ranveer Singh', 'Akshaye Khanna', 'Sanjay Dutt', 'R. Madhavan', 'Arjun Rampal', 'Sara Arjun', 'Rakesh Bedi', 'Gaurav Gera', 'Danish Pandor']
Salaar ---> ['Prabhas', 'Prithviraj Sukumaran', 'Shruti Haasan', 'Jagapathi Babu', 'Bobby Simha', 'Sriya Reddy']
Singham_again ---> ['Ajay Devgn', 'Kareena Kapoor Khan', 'Deepika Padukone', 'Ranveer Singh', 'Akshay Kumar', 'Tiger Shroff']
'''

# Display the all keys of dictionary using items() method
for k,v in movie_db.items():
    print(k)
'''
Chhaava
Dhurandar
Salaar
Singham_again
'''

# task :- Display the names of the movies of 'Ranveer Singh' and the total number of movies.
count = 0
for k,v in movie_db.items():
    for name in v:
        if name == "Ranveer Singh":
            count = count + 1
            print(k)
print("The number of movies : ",count)
'''
Dhurandar
Singham_again
The number of movies :  2
'''

# task :- Display the number of 'a' in movie_db
count = 0
for k,v in movie_db.items():
    for i in v:
        for l in i:
            if l.lower() == 'a':
                count = count + 1
print(count) # 67

# task :- Display the number of actors whose names start with 'A' in movie_db.
count = 0
for k,v in movie_db.items():
    for i in v:
        for name in i:
            if name.startswith('A'):
                count=count+1
print(count) # 7

# Task :- Display the names of the movies of 'Akshaye Khanna' and the total number of movies.
count = 0
for k,v in movie_db.items():
    for name in v :
        if name == "Akshaye Khanna":
            count = count + 1
            print(k)
print("The number of movies : ", count)
'''
Chhaava
Dhurandar
The number of movies :  2
'''