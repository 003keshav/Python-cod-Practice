# 1. print all natural number 1-n
# n=9
# i=1
# while i<=n:
#     print(i)
#     i+=1


# 2. print all natural num n-1
# n=9
# i=1
# while i<=n:
#     print(n)
#     n-=1


# 3. print all alphabets a-z
# i=97
# while i<=122:
#     print(chr(i))
#     i+=1


# 4. print all even num 1-100
# i=1
# while i<=100:
#     if i%2==0:
#         print(i)
#     i+=1


# 5. sum of all odd num 1-n
# n=5
# i=1
# sum=0
# while i<=n:
#     if i%2!=0:
#      sum+=i
#     i+=1
# print(sum)


# 6. count digits in num
# num='12345'
# count=0
# while count<len(num):
#     count+=1
# print(count)


# 7. calculate sum of digits of number 
# count=0
# sum=0
# n='123456' 
# while count<=len(n):
#     sum+=count%10
#     count+=1
# print(sum)


# 8. find first & last digit of number
# num=12345
# first=num
# last=num%10
# while first>=10:
#     first//=10
# print(first,last)


# 9. find sum of first & last digit of a number
# num=92843281
# first=num
# last=num%10
# while first>=10:
#     first//=10
#     sum=first+last
# print(sum)


# 10. enter number & print reverse of it
# n=1234
# rev=0
# while n>0:
#     digit=n%10
#     rev=(rev*10)+digit
#     n=n//10
# print(rev)


# 11. find power of a number 
# base=2
# power=3
# result=1
# while power>0:
#     result*=base
#     power-=1
# print(result)


# 12. find all factors of a number
n=16
i=2
while i<n:
    if n%i==0:
        print(i)
    i+=1