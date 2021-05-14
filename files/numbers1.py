f=open("numbers","r")
# for lines in f:
#     print(lines)
evenlist=[]
oddlist=[]
for num in f:
    if(num%2==0):
        evenlist.append(int(num.rstrip("\n")))
    else:
        oddlist.append(int(num.rstrip("\n")))
print("evenlist is:",evenlist)
print("oddlist is:",oddlist)
print("evenlist sum=",sum(evenlist))
print("oddlist sum=",sum(oddlist))


