# prime number
# n=5
# count=0
# for k in range(2,n):
#     if n%k==0:
#         count+=0
# if count==0:
#     print("Prime number",n)
# else:
#     print("Not Prime",n)

# a=1
# while a>5:
#     print(a)
#     a+=1

n=6
a=5
count=0
while a>1:
    if a%n==0:
        count+=1
    a-=1
if count==1:
    print("Prime")
else:
    print("not Prime")