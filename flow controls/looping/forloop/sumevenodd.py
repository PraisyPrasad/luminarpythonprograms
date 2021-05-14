low=int(input("enter a num"))
upp=int(input("enter a num"))
even=0
odd=0
for i in range(low,upp+1):
    if(i%2==0):
        even=even+i
    else:
        odd=odd+i
print("even sum  is",even)
print("odd sum is",odd)
