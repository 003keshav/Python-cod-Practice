# 5 4 3 2 1 
#   4 3 2 1 
#     3 2 1 
#       2 1 
#         1
# for i in range(1,6):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for k in range(6-i,0,-1):
#         print(k,end=" ")   
#     print("")


# * * * * * * 
# *       *
# *     *
# *   *
# * *
# *
# for k in range(1,7):
#     for l in range(1,7-k+1):
#         if l==1 or 7-k==l or k==1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")


# * * * * * * 
#   *       *
#     *     *
#       *   *
#         * *
#           *
# for k in range(1,7):
#     for l in range(1,7):
#         if k==1 or l==6 or k==l:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")


for k in range(1,7):
    for l in range(1,7):
        if l==6 or k==6 or l==6-k+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")