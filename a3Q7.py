    #       1
    #     1 2
    #   1 2 3
    # 1 2 3 4
n=4
for a in range(n):
    num=1
    for b in range(n):
        if b>=n-a-1:
            print(num, end=" ")
            num+=1
        else:
            print(" ", end=" ")
    print()