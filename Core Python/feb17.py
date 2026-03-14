#                            	##   String Functions  ##

#  1. upper()
#  	Purpose: Converts all characters to uppercase.
#  	Syntax: v_name.upper()

#  2. lower()
#  	Purpose: Converts all characters to lowercase.
#  	Syntax: v_name.lower()

#  3. capitalize()
#  	Purpose: Capitalizes the first character and lowercases the rest.
#  	Syntax: v_name.capitalize()

#  4. title()
#  	Purpose: Capitalizes the first character of each word.
#  	Syntax: v_name.title()

#  5. strip() / rstrip() / lstrip()
#  	Purpose: Removes leading/trailing whitespace (or specified characters).
#  	Syntax: 	
#   		v_name.strip()
#   		v_name.rstrip()
#   		v_name.ltrip()

#  6. split()
#  	Purpose: Splits the string into a list using a delimiter (default: whitespace).
#  	Syntax: v_name.split()

#  7. join()
#  	Purpose: Joins elements of an iterable (e.g., list) into a string.
#  	Syntax: "-".join(v_name)

#  8. find()  / rfind()
#  	Purpose: Returns the index of the first occurrence of a substring (or -1 if not found).
#  	Syntax: 	
#   		v_name.find()
#   		v_name.rfind()

#  9. replace()
#  	Purpose: Replaces occurrences of a substring with another substring.
#  	Syntax:  v_name.replace(old, new)

#  10. startswith() / endswith()
#  	Purpose: Checks if the string starts/ends with a specified substring.
#  	Syntax:
#    		v_name.startswith(Character/ word) 
#    		v_name.endswith(Character/ word)

#  11. count()
#  	Purpose: Counts occurrences of a substring.
#  	Syntax:	v_name.count(Character/ word)
   
#  12. index() / rindex()
#  	Purpose: Similar to find(), but raises an error if the substring is not found.
#  	Syntax: 	
#   		v_name.index(Character)
#   		v_name.rindex(Character)

#  13. isalpha() / isdigit() / isalnum() / isnumeric() /  isspace()  
#  	Purpose: Checks if all characters are alphabets, digits, or alphanumeric or space.
#  	Syntax: 	
#   		v_name.isalpha() 
#   		v_name.isdigit() 
#   		v_name.isalnum()
#   		v_name.isnumeric()
#   		v_name. isspace()

#  14. format()
#  	Purpose: Formats a string using placeholders ({}).
#  	Syntax: v_name.format(*args, **kwargs)

#  15. partition() / rpartition()
#  	Purpose: Splits the string into a tuple of three parts using a separator.
#  	Syntax: 	
#   		v_name.partition(sep)
#   		v_name.rpartition(sep)

#  16. casefold()
#  	Purpose: Converts to lowercase for case-insensitive comparisons (stronger than lower()).
#  	Syntax: v_name.casefold()

#  17. zfill()
#  	Purpose: Pads the string with leading zeros to reach a specified width.
#  	Syntax: v_name.zfill(size)
#  	Example:
#   		s = "42"
#   		print(s.zfill(5))  # Output: "00042"

#  18. isupper() / islower() /  istitle()  
#  	Purpose: Checks if all characters are alphabets, uppercase, or lowercase  or title  	Syntax: 	
#   	v_name. isupper() 
#   	v_name.islower() 
#   	v_name.istitle()

#  19. sorted()
#  	Purpose: sort the String .
#  	Syntax: sorted(v_name) 

#  20 . len()
#  	Purpose: sort the String .
#  	Syntax: len(v_name) 
  	
l1 = [1,2,3,4,2,4,5,6,7,5,6,7,8,45,3,4,5]
duplicates = []
for i in l1:
    if l1.count(i)>1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)


l1 = [1,2,3,4,2,4,5,6,7,5,6,7,8,45,3,4,5]
unique = []
for i in l1:
    if l1.count(i)==1 :
        unique.append(i)
print(unique)