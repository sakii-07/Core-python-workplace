# import mysql.connector

# # mysql connection
# conn = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="root",
#     database="jbk_1319"
# )

# # print(conn)

# # if (conn.is_connected):
# #     print("Database connection done")
# # else:
# #     print("Database connection not done")

# def getAllStudentData():
#     curser=conn.cursor()
#     query = "select * from student"
#     curser.execute(query)
#     std= curser.fetchall()
#     print(std)
#     curser.close()
#     conn.close()

# # getAllStudentData()

# def getAllStudentData_1():
#     curser=conn.cursor()
#     query="select * from student"
#     curser.execute(query)
#     std_data=curser.fetchall()
#     for std in std_data:
#         print(std)
#     curser.close()
#     conn.close()

# # getAllStudentData_1()

# def insertData():
#     curser=conn.cursor()
#     query="insert into student values(%s,%s,%s,%s)"
#     data=(31,"Sakshi Jagtap",23,"Solapur")
#     curser.execute(query,data)
#     conn.commit()
#     print("Student data added...")
#     curser.close()
#     conn.close()

# # insertData()

# def getStudentData():
#     curser=conn.cursor()
#     query="select * from student where id=%s"
#     data=(31,)
#     curser.execute(query,data)
#     std=curser.fetchone()
#     print(std)
#     curser.close()
#     conn.close()

# # getStudentData()

# def updateData():
#     curser=conn.cursor()
#     query="update student set age=%s where id=%s"
#     data=(26,31)
#     curser.execute(query,data)
#     conn.commit()
#     print("Student data Updated...")
#     curser.close()
#     conn.close()

# # updateData()

# def deleteData():
#     curser=conn.cursor()
#     query="delete from student where id=%s"
#     data=(10,)
#     curser.execute(query,data)
#     conn.commit()
#     print("Student data deleted...")
#     curser.close()
#     conn.close()

# deleteData()



# table = str.maketrans("abc", "123")

# print("abc".translate(table))

s = "a-b-c-d"
print(s.split("-", 2))