lst=[4,2,1,6,7,8]
#op 3,1,0,7,8,9
updatelst=[]
for i in lst:
    if(i<5):
        i=i-1
        updatelst.append(i)
    else:
        i=i+1
        updatelst.append(i)
print(updatelst)
result=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(result)