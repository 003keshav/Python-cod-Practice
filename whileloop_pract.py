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
# n=16
# i=2
# while i<n:
#     if n%i==0:
#         print(i)
#     i+=1


# 13.Write a program to calculate the factorial of a number.
# n=4
# factorial=1
# while n>=1:
#     factorial*=n
#     n-=1
# print(factorial)


# 14.Write a program to find LCM of two numbers.
# a=4
# b=6
# lcm=max(a,b)
# while True:
#     if lcm%a==0 and lcm%b==0:
#         break
#     lcm+=1
# print(f"LCM of {a} and {b} is: {lcm}")


# 15.Write a program to check whether a number is Prime number or not.
# n=6
# count=0
# start=2
# while start<n:
#     if n%start==0:
#         count+=1
#         break
#     start+=1
# if count==0:
#     print("Prime number")
# else:
#     print("Not a prime number")


# 16.Write a program to print all Prime numbers between 1 to n.
# a=20
# start=2
# while start<=a:
#     i=2
#     prime=True
#     while i<start:
#         if start%i==0:
#             prime=False
#             break
#         i+=1
#     if prime:
#         print(start, end=" ")
#     start+=1
    

# 17.Write a program to find all prime factors of a number.
# n=20
# start=2 
# while start<=n:
#     if n%start==0:
#        i=2
#        prime=True
#        while i<start:
#            if start%i==0:
#                prime=False
#                break
#            i+=1
#        if prime:
#          print(start,end=" ")
#     start+=1


# 18.Write a program to check whether a number is an Armstrong number or not.
# a=371
# b=a
# am=0
# digit=0
# temp=a
# while temp>0:
#     digit+=1
#     temp//=10
# while b>0:
#     am=am+(b%10)**digit
#     b=b//10
# if am==a:
#     print("Armstrong number")
# else:
#     print("Not an armstrong number")


# 19.Write a program to check whether a number is Strong number or not
# a=145
# b=a
# sum=0
# while b>0:
#     digit=b%10
#     fact=1
#     i=1
#     while i<=digit:
#         fact*=i
#         i+=1
#     sum+=fact
#     b//=10
# if sum==a:
#     print("Strong Number")
# else:
#     print("Not an Strong Number")


# 20.Write a program to check whether a number is perfect number or not
# n=6
# i=1
# sum=0
# while i<n:
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("Perfect number")
# else:
#     print("Not a Perfect number")


# 21.Write a program to print fibonacci series upto n terms
# n=15
# a=0
# b=1
# i=1
# while i<=n:
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
#     i+=1


# 22.Write a program to find ones complement of a binary number
a="01010101"
i=0
complement=""
while i<len(a):
    if a[i]=='0':
        complement+='1'
    else:
        complement+='0'
    i+=1
print(complement)