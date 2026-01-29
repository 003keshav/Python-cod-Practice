# data="ABAD"
# start=0
# end=len(data)-1
# while start<len(data)-1:
#     if data[start]==data[end]:
#         print(data[start], data[end])
#     end-=1

#     if end==start:
#         end=len(data)-1
#         start+=1



n=153
total=0
while n!=0:
    x=n%10
    total+=x**3
    print(f"reminder: {x} , total:: {total}")
    n=n//10
    