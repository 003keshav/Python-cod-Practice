# Beginner
# 1. Write a Python program to find the maximum element in a list of numbers without max functions
# num=[10,20,444,45,99]
# max=num[0]
# i=1
# while i<len(num):
#     if num[i]>max:
#         max=num[i]
#     i+=1
# print(max)


# 2. Write a Python program to sum all the elements in a list of numbers.
# n=[10,20,30,40]
# sum=0
# for k in n:
#     sum+=k
# print(f"Sum of numbers present in list is: {sum}")


# 3. Write a Python program to reverse a list without reverse or slicing operator
# num=[1,2,3,4,5]
# rev=[]
# i=len(num)-1
# while i>=0:
#     rev.append(num[i])
#     i-=1
# print(rev)


# 4. Write a Python program to sort a list in ascending order without sort functions
# a=[1,5,7,94,3456,367,45789,89,704,34,2]
# i=len(a)
# for k in range(i-1):
#     for l in range(k+1,i):
#         if a[k]>a[l]:
#             a[k],a[l]=a[l],a[k]
# print(a)