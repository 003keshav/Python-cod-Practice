    # D 
    # C D 
    # B C D 
    # A B C D
c=68
for a in range(4):
    for b in range(a+1):
        print(chr(c+a-b), end=" ")
    print()