class College:
    collegename="LT"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def printDetails(self):
        print("collegename",self.collegename)
        print("name",self.name)
        print("roll",self.roll)
    def __str__(self):
        return self.name+str(self.roll)
ob=College("anu",4)
print(ob)