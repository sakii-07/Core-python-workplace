							## String Functions Practices ##
		
#   1. Write a Python program to convert the given string "hello world" to uppercase.
s = "hello world"
s1 = s.upper() # HELLO WORLD
print(s1)

#   2. Convert the string "Python Programming" to lowercase.
s = "Python Programming"
s1 = s.lower() # python programming
print(s1)

#   3. Capitalize the first letter of "hello python learners".
s = "hello python learners"
s1 = s.capitalize() # Hello python learners
print(s1)

#   4. Convert "welcome to python" to title case.
s = "hello python learners"
s1 = s.title() # Hello Python Learners
print(s1)

#   5. Remove leading and trailing spaces from the string " Python String Functions " using strip().
#   lstrip() → removes spaces from left side
#   rstrip() → removes spaces from right side
s = " Python String Functions "            
s1 = s.strip() # Python String Functions
print(s1)

#   6. Remove only trailing spaces from "Hello World " .
#   Leading spaces - Spaces that appear before the text starts.
#   Trailing spaces - Spaces that appear after the text ends.
s = "Hello World "
s1 = s.rstrip() # Hello World
print(s1)

#   7. Remove only leading spaces from " Learn Python".
s = " Learn Python"
s1 = s.lstrip() # Learn Python
print(s1)

#   8. Split the string "apple banana grape" into a list using split().
s = "apple banana grape"
s1 = s.split() # ['apple', 'banana', 'grape']
print(s1)

#   9. Join the list ['Python', 'is', 'fun'] into a single string using join() with space as a separator.
list = ['Python', 'is', 'fun']
j_list = " ".join(list) # Python is fun
print(j_list)

#   10. Convert the list ['A', 'B', 'C'] into a single string "A-B-C" using join().
list = ['A', 'B', 'C']
j_list = "-".join(list) # A-B-C
print(j_list)

#   11. Find the index of the first occurrence of "Python" in "I love Python programming".
s = "I love Python programming"
s1 = s.find("Python") # 7
print(s1)

#   12. Find the last occurrence of "o" in "Hello World".
#   find() → first occurrence
#   rfind() → last occurrence
s = "Hello World"
s1 = s.rfind("o") # 7
print(s1)

#   13. Replace "Java" with "Python" in the string "I love Java".
s = "I love Java"
s1 = s.replace("Java","Python") # I love Python
print(s1)

#   14. Check if the string "Hello World" starts with "Hello".
s = "Hello World"
s1 = s.startswith("Hello") # True
print(s1)

#   15. Check if the string "example.txt" ends with ".txt".
s = "example.txt"
s1 = s.endswith(".txt") # True
print(s1)

#   16. Count the occurrences of "o" in "Hello, how are you?".
s = "Hello World"
s1 = s.count("o") # 2
print(s1)

#   17. Find the index of "r" in "programming".
s = "programming"
s1 = s.index('r') # 1
print(s1)

#   18. Try finding the index of "z" in "python" using index(), and observe the error.
s = "python"
s1 = s.index('z') # ValueError: substring not found
print(s1)

#   19. find the last occurrence of "e" in "experience".
s = "experience"
s1 = s.rfind('e') # 9
print(s1)

#   20. find the first occurrence of "e" in "experience".
s = "experience"
s1 = s.find('e') # 0
print(s1)

#   21. Check if the string "Python" contains only alphabets.
s = "experience"
s1 = s.isalpha() # True
print(s1)

#   22. Verify if "12345" contains only digits.
s = "12345"
s1 = s.isdigit() # True
print(s1)

#   23. Check if "Python123" is alphanumeric.
s = "Python123"
s1 = s.isalnum() # True
print(s1)

#   24. Test if the string " " consists of only spaces.
s = " "
s1 = s.isspace() # True
print(s1)

#   25. Check if "12345" is numeric using.
s = "12345"
s1 = s.isnumeric() # True
print(s1)

#   26. Use format() to insert "Python" and "fun" into the string "{} is {}!".
s = "{} is {}!"
s1 = s.format("Python","fun") # Python is fun!
print(s1)

#   27. Partition the string "python-programming-language" at "-".
s = "python-programming-language"
s1 = s.partition("-") # ('python', '-', 'programming-language')
print(s1)

#   28. Use rpartition() to split "one-two-three" from the right sing "-".
s = "one-two-three"
s1 = s.partition("-") # ('one', '-', 'two-three')
print(s1)

#   29. Convert "PYTHON" to lowercase using casefold().
s = "PYTHON"
s1 = s.casefold() # python
print(s1)

#   30. Convert "42" into a 5-character string padded with zeros using zfill().
s = "42"
s1 = s.zfill(5) # 00042
print(s1)

#   31. Check if "HELLO" is in uppercase.
s = "HELLO"
s1 = s.isupper() # True
print(s1)

#   32. Verify if "hello" is in lowercase.
s = "hello"
s1 = s.islower() # True
print(s1)

#   33. Check if "Python Programming" follows title case.
s = "Python Programming"
s1 = s.istitle() # True
print(s1)

# #   34. Sort the characters of "banana" alphabetically.
s = "banana"
s1 = "".join(sorted(s)) # aaabnn
print(s1)

#   35. Find the length of the string "Data Science".
s = "Data Science"
s1 = len(s) # 12
print(s1)

#   36. Sort the characters of "The Kiran  Academy" alphabetically in descending Order.
s = "The Kiran  Academy"
s1 = "".join(sorted(s, reverse=True)) # yrnmiheedcaaTKA
print(s1)