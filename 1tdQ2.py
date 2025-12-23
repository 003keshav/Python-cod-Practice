# 2. run loop 400-250 & count num divisible by 11&13
count=0
for a in range(400,250,-1):
    if a%11==0 and a%13==0:
        count+=1
print(count)