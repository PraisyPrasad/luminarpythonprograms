class Addition:
    def initial(self,a,b):
        self.a=a
        self.b=b
        s=a+b
        return s
a=int(input("enter first num"))
b=int(input("enter second num"))
obj=Addition()
s=obj.initial(a,b)
print("sum is",s)

