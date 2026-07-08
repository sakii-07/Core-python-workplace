# # comman from two list
# l1= [1,2,3,4,5,6]
# l2 = [2,5,7,8]
# comman = {}
# c = []
# for i in l1:
#     if i in l2:
#         c.append(i)
# comman["Comman"] = c

# print(comman)


# Exception in finally
class notConvertToString(Exception):
    def __init__(self, msg):
        self.msg = msg
try:
    print(4/0)
finally:
    raise notConvertToString("Pass int value")
