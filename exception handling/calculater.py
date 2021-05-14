class Calculater:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
obj=Calculater(4,2)
print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div())