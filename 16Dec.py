    # * * * * 
    # *     *
    # *     *
    # * * * *
# for k in range(4):
#     for l in range(4):
#         if k==0 or k==4-1 or l==0 or l==4-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


    #       *       
    #     * * *
    #   * * * * *
    # * * * * * * *
# n=4
# for k in range(n):
#     for l in range(2*n-1):
#         if l>=n-k-1 and l<=n+k-1 :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


    # * 
    # * *
    # *   *
    # * * * *
# for a in range(4):
#     for b in range(a+1):
#         if b==0 or a==b or a==4-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


for a in range(4):
    for b in range(4):
        if a==4-1 or b==4-1 or b==4+1-a:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
