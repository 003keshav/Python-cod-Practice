# tuple
# a=(10,20,30)   #a=10,20,30
# print(a,id(a))
# a.index(20)

# b=60,40,50
# print(b,type(b))
# a=a+b
# print(a,id(a))
# if memory addresss is change after an change  we call it mutable
# a=[10,20]
# print(a,id(a))
# a.append(30)
# print(a,id(a))
# if memory address is not change after change we call it immutable


# List Comphrencsion: A simple way to create a new list.
# k=[i**2 for i in range(1,10) ]
# print(k)

# List
# k=[]
# for i in range(1,10):
#     k.append(i**2)
# print(k)

# List Comphrension in nested loop.
# k=[(i,j) for i in range(1,5) for j in range(1,5)]
# print(k)

# new=[]
# for i in range(5,10):
#     temp=[]
#     temp.append(i)
#     new.append(temp)
#     print(new)

# a="575"
# new=[]
# for i in range(len(a)):
#     temp=[]
#     temp.append(int(a[i]))
#     new.append(temp)
#     print(new)

# x=5
# new=[]
# for i in range(1,4):
#     temp=[]
#     for j in range(1,i+1):
#         temp.append(x)
#         x+=1
#     new.append(temp)
#     print("")
# print(new)




for i in range(1,5):
    temp=[]
    x=1
    for j in range(1,i+1):
        temp.append(x)
        x+=1
    print(temp)
    print("")
    