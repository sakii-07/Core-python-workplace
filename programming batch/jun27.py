# class Mobile:
#     def __init__(self, n, p):
#         self.name = n
#         self.price = p

#     def calling(self):
#         print("Calling")

#     @staticmethod()
#     def watching(a):
#         print("Watching", a)

#     def show_details(self):
#         print("Mobile name : ", self.name)
#         print("Mobile price : ", self.price)

# m = Mobile("Readme",23000)
# m.watching("Movie")
# m.calling()
# m.show_details()


# Employee payroll system
class employee:

    def __init__(self,id,n,s):
        self.emp_id = id
        self.name= n
        self.salary = s

    def cal_alloances(self):
        HRA = self.salary * 0.20
        DA = self.salary * 0.10

        return HRA, DA
    
    def cal_gross_salary(self):
        hra, da =self.cal_alloances()

        sal = self.salary + hra + da
        return sal
    
    def cal_net_salary(self):
        sal = self.cal_gross_salary()
        gross = sal - sal*0.10
        return gross
    
    def display_payslip(self):
        print("Employee ID : ", self.emp_id)
        print("Employee Name : ", self.name)

        print("Basic salary : ", self.salary)

        hra,da = self.cal_alloances()
        print("HRA : ",hra)
        print("DA : ", da)

        gross = self.cal_gross_salary()
        print("Gross Salary : ", gross)

        net_sal = self.cal_net_salary()
        print("Net salary : ", net_sal)

        

e = employee(101,"Sakshi Jagtap", 50000)
e.display_payslip()   
