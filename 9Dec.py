# check whether the number is prime or not
# n=int(input("Enter an number:"))
# It has 2 factors -> 1,self
# is_prime= True
# Here we're checking the number whether the number is greater then 1
# if n > 1:
    # then we 
    # for i in range(2, n):
        # if n % i == 0:
            # is_prime = False
    # if is_prime:
    #    print("This is a prime number")
    # else: print("This is not a prime number")

# another method
# n=6
# count=0
# for i in range(2,n):
#     if n%i==0:
#         count+=1
# if count>0: print("Not a prime") 
# else: print("Prime number")       

# factorial
# num=6
# fact=1
# for r in range(6,0,-1):
#     fact*=r
#     print("factorial is:",fact)

# Continue statement is used to skip current iteration on the certation condition
# for i in range(1,6):
#     if i==3: continue 
#     print(i)

# break statement is used to break the loop on the basis of the certaion cendition 
# for j in range(1,6):
#     print(j)
#     if i==6:
#         break

for i in range(1,21):
    if i==15: continue
    print(i)