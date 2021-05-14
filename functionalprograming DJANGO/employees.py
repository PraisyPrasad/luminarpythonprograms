class Employee:
    def init(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def print_emp(self):
        print(self.ename)
e1=Employee(1000,"varun","developer",25000)
e2=Employee(1001,"vivek","developer",24000)
e3=Employee(1002,"vivek","qa",27000)
e4=Employee(1003,"nikil","mrkt",28000)
employees=[]
employees.append(e1)
employees.append(e2)
employees.append(e3)
employees.append(e4)
# sal=[]
# for emp in employees:
#     sal.append(emp.salary)
# print(sal)
salary=list(map(lambda emp:emp.salary,employees))
print(salary)