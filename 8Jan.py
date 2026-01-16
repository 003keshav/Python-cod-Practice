# a=[1450,4540,3045,445,5450]
# b=a.pop(2)
# print(a)
# print(b)
# a.sort(reverse=True)
# print(a)

# minimum number
# a=[100,500,600,800,50]
# b=a[0]
# for k in a:
#     if b>k:
#         b=k
# print(b)


# maximum number
# a=[100,500,6000,800,50]
# b=a[0]
# for k in a:
#     if b<k:
#         b=k
# print(b)


# a=[100,54,65,80,503]
# c=[]
# for k in a:          #for k in range(0,len[a]):
#     if k%5==0:           #if len[a]%5==0
#         c.append(k)
# print(c)


# duplicate with 2 pointer approch
# a=[123,500,60,400,60]
# b=0
# c=len(a)-1
# d=[]
# while b<c:
#     if a[b]==a[c]:
#         d.append(a[b])
#     c-=1
#     if b==c:
#         c=len(a)-1
#         b+=1
# print(d)



# find sum of 2 number is 9.
# a=[1,2,4,7,14,17,32]
# start=0
# end=len(a)-1
# while(start<end):
#     if a[start]+a[end]==9:
#         print(a[start],a[end])
#         break
#     end-=1
#     if start==end:
#         end=len(a)-1
#     start+=1



# find max profit
# a=[10,3,7,14,13]
# profit=0
# x=0
# y=len(a)-1
# while x<y:
#     if profit<a[y]-a[x]:
#        profit=a[y]-a[x]
#     y-=1
#     if x==y:
#         y=len(a)-1
#         x+=1
# print(profit)