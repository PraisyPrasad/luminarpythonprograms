class Parent:
    def properties(self):
        print("10 lack rs,2 car")
    def marry(self):
        print("with ram")
class Child(Parent):
    def marry(self):
        print("with ram")
per=Child()
per.marry()