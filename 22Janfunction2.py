# def hey():
#     print("Hello future")
#     return "soldier"
# print(hey())

# def num_check(x):
#     x=int(input("Enter num"))
#     if x%2==0:
#         print("Even")
#     else:
#         print("Odd")
# print(num_check(12))



# def check_prime():
#     x=int(input("Enter num"))
#     count=0
#     for i in range(2,x):
#         if x%i==0:
#             count+=1
#             break
#         else:
#             continue
#     if count==0:
#         print(f"{x} is Prime Number")
#     else: print(f"{x} is not a Prime Number")
# print(check_prime())


# def requestnotification(x):
#     print(f"Hey user {x} you get a friend request !!!")
# user="Nikhil"
# print(requestnotification(user))



# def requestnotification(x,friendname):
#     print(f"Hey user {x} you get a friend request from {friendname}!!!")
# user="Nikhil"
# friend="Keshav"
# # print(requestnotification(user))
# print(requestnotification(user,friend))


# def add_two_num(a,b):
#     c=a+b    #c is local scope / local variable in function
#     print(f"Total of {a} and {b} is {c}")
# print(add_two_num(5,4))


# age=23 #global variable / session 
# def add_two_num(a,b):
#     c=a+b    #c is local scope variable in function
#     print(f"Total of {a} and {b} is {c} and age is {age}")
# add_two_num(10,13)
# print(f"age is {age}")


x=100
y=20
print("before function", id(x), id(y))
def add_two_num(a,b):
    print("Memory of a & b", id(a), id(b))
    a=50
    print("Update Memory of a & b", id(a), id(b))
    c=a+b    #c is local scope / local variable in function
    print(f"Total of {a} and {b} is {c}")
add_two_num(x,y)