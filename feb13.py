 #Slicing - access multiple elements from string
s = "Instagram"

# var_name[start_index : end_index] - step_size is optional
print(s[3:6]) # tag

print(s[6:9]) # ram
print(s[6:]) # ram - end_index is optional : end = len(s)

print(s[0:5]) # Insta
print(s[:5]) #Insta - start_index is optional : start = 0

print(s[:]) # Instagram - gives complete string

print(s[3:3]) # Empty string

print(s[6:19]) # ram

print(s[12:18]) # It gives empty string (no any error)

# var_name[start_index : end_index : step_size]
print(s[0:5:+2]) # Isa - + is positive directon means LHS to RHS
print(s[::+2]) # Isarm

print(s[9:2:-1]) # margat (- is negative directon means RHS to LHS )

print(s[3:6:+1]) # tag
print(s[6:3:-1]) # rga

print(s[3:6:+2]) # tg
print(s[6:3:-2]) # ra

print(s[::+1]) # Instagram - gives complete string
print(s[0:9:+1])

print(s[ : :-1]) # margatsnI - gives reverse string
print(s[-1:-10:-1])

print(s[0:9:-1]) # empty string
print(s[-6:-2:-1]) # empty string

print(s[-6:-2:+1]) # tagr

print(s[-6:8:+1]) # tagra
print(s[-6:8:+2]) # tga
print(s[-6:8:+5]) # t