l1 =[]

l2 = [10,30,"sakshi", False,56.34]
t1 = (10,20,30,40,50,60)
s1 = {0,"saki",True,90,67,46.8}

# add list into list - nestead list
l1.append(l2)
print(l1) # [[10, 30, 'sakshi', False, 56.34]]

# add tuple into list
l1.append(t1)
print(l1) # [[10, 30, 'sakshi', False, 56.34], (10, 20, 30, 40, 50, 60)]

# add set into list
l1.append(s1)
print(l1) # [[10, 30, 'sakshi', False, 56.34], (10, 20, 30, 40, 50, 60), {0, 'saki', True, 67, 90, 46.8}]