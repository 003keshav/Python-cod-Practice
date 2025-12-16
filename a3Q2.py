######
#    #
#    # 
######
n=6
for k in range(n):
    for l in range(n):
        if k==0 or k==n-1 or l==0 or l==n-1  :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()