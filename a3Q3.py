    # A 
    # AB 
    # ABC 
    # ABCD 
ch=65
for k in range(4):
    for l in range(k+1):
        print(chr(ch+l), end=" ")
    print()