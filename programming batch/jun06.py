# '''
# WAP that accepts number as interger and find of its factors
# '''

# def factor(num):
#     for i in range(1,num+1):
#         if num%i == 0:
#             print(i , end=" ")
# num = int(input("Enter number : "))
# factor(num) # 1 2 3 6 


# '''
# WAP that accepts number as interger and calculate the sum of its factors
# '''
# num = int(input("Enter number : "))
# sum = 0
# for i in range(1,num):
#     if num%i==0:
#         sum += i
# print(sum)

# '''
# WAP that accepts number as interger and counters how many factors it has
# '''

# num = int(input("Enter number : "))
# count = 0
# for i in range(1,num):
#     if num%i==0:
#         count+=1
# print(count)

# '''
# WAP that accepts number as interger and their least common multiple
# '''

# num1 = int(input("Enter the first number "))
# num2 = int(input("Enter the second number "))

## Way - 1
# for i in range(1,num1):
#     for j in range(1,num2):
#         if num1*i == num2*j:
#             print(num1*i)
#             break

## Way - 2
# max = max(num1,num2)
# min = min(num1,num2)
# for i in range(1,max):
#     if (max*i) % min == 0:
#         print(max*i)
#         break

## Way - 3
# max = max(num1,num2)
# min = min(num1,num2) 
# inc = max
# while True:
#     if max%min==0:
#         print(max)
#         break
    # max+=inc

'''
dict of number with factors
'''
numbers = [5,6,7,9,12,34,67]
# d = {}
# for num in numbers:
#     factors = []
#     for j in range(1,num):
#         if num%j == 0 :
#             factors.append(j)
#     d[num] = factors
# print(d) # {5: [1], 6: [1, 2, 3], 7: [1], 9: [1, 3], 12: [1, 2, 3, 4, 6], 34: [1, 2, 17], 67: [1]}

# numbers = [5,6,7,9,12,34,67]
# factors_count = {}
# for num in numbers:
#     count = 0
#     for j in range(1,num):
#         if num%j == 0 :
#             count += 1
#     factors_count[num] = count
# print(factors_count) # {5: 1, 6: 3, 7: 1, 9: 2, 12: 5, 34: 3, 67: 1}

# numbers = [5,6,7,9,12,34,67]
# factors_sum = {}
# for num in numbers:
#     sum = 0
#     for j in range(1,num):
#         if num%j == 0 :
#             sum += j
#     factors_sum[num] = sum
# print(factors_sum) # {5: 1, 6: 6, 7: 1, 9: 4, 12: 16, 34: 20, 67: 1}