class Employee:
    def __init__(self,name,emp_no):
        self.name=name
        self.emp_no=emp_no
    def display(self):
        print("NAME:",self.name)
        print("EMPLOYEE NUMBER:",self.emp_no)
class Manager(Employee):
    def __init__(self,emp_no,name,age,salary,deptt):
        Employee.__init__(self,name,emp_no)
        self.age=age
        self.salary=salary
        self.deptt=deptt
    def displayData(self):
        Employee.display(self)
        print("AGE:",self.age)
        print("SALARY",self.salary)
        print("DEPARTMENT",self.deptt)
class Clerk(Employee):
    def __init__(self,emp_no,name,age,salary,deptt):
        Employee.__init__(self,name,emp_no)
        self.age=age
        self.salary=salary
        self.deptt=deptt
    def displayData(self):
        Employee.display(self)
        print("AGE:",self.age)
        print("SALARY",self.salary)
        print("DEPARTMENT",self.deptt)
M=Manager(345671,"nikhil",34,78000,"HR")
M.displayData()
C=Clerk(119834,"ankit",36,8900,"finance")
C.displayData()
