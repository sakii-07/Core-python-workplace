# class - bank 
# create acount
# deposite
# withdraw
# show details by id
import csv
import datetime
class Bank:

    def __init__(self):
        pass

    def create_account(self):
        name = input("Enter the name : ")
        mobile = input("Enter the mobile no : ")    
        email = input("Enter the email : ")
        balance = input("Enter the balance : ")
        city = input("Enter the city : ")

        with open('bank_details.csv',"r") as file:

            reader = list(csv.reader(file))

        last_account_no= int(reader[-1][0])
        ac = last_account_no + 1
        for data in reader:
            if data[3] == email:
                print("Account exist already ")
                return
                
        with open('bank_details.csv',"a",newline="") as file1:

            writer = csv.writer(file1)
            writer.writerow([ac,name,mobile,email,balance,city,datetime.datetime.now()])
        print("\nAccount created successfully .. ")
        print("Your account number : ", ac)
                    

    def deposite(self):
        ac = input("Enter the account no : ")
        dip = int(input("Enter the deposite : "))

        row = []

        with open("bank_details.csv",'r') as file:
            reader = list(csv.reader(file))

            for data in reader:
                if data[0] == ac:
                    b = str(int(data[4]) + dip)
                    data[4]=b

                row.append(data)

        with open("bank_details.csv",'w',newline="") as file1:
            writer = csv.writer(file1)
            writer.writerows(row)
        
        print("\nDeposite added successfully .. ")
        print("Your bank balnace : ",b)


    def withdraw(self):
        ac = input("Enter the account no : ")
        amount = int(input("Enter the amount : "))

        row = []

        with open("bank_details.csv",'r') as file:
            reader = list(csv.reader(file))

            for data in reader:
                if data[0] == ac:
                    b = str(int(data[4]) - amount)
                    data[4]=b

                row.append(data)

        with open("bank_details.csv",'w',newline="") as file1:
            writer = csv.writer(file1)
            writer.writerows(row)
            
        print("\nBalance updated successfully .. ")
        print("Your bank balnace : ",b)

    def display_info(self):
        ac = input("Enter the account no : ")

        with open("bank_details.csv",'r') as file:
            reader = list(csv.reader(file))

            for data in reader:
                if data[0] == ac:
                    print(f"""
Account Number : {data[0]}
Name : {data[1]}
Mobile : {data[2]}
Email : {data[3]}
Balance : {data[4]}
City : {data[5]}
Account Open Date : {data[6]}
""")

while True:
    print("""
========================================================
              Bank management system
========================================================
              
            1. Create Account
            2. Add Deposite
            3. Withdraw amount
            4. display Information by Account Number
""")  
    choice = int(input("Enter choice : "))
    b = Bank()
    if choice == 1:
        b.create_account()
    elif choice == 2:
        b.deposite()
    elif choice == 3:
        b.withdraw()
    elif choice == 4:
        b.display_info()
    else:
        print("Invalid Choice")

    ch = input("Do you want to countinue enter (y/n) : ").lower()

    if ch == 'n':
        break