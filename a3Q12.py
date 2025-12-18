    #       *       
    #     * * *
    #   * * * * *
    # * * * * * * *
n=4
for k in range(n):
    for l in range(2*n-1):
        if l>=n-k-1 and l<=n+k-1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()