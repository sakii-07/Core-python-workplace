# Explore at least 10 string methods

# 1. uppercase()
s = "hello world"
s1 = s.upper() # HELLO WORLD
print(s1)

#   2. lowercase()
s = "Python Programming"
s1 = s.lower() # python programming
print(s1)

#   3. Capitalize()
s = "hello python learners"
s1 = s.capitalize() # Hello python learners
print(s1)

#   4. title()
s = "hello python learners"
s1 = s.title() # Hello Python Learners
print(s1)

#   5. strip().
'''  lstrip() → removes spaces from left side
  rstrip() → removes spaces from right side'''
s = " Python String Functions "            
s1 = s.strip() # Python String Functions
print(s1)

#   6. rstrip()
''' Leading spaces - Spaces that appear before the text starts.
  Trailing spaces - Spaces that appear after the text ends.'''
s = "Hello World "
s1 = s.rstrip() # Hello World
print(s1)

#   7. lstrip()
s = " Learn Python"
s1 = s.lstrip() # Learn Python
print(s1)

#   8. split().
s = "apple banana grape"
s1 = s.split() # ['apple', 'banana', 'grape']
print(s1)

#   9. join()
list = ['Python', 'is', 'fun']
j_list = " ".join(list) # Python is fun
print(j_list)

#   10. join().
list = ['A', 'B', 'C']
j_list = "-".join(list) # A-B-C
print(j_list)

