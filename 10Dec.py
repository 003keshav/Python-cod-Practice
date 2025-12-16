# 1. Print all even numbers from 1 to 50 using a for loop.
# for i in range(1,51):
#     if i%2==0: print(i)
# 2. Print numbers from 1 to 100 but stop the loop if the number is 37. (Use break)
# for i in range(1,101):
#     if i==37: break
#     print(i)
# 3. Print numbers 1 to 50 but skip multiples of 5. (Use continue)
# for i in range(1,51):
#     if i%5==0: continue
#     print(i)
# 4. Take a number from the user and print its multiplication table (1–10).
# num=int(input("Enter number:"))
# for i in range(1,11): print(f"{num} X {i} = {num*i}")
# 5. Count how many numbers between 1 to 100 are divisible by 7.
# count=0
# for k in range(1,101):
#     if k%7==0: count+=1
# print(count)
# 6. Print only the vowels from a string given by the user.
# s="string gIven by usEr"
# vowels='aeiouAEIOU'
# for ch in s:
#     if ch in vowels: print(ch)
# 7. Given a string, print the first 5 characters only and stop. (Use break)
# c='Given a string'
# count=0
# for v in c:
#     if count==5: 
#         count+=1
#         break

# print fibonacci series upto N terms
# a=0
# b=1
# for i in range(11):
#     print(a) 
#     a,b=b,a+b





# WHILE LOOP
# while loop is used when we don't know how many iterations we should run 
# this loop runs until the condition is false.
# n=1
# while n!=6:
#     print(n)
#     n=n+1

# n=5
# while n!=0:
#     print(n)
#     n=n-1

password='sam'
user=input("Enter password:")
while True:
    if password == user:
        print("Login Successful")
        break
    else:
        print("Invalid Password!!!")
        continue
