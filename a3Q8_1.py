    # 1 2 3 4
    #   1 2 3
    #     1 2
    #       1
n=4
for a in range(n):
    num=1
    for b in range(n):
        if a<=b:
            print(num, end=" ")
            num+=1
        else:
            print(" ", end=" ")
    print()