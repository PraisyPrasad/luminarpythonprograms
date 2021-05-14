list=[18,4,5]
a=int(input("enter index"))
try:
    print(list[a])
except:
    print("exception")
finally:
    print("inside finally")