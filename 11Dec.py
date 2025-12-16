# reverse a number
# a=123
# rev=0
# while  a!=0:
#     digit = a%10
#     rev = rev*10+digit
#     a=a//10
# print(rev)    

# count the n0 of digits in a given number
# a=123
# count=0
# while a!=0:
#     a = a // 10
#     count+=1
# print(count)

# calculate a factorial of given number using the while loop
# a=5
# fact=1
# while a>0:
#     fact=fact *a
#     a-=1
# print(fact)   

# Password login
# password='abc'
# while True:
#     user=input("Enter your password")
#     if user == password:
#         print("Login Successful")
#         break
#     else:
#         print("Invaild Password!!!")

# fibonacci series
# a=0
# b=1
# while a!=11:
#     print(a)
#     a,b == b, a+b

# check whether a number is palindrome or not?
a=121
rev=0
while a!=0:
    digit=a%10
    rev=rev*10+digit
    a=a//10
if rev==a:
    print("Number is Palindrome")