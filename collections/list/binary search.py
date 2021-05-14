list=[3,4,2,11,10,13,12,14,15]
list.sort()
print(list)
low=0
upp=len(list)-1
element=int(input("enter the element to search"))
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(element>list[mid]):
        low=mid+1
    elif(element<list[mid]):
        upp=mid-1
    elif(element==list[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")