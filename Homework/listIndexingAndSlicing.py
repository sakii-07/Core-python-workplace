list2 = [10, 20, 30, [40, 50, [60, 80, 90], 100, 110, 120], [112, 114, 116], 221, 226, 336]

# 1. Access First-Level Elements
print(list2[0]) # 10

# 2. What is the output of list2[0] and list2[3]?
print(list2[0]) # 10
print(list2[3]) # [40, 50, [60, 80, 90], 100, 110, 120]

# 3. Extract the list [40, 50, [60, 80, 90], 100, 110, 120] using indexing.
print(list2[3])

# 4. Retrieve 60, 80, and 90 from the nested list using indexing.
print(list2[3][2]) # [60, 80, 90]

# 5. What is the output of list2[4][1]?
print(list2[4][1]) # 114
		
# 6. Write a statement to access the element 336.
print(list2[-1]) # 366
		
# 7. The last element (336).
print(list2[-1]) # 336
		 
# 8. The second-to-last sub-list ([112, 114, 116]).
print(list2[-4]) # [112, 114, 116]	

# 9. Access 110 from the sub-list [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][-2]) # 110

# 10. Retrieve the element 116 from the list [112, 114, 116].
print(list2[-4][-1]) # 116

# 11. Extract 40 from [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][0]) # 40

# 12.	Write a slice to extract [30, [40, 50, [60, 80, 90], 100, 110, 120]].	
print(list2[2:4]) # [30, [40, 50, [60, 80, 90], 100, 110, 120]]

# 13.	Extract [100, 110, 120] from the nested sub-list [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][3:]) # [100, 110, 120]
			
# 14.	Write a slice to reverse the entire list2.	
print(list2[::-1])

l1 = list2[slice(None,None,-1)]
print(l1)

# # 15.	Reverse the list [112, 114, 116].
print(list2[-4][::-1]) # [116, 114, 112]

# # 16.	Write a slice to get [60, 80, 90].
print(list2[3][2]) # [60, 80, 90]

# 17. From the main list, extract [10, 30, [112, 114, 116]] using slicing.
list3 = list2[:3:2] + [list2[4]]
print(list3) # [10, 30, [112, 114, 116]]

# 18. Slice to extract [221, 226, 336] from the main list.
print(list2[5:]) # [221, 226, 336]

# 19. Write a slice to extract [40, 50, [60, 80, 90]].
print(list2[3][:4]) # [40, 50, [60, 80, 90], 100]

# 20.	Write a slice to get [10, 30, [112, 114, 116], 226].
list4 = list2[:3:2] + [list2[4]] + [list2[-2]]
print(list4) # [10, 30, [112, 114, 116], 226]




 
















