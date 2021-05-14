age=int(input("enter age"))
sex=int(input("enter sex:M/F"))
martialstatus=int(input("are u married:Y/N"))
if(sex==F):
    print("works in urban area")
elif(sex==M):
    if(age>20)&(age<40):
    print("may work anywhere")
elif(sex==M):
    if(age>40)&(age<60):
    print("work in urban")
else:
    print("error")
