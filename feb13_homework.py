# slicing - access multiple elements from string
name = "Sakshi Jagtap"

# var_name[start_index : end_index] - step_size is optional
print("Name : ", name)  # Sakshi Jagtap
print("length of given String : ",len(name)) # 13
print("----------------------")

# var_name[start_index : end_index] - step_size is optional

# 5 positive + positive index
print("Example of 5 positive + positive index")
print(name[:]) # Sakshi Jagtap - gives complete string start with 0 and end with len(name)
print(name[:9]) # Sakshi Ja - start_index is optional : start = 0
print(name[8:]) # agtap - end_index is optional : end = len(name)
print(name[5:14]) # i Jagtap
print(name[19:20]) # empty string
print("----------------------")

# 5 negative + negative index
print("Example of 5 negative + negative index")
print(name[-12:-3]) # akshi Jag
print(name[:-7]) # Sakshi
print(name[-9:]) # hi Jagtap
print(name[-15:-24]) # empty string
print(name[-10:-4]) # shi Ja
print("----------------------")

# 5 positive + negative index
print("Example of 5 positive + negative index")
print(name[4:-4]) # hi Ja
print(name[:-5]) # Sakshi J
print(name[2:-6]) # kshi
print(name[5:-2]) # i Jagt
print(name[:-1]) # Sakshi Jagta
print("----------------------")

# 5 negative + positive index
print("Example of 5 negative + positive index")
print(name[-10:]) # shi Jagtap
print(name[-8:12]) # i Jagta
print(name[-11:]) # kshi Jagtap
print(name[-7:12]) #  Jagta
print(name[-5:11]) # agt
print("----------------------")

# var_name[start_index : end_index : step_size]

# 5 on +ve step size
print("5 Example on positive step size")
print(name[::]) # Sakshi Jagtap - start with 0, end with len(name) and default step size is +1
print(name[5::+2]) # iJga
print(name[7:12:+3]) # Jt
print(name[:13:+4]) # Shap
print(name[::+5]) # Sit
print("----------------------")

# 5 on -ve step size
print("5 Example on negative step size")
print(name[-10:-3:-1])  # Empty string
print(name[-4:-9:-2]) # gJi
print(name[-2:-11:-3]) # aai
print(name[-5:-50:-4]) # ahS
print(name[-3:-10:-5]) # ti
print("----------------------")