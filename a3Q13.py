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