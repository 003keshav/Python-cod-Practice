# first class function
# def test(num):
#     print(num+10)
# x=test #first class function
# print(f"x:{x}")
#       #or
# x=lambda num: num+10  #first class function
# print(f"x:{x}")

# note:- x=test() not a first class function it will call the function

# student={"isha":[10,20,30,40], "yash":[90,8,5,254,245]}
# finding average of list values
# def avg(newlist):
#     print(f"Average: {sum(newlist)/len(newlist)}")

# for i in student:
#     print(i, student[i])  #print dictionary values
#     # avg(student[i])   #calling function
#     b=lambda newlist: {sum(newlist)/len(newlist)}
#     print(b(student[i]))


# def square(num):
#     print(num**2)
# square(5)
      #or
# a=lambda num: num**2
# print(a(5))

# MAP:-
# 1. It is high order function which take another function as argument
# 2. map(func_name, iterable)
# 3. it is lazy, so that memory can use in an efficient way

# d=map(len, ["heyuser", "Sam"])
# print("1st:",next(d))
# print('2nd:',next(d))

# def cube(num):
#     return num**3
# d=map(cube, [3,5,7,9])
# d=map(lambda num: num**3, [3,5,7,9])
# print('1st:', next(d))
# print('2nd:', next(d))
# print('3rd', next(d))
# print('4th', next(d))