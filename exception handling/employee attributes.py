class Employee:
    cname="luminar"
    def __init__(self,ename,eid,esalary):
        self.ename=ename
        self.eid=eid
        self.esalary=esalary
    def printvalue(self):
        print("ename:",self.ename)
        print("eid:",self.eid)
        print("esalary:",self.esalary)
        print(Employee.cname)
emp=Employee("rahul",1001,20000)
emp.printvalue()

