# High Order Function and First Class Function
# first class function :-
#1. which can be assign in any variable
# def func():
#     print("hello")

# x=func  #here func() is a first class function
# x()
# print(f"x value:: {x}")
# func()


# def add(num): #step2
#     print(num+20) #step3
#     return num+20

# x=add(81) #step1
# print("x values",x)



#2. assign in data structure
# def sample():
#     print("ReGex")
# mylist=[10,20,30,sample]
# print(mylist[-1]())



#3. if we pass a function  to another function as a argument
# def add(a,b):
#     print(a+b)
# def add2(x,y):
#     print(f"x:{x}, y:{y}")
# add2(30,add(20,40))



#4. 
# def add(a,b):
#     print(a+b)
# def add2(x,y):
#     print(f"x:{x}, y:{y}")
#     print(y(20,40))
# add2(30,add)


# all High Order Functions are First Class Functions 
# but not all the first class functions are high order functions


'''lambda function is like normal function
1.start with lambda keyword
2.annynomous function bz they don't have name
3.use to make code redable
4.1- line function / syntax is small / amd use and throw

lanbda paremeter1, per2.... : expression
lanbda pareneter : expression

def func()
'''

a=lambda square: num*num
print(a(7))


'''Assignment -
 1. Generator
2. Map and filter
'''