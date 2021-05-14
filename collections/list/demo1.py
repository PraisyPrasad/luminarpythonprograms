# list=[10,10,20,20,25,25,85,41,41,25,58]
# list1=set(list)
# print(list1)
employee=[[1001,"arjun",15000],
          [1002,"arun",20000],
          [1003,"vinu",25000],
          [1004,"binu",30000]]
#print(employee)
# for i in employee:
#     print(i)
# for i in employee:
#     print(i[1])
# for i in employee:
#     if(i[2]>17000):
#         print(i[1])
sum=0
for i in employee:
    sum=sum+i[2]
print(sum)
