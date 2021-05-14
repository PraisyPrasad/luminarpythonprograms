from functools import reduce
lst=[10,20,30,50,80]
total=reduce(lambda no1,no2:no1+no2,lst)
mx=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(mx)
print(total)
min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)
# if(no<0):
#     return -ve
# else: