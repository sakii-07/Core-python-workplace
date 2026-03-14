list1 = [1,2,3,4,5,3,6,7,4,7,6,23,10,4,5,8,9,1,2]

# way - 1
unique = []
for i in list1:
    if i not in unique:
        unique.append(i)
print(unique) # [1, 2, 3, 4, 5, 6, 7, 23, 10, 8, 9]

# way - 2
unique = list(set(list1))
print(unique) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23]

# way - 3
unique = list(dict.fromkeys(list1))
print(unique) # [1, 2, 3, 4, 5, 6, 7, 23, 10, 8, 9]
