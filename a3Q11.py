#         A B C D E   
#       A B C D E     
#     A B C D E
#   A B C D E
# A B C D E      
st=5
for a in range(5):
    ch=65
    for b in range(5+st):
        if b>=5-a-1 and b<5-a-1+st:
            print(chr(ch), end=" ")
            ch+=1
        else:
            print(" ", end=" ")
    print()