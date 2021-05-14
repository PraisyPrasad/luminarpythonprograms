birthdate=int(input("enter birthdate"))
birthmonth=int(input("enter birthmonth"))
birthyear=int(input("enter birthyear"))
currentdate=int(input("enter currentdate"))
currentmonth=int(input("enter currentmonth"))
currentyear=int(input("enter currentyear"))
if currentmonth<birthmonth:
    currentyear=currentyear-1
    age=currentyear-birthyear
    print("age is",age)
elif(currentmonth==birthmonth):
  if(birthdate<=currentdate):
        age=currentyear-birthyear
        print("age is",age)
  elif(birthdate>currentdate):
        currentyear=currentyear-1
        age=currentyear-birthyear
        print("age is",age)
elif(currentmonth>birthdate):
        age=currentyear-birthyear
        print("age is",age)




