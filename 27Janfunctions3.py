# count=0  #global variable
# def add(a,b):
#     global count
#     c=a+b    #local variable
#     count+=1
#     print(f"sum of {a} + {b} :: {c}, count::{count}")

# add(50,20)
# print(count)






# function type of argument passing
# def data(name, age, fees=5000):
#     print(f"Name: {name}, Age: {age}, fees::{fees}")

# # data() # Error because no argument is passed
# # positional argument
# data("Raj",22,35000) 
# data(25000,"Raj", 23) #will give differnt result
# # keyword argument
# data(age=22, fees=35000, name='Raj')
# # default argument
# data(age=22, name='Raj')
# data(age=22, fees=35000, name='Raj') #it overrite the default value of fees



# variable length argument or *args
# def fun(*args):
#     print(num, type(num))

# fun(10)
# fun(10,20,30,40,50)



# keyword variable length argument or **kwrgs
def fun2(**kwargs):
    print(num, type(num))

fun2(a=10,b="Sam",c=15)


# Assignment :- High Order and first class function (properties)