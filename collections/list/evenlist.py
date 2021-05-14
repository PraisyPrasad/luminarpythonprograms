list=[]
evenlist=[]
oddlist=[]
for i in range(50,201):
    list.append(i)
    if(i%2==0):
        evenlist.append(i)
    else:
        oddlist.append(i)
print(list)
print(evenlist)
print(oddlist)