# String iteraton using for loop

s = "Instagram"

for ch in s :
    print(s) # return 9 times Instagram

for ch in s :
    print(ch)

for i in "atul" :
    print("111")
    for j in "atul" :
        print("222")
    print("333")

for ch in s :
    print(ch,"----> Insta") 

for ch in s :
    print(ch, " -----> ",s[:5]) 

# task-1 print I ----> 1 , ..... , m ----> 9
i = 1
for ch in s :
    print(ch," ----> ",i)               # I ----> 1
    i = i+1                             # n ----> 2
                                        # s ----> 3
                                        # t ----> 4
                                        # a ----> 5
                                        # g ----> 6
                                        # r ----> 7
                                        # a ----> 8
                                        # m ----> 9
 

for ch in s :
    print(ch,"---->", s.index(ch)+1)    # I ----> 1
                                        # n ----> 2
                                        # s ----> 3
                                        # t ----> 4
                                        # a ----> 5
                                        # g ----> 6
                                        # r ----> 7
                                        # a ----> 5 - here the address of a is repeated
                                        # m ----> 9

# task-2 : find total white spaces in given string

s1 = "I love python programming"
count = 0
for ch in s1 :
    if(ch == " ") :
        count = count + 1

print(F"Total white spaces = {count}")  # Total white spaces =  3

# task-2 : find number of  p in given string

for ch in s1 :
    if(ch == "p") :
        count = count + 1
print(f"Total P's in string = {count}") # Total P's in string = 5

# task-3 : find freqeuncy of given string or total number of words
