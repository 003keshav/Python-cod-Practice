# for a in range(2*4-1):
#     if a<5:
#         for b in range(4-a):
#             print("*", end=" ")
#     else:
#         for b in range():
#             print("*", end=" ")
#     print()


# n=4
# for k in range(n+1):
#     for l in range(2*n):
#         if l>=n-k-1 and l<=n+k-1 :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#         * * * * 
#       * * * *
#     * * * *
#   * * * *
# for i in range(4):
#     for j in range(4-i):
#         print(" ", end=" ")
#     for j in range(4):
#         print("*", end=" ")
#     print()


        #
      #   #       
    #       #     
  #           #   
# # # # # # # # # 
for k in range(4+1):
    for l in range(2*4+1):
        if l==4-k or k==4 or l==4+k :
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()