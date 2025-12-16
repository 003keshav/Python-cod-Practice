    ####
     ####
      ####
       ####
for k in range(4):
    for l in range(4+k):
        if k>l:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()