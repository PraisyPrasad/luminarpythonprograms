class Vehicle:
    vehiclename='Bus'
    def details(self,vname):
        self.vname=vname
        print("vehicle name is",Vehicle.vehiclename)
class Bus(Vehicle):
    def details2(self,bnum):
        self.bnum=bnum
        print("vehicle is",Vehicle.vehiclename)
        print(self.vname)
        print(self.bnum)
ob=Bus()
ob.details(Bus)
ob.details2(34567)
