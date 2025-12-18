#         1 2 3 4 5   
#       1 2 3 4 5
#     1 2 3 4 5
#   1 2 3 4 5
# 1 2 3 4 5
st=5
for a in range(5):
    num=1
    for b in range(5+st):
        if b>=5-a-1 and b<5-a-1+st:
            print(num, end=" ")
            num+=1
        else:
            print(" ", end=" ")
    print()