# 13. Check if a given number is prime or not using a for loop.
a=237
count=0
for k in range(2,a):
    if a%k==0: count+=1
if count == 0: print("Prime Number")
else: print("Not Prime Number")