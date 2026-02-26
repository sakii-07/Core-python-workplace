# 						## List Method Practical ##

# 1. Create an empty list and use append() to add five different numbers to it. Print the final list.
l1 = []
l1.append(10)
l1.append("sakshi")
l1.append(200)
l1.append(12.3)
l1.append(2+3j)
print(l1)  # [10, 'sakshi', 200, 12.3, (2+3j)]

# 2. Create a list of student name  and append a new Student name  and print the length of list .
name = ["sakshi","sojar","pranjali","pranali","amruta"]
name.append("harsh")
print(name) # ['sakshi', 'sojar', 'pranjali', 'pranali', 'amruta', 'harsh']
print(len(name)) # 6

# 3. Append a list [10, 20, 30] to another list and observe the result.
l1 = [10,20,30]
l2 = []
l2.append(l1)
print(l2) # [[10, 20, 30]]

# 4. Create a list and make a copy using copy().
l1 = [10,20,30,40]
l2 = l1.copy()
print("l1 :  " , l1) # l1 :   [10, 20, 30, 40]
print("l2 :  " ,l2) # l2 :   [10, 20, 30, 40]

# 5. Create a list with at least 10 elements, use clear(), and check the length of the list afterward.
l1 = [10,20,30,40,40,50,60,70,80,90,10,39]
l1.clear()
print(l1) # []
print(len(l1)) # 0

# 6. Create a nested list and clear only the inner list while keeping the outer list intact .
l1 = [1,2,3,4,[1,6,8,9,2,3,[7,8,9],4,2,5],3,4,8]
l1[4].clear()
print(l1) # [1, 2, 3, 4, [], 3, 4, 8]
l1[4][6].clear()
print(l1) # [1, 2, 3, 4, [1, 6, 8, 9, 2, 3, [], 4, 2, 5], 3, 4, 8]

# 7. Given nums = [1, 2, 3, 4, 2, 2, 5, 2], find how many times 2 appears in the list.
nums = [1, 2, 3, 4, 2, 2, 5, 2]
print(nums.count(2)) # 4

# 8. Create a list of words and find how many times a particular word appears.
words = ["hi","hello","hi","welcome","python","hi","java","hi"]
print(words.count("hi")) # 4

'''9. Create two lists, list1 in integer variable  and list2 in String variable. Use extend() to add
elements of list2 to list1. Print the final result.'''
list1 = [1, 2, 3, 4]
list2 = ["Python", "Java", "C++"]
list1.extend(list2) # [1, 2, 3, 4, 'Python', 'Java', 'C++']
print(list1)

# 10. Given fruits = ['apple', 'banana', 'cherry', 'banana', 'grape'], find the index of banana.
fruits = ['apple', 'banana', 'cherry', 'banana', 'grape']
print(fruits.index("banana")) # 1

# 11. Insert the number 100 at the beginning of the list [10, 20, 30].
list = [10, 20, 30]
list.insert(0,100) # [100, 10, 20, 30]
print(list)

# 12. Insert 'Python' at index 2 in a list of programming languages and print the result.
lang = ["C", "C++", "Java", "JavaScript"]
lang.insert(2,"Python")
print(lang) # ['C', 'C++', 'Python', 'Java', 'JavaScript']

# 13. Given numbers = [5, 10, 15, 20, 25], remove and print the last element using pop().
numbers = [5, 10, 15, 20, 25]
print(numbers.pop()) # 25

# 14. Remove an element at index 2 and print both the removed element and the updated list.
numbers = [5, 10, 15, 20, 25]
print(numbers.pop(2)) # 15
print(numbers) # [5, 10, 20, 25]

# 15. Given colors = ['red', 'blue', 'green', 'blue', 'yellow'], remove the first occurrence of 'blue'.
colors = ['red', 'blue', 'green', 'blue', 'yellow']
colors.remove("blue")
print(colors) # ['red', 'green', 'blue', 'yellow']

# 16. Reverse the list [1, 4, 9, 16, 25] and print the result.
list = [1, 4, 9, 16, 25]
list.reverse() # [25, 16, 9, 4, 1]
print(list)

# 17. Reverse a list of words and join them to form a sentence words = ["Hello", "world", "Python"].
words = ["Hello", "world", "Python"]
words.reverse()
j_list = " ".join(words)
print(j_list) # Python world Hello

# 18. Sort a list of numbers [10, 5, 8, 3, 1] in ascending and then in descending order.
l1 = [10, 5, 8, 3, 1]
l1.sort()
print(l1) # [1, 3, 5, 8, 10]
