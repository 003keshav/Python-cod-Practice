# for a in range(1,5):
#     print("Student::",a)

#     for b in range(1,5-a+1):
#         print("Assin:",b,end=" ")
    
#     print("")


# ****
# ****
# ****
# ****
# for a in range(1,5):
#     for b in range(1,5):
#         print("*",end="")

#     print("")


# 1111
# 2222
# 3333
# 4444
# for a in range(1,5):
#     for b in range(1,5):
#         print(a,end="")

#     print("")


# 444
# 333
# 222
# for a in range(1,4):
#     for b in range(1,4):
#         print(4-a+1,end="")

#     print("")


# 123
# 123
# 123
# for a in range(1,4):
#     for b in range(1,4):
#         print(b,end="")

#     print("")


# 4321
# 4321
# 4321
# for a in range(1,4):
#     for b in range(1,4+1):
#         print(4-b+1,end="")

#     print("")


# 123
# 456
# 789
# k=1
# for a in range(1,4):
#     for b in range(1,4):
#         print(k,end="")
#         k+=1
#     print("")


# 7654
# 7654
# 7654
# 7654
# for a in range(1,4+1):
#     k=7
#     for b in range(1,4+1):
#         print(k,end="")
#         k-=1
#     print("")


# 65 66 67 
# 65 66 67
# 65 66 67
# for a in range(1,4):
#     k=65
#     for b in range(1,4):
#         print(k,end=" ")
#         k+=1
#     print("")


# ABCD
# ABCD
# ABCD
# for a in range(1,4):
#     ch=65
#     for b in range(1,4+1):
#         print(chr(ch),end="")
#         ch+=1

#     print("")


# ABC
# ABC
# ABC
# for a in range(1,4):
#     ch=65
#     for b in range(1,4):
#         print(chr(ch),end="")
#         ch+=1

#     print("")


# ABC
# DEF
# GHI
# ch=65
# for a in range(1,4):
#     for b in range(1,4):
#         print(chr(ch),end="")
#         ch+=1

#     print("")


# * 
# * *
# * * *
# * * * *
# for a in range(1,5):
#     for b in range(1,a+1):
#         print("*",end=" ")
#     print("")


# * * * * 
# * * *
# * *
# *
# for a in range(1,5):
#     for b in range(1,5-a+1):
#         print("*",end=" ")
#     print("")


# 2 3 4 5 
# 2 3 4
# 2 3
# 2
# for a in range(1,5):
#     for b in range(1,5-a+1):
#         print(b+1,end=" ")
#     print("")


# 1 2 3 4 
# 1 2 3
# 1 2
# 1
# for a in range(1,5):
#     for b in range(1,5-a+1):
#         print(b,end=" ")
#     print("")


# A 
# B C
# D E F
# G H I J
# ch=65
# for a in range(1,5):
#     for b in range(1,a+1):
#         print(chr(ch),end=" ")
#         ch+=1
#     print("")


# A 
# A B
# A B C
# A B C D
# for a in range(1,5):
#     ch=65 
#     for b in range(1,a+1):
#         print(chr(ch),end=" ")
#         ch+=1
#     print("")


# 1 2 3 4 
# 2 3 4
# 3 4
# 4
# s=1
# for a in range(1,5):
#     temp=s
#     for b in range(1,5-a+1):
#         print(temp,end=" ")
#         temp+=1
#     s+=1    
#     print("")


# 1 0 1 0 1 
# 1 0 1 0
# 1 0 1 
# 1 0
# 1
# for a in range(1,6):
#     for b in range(1,6-a+1):
#         if b%2!=0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
            
#     print("")



# A 1 B 2 C 3 
# D 4 E 5
# F 6
# s=1
# ch=65
# for a in range(1,4):
#     temp=s
#     for b in range(1,4-a+1):
#         print(chr(ch),s,end=" ")
#         ch+=1
#         s+=1
            
#     print("")



# 1 2 3 4 5 
# 3 4 5 6
# 5 6 7
# 7 8
# 9
s=1
for a in range(1,6):
    temp=s
    for b in range(1,6-a+1):
        print(temp,end=" ")
        temp+=1
    s+=2    
    print("")
