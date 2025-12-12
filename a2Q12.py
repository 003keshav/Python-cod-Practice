# 12. Given a list of numbers, stop printing when the number 0 is found. (Use break)
# ○ Example: [3, 4, 1, 0, 7, 9] → stop at 0
s=[3,4,1,0,7,9]
for j in s:
    if j==0: break
    print(j,end=" ")