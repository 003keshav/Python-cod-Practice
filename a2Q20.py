# 20.Print the Fibonacci series up to N terms using a for loop.
n=int(input("Enter number"))
a=0
b=1
for j in range(n):
    print(a, end=" ")
    a,b=b,a+b