class Prob:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name:",self.name)
        print("age:",self.age)
    def __str__(self):
        return self.name
f=open("prob",'r')
for line in f:
    data=line.split(",")
    #print(data)
    name=data[0]
    age=data[1]
    obj=Prob(name,age)
    print(obj)
    obj.printvalue()
