# for i in (1,6):
#     for j in range(1,5-i+1):
#         print("-",end="")
        
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print("")


# for i in range(1,6):
#     for j in range(1,i):
#         print(" ",end="")
#     for k in range(1,6-i+1):
#         if k==1 or i==1 or k==6-i+1:
#             print("*", end=" ")
#         else:
#             print("",end="")
#     print("")



# for i in range(1,6):
#     for j in range(2*i):
#         print("*", end=" ")
#     for k in range()
#     print("")

# n=4
# for k in range(n):
#     for l in range(2*n-1):
#         if l>=n-k-1 and l<=n+k-1 :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

a=[10,20,30,40]
print(a,type(a))
a[0]=45
print(a)
a.append(100)
print(a)
# extend function Iterable value lega
# Iterable a datatype on which we can run for loop
# Iterables are list, String, set, dict
a.extend([101,"hey"])
a.extend("sam")
print(a)
