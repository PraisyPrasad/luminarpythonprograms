list=[10,15,20,25,30,35,40,45,50]
element=int(input("enter elemrnt to serch")
flag=0
for i in list:
    if(i==element):
        flag=1
        break
    else:
        pass
if(flag>0):
    print("element found")
else:
    print("element not found")

