    # A
    # B B 
    # C C C 
    # D D D D 
ch=65
for k in range(4):
    for l in range(k+1): 
        print(chr(ch+k), end=" ")
    print()