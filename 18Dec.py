#       1 
#     2 3 2
#   3 4 5 4 3
# 4 5 6 7 6 5 4
n=4
temp=0
for a in range(1,n+1):
    temp+=1
    for b in range(n-a):
        print(" ", end=" ")
    for b in range(temp,temp+a):
        print(b, end=" ")
    for k in range(temp+a-1,temp,-1):
        print(k-1, end=" ")
    print()

         
