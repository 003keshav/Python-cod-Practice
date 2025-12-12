# 7. Given a string, print the first 5 characters only and stop. (Use break)
c='Given a string'
count=0
for v in c:
    print(v)
    count+=1
    if count==5:
        break