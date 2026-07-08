# WAP to check whether a give number  is perfect square or not
# way - 1
def isPerfectSquare(num):
    for i in range(1,num+1):
        if i*i == num:
            return True
    else:
        return False
print(isPerfectSquare(64))

# way - 2
num = int(input("Enter number "))
sr = int(num**0.5)
num1 = sr*sr
if num == num1:
    print("Yes")
else:
    print("No")

'''
mobile number
check ---> valid
'''

mobile = int(input("Enter mobile number "))
def isvalid(mobile_no):
    if isinstance(mobile_no,int) and len(str(mobile_no)) == 10:
        return True
    else:
        return False
    
print(isvalid(mobile))

# iterate all valid numbers form list
numbers = [8947635490,9808764234,9876543289,'87904673528',9908474638,'9088907.7864']

for mobile in numbers:
    if isinstance(mobile,int) and len(str(mobile)) == 10:       
        print(mobile)
   
# user --> email and check is valid
email = input("Enter email ")

def isEmailValid(email):
    if email.endswith("gmail.com") and len(email[:-10])>0 and email.islower() and ' ' not in email and not any (ch in email for ch in [' ','#','%','$'] or any (ch in email for ch in ['_','.'])):
        return True
    else:
        return False
    
print(isEmailValid(email))

# list ---> [N.R.Patil,....]
details = ["nayan rajesh patil","praful ravindra raut","vijay sudhakar bhosale","sakshi balasaheb jagtap"]
names = []
for name in details:
    l = name.split(" ")
    fname = l[0][0]
    mname = l[1][0]
    lname = l[-1]
    nm = f'{fname}.{mname}.{lname}'.title()
    names.append(nm)
print(names)

# perfect number
num = int(input("Enter number :"))
def isperfect(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum +=i

    if sum == num:
        return True
    else:
        return False

print(isperfect(num))

# WAP to reverse a string
string = input("Enter the string : ")
def reverseString(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev
print(reverseString(string))

# WAP to calculate new salary after increament
salary = eval(input("Enter salary : "))
increment = eval(input("Enter the increment : "))

total = salary + (salary*increment)/100
print("New salary : ",total)

# The kiran acadamy  --->  ehT narik ymadaca
s = "The kiran acadamy"
l = s.split()
r = []
for word in l:
    rev = ""

    for ch in word:
        rev = ch + rev

    l.append(rev)

print(" ".join(r))
# print(s2)


# count no of character in string
string = input("Enter the string : ")
count = 0
for i in string:
    count += 1
print(count)

# WAP to count no of scpaes in given sentence
sen = 'The Kiran Acadamy'
count = 0
for ch in sen:
    if ch == " ":
        count += 1
print(count)

sen = 'The Kiran Acadamy'
word_count = {}
l = sen.split()
for word in l:
    count = 0
    for ch in word:
        count += 1
    word_count[word] = count
print(word_count)

# WAP count frequency of the word
word = input("Enter the string : ")
def frequency(word):
    d = {}
    for ch in word:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d
print(frequency(word))

# longest palindrome
word = "acadamy"
longest = ""
c =[]
for ch in word:
    for i in range(len(word)):
        for j in range(i+1,len(word)+1):
            sub = word[i:j]
        
            if sub == sub[::-1] and len(sub)>len(longest):
                longest = sub
            if len(sub)==len(longest) and sub == sub[::-1] and sub not in c and len(sub)>1:
                c.append(sub)

print(longest)
print(c)



word = "sacasdamy"
longest = ""

for ch in word:
    for i in range(len(word)):
        for j in range(i+1,len(word)+1):
            sub = word[i:j]

            if sub == sub[::-1] and len(sub)>len(longest):
                longest = sub

print(longest)

word  = "acadaasddsamy"
longest = ""

for ch in word:
    for i in range(len(word)):
        for j in range(i+1,len(word)+1):
            sub = word[i:j]

            if sub[::-1] == sub and len(sub) > len(longest):
                longest = sub
print(longest)