class Employee:
    employeename="sam"
    def __init__(self,eid,salary):
        self.eid=eid
        self.salary=salary
    def printdetails(self):
        print("employeename",self.employeename)
        print("eid",self.eid)
        print("salary",self.salary)
    def __str__(self):
        return str(self.eid)
ob=Employee(1001,2000)
print(ob)