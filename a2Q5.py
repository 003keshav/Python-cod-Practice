# 5. Count how many numbers between 1 to 100 are divisible by 7.
count=0
for k in range(1,101):
    if k%7==0: count+=1
print(count)