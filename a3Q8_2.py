    # A B C D 
    #   A B C 
    #     A B 
    #       A 
n=4
for a in range(n):
    ch=65
    for b in range(n):
        if a<=b:
            print(chr(ch), end=" ")
            ch+=1
        else:
            print(" ", end=" ")
    print()