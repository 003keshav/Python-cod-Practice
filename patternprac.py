    ####
     ####
      ####
       ####
# for k in range(4):
#     for l in range(4+k):
#         if k>l:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()


######
#    #
#    # 
######
# n=6
# for k in range(n):
#     for l in range(n):
#         if k==0 or k==n-1 or l==0 or l==n-1  :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


    # A 
    # AB 
    # ABC 
    # ABCD 
# ch=65
# for k in range(4):
#     for l in range(k+1):
#         print(chr(ch+l), end=" ")
#     print()


    # A
    # B B 
    # C C C 
    # D D D D 
# ch=65
# for k in range(4):
#     for l in range(k+1): 
#         print(chr(ch+k), end=" ")
#     print()


    # D 
    # C D 
    # B C D 
    # A B C D
# c=68
# for a in range(4):
#     for b in range(a+1):
#         print(chr(c+a-b), end=" ")
#     print()


          #
        # #
      # # #
    # # # #
# for a in range(4):
#     for b in range(4):
#         if b>=4-a-1:
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


    #       1
    #     1 2
    #   1 2 3
    # 1 2 3 4
# n=4
# for a in range(n):
#     num=1
#     for b in range(n):
#         if b>=n-a-1:
#             print(num, end=" ")
#             num+=1
#         else:
#             print(" ", end=" ")
#     print()


    # 1 2 3 4
    #   1 2 3
    #     1 2
    #       1
# n=4
# for a in range(n):
#     num=1
#     for b in range(n):
#         if a<=b:
#             print(num, end=" ")
#             num+=1
#         else:
#             print(" ", end=" ")
#     print()


    # A B C D 
    #   A B C 
    #     A B 
    #       A 
# n=4
# for a in range(n):
#     ch=65
#     for b in range(n):
#         if a<=b:
#             print(chr(ch), end=" ")
#             ch+=1
#         else:
#             print(" ", end=" ")
#     print()


        # # # # #   
      # # # # #
    # # # # #
  # # # # #
# # # # #
# st=5
# for a in range(5):
#     for b in range(5+st):
#         if b>=5-a-1 and b<5-a-1+st:
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#         1 2 3 4 5   
#       1 2 3 4 5
#     1 2 3 4 5
#   1 2 3 4 5
# 1 2 3 4 5
# st=5
# for a in range(5):
#     num=1
#     for b in range(5+st):
#         if b>=5-a-1 and b<5-a-1+st:
#             print(num, end=" ")
#             num+=1
#         else:
#             print(" ", end=" ")
#     print()


#         A B C D E   
#       A B C D E     
#     A B C D E
#   A B C D E
# A B C D E      
# st=5
# for a in range(5):
#     ch=65
#     for b in range(5+st):
#         if b>=5-a-1 and b<5-a-1+st:
#             print(chr(ch), end=" ")
#             ch+=1
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


        #
      #   #       
    #       #     
  #           #   
# # # # # # # # # 

# for k in range(4+1):
#     for l in range(2*4+1):
#         if l==4-k or k==4 or l==4+k :
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


