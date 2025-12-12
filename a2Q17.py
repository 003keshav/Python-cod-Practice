# 17. Print numbers 1–30; if a number is divisible by both 4 and 6, then stop. (Use break)
for j in range(1,31):
    if j%4==0 and j%6==0: break
    print(j)