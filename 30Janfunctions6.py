# s=map( lambda a: a+10, (4,6,89,90))
# print(s)
# print(next(s))
# print(next(s) )

# or
# print(tuple(map(lambda a: a+10, (4,6,89,90))))

# print(list(map(lambda a: a+10, (4,6,89,90))))
# print(tuple(map(lambda a: a%2!=0, (4,6,89,90))))   #give true/false according to condition

# print(tuple(filter(lambda a: a%2!=0, (4,6,89,90))))   #give value which satisfy the condition




# GENERATOR:- 1.It is a function in python use to generate a value on demand
# 2. generator have a yield keyword
# 3. it is to generate a value one at a time

# def gen():
#     print("abc")
    # return 22
    # yield 22
# print(gen())
# out=gen()
# print("value of out :", out)


# def fun():
#     print("abc")
#     return 1
#     print("def")
#     yield 2
# print(fun())
# print(fun())


# def fun():
#     print("abc")
#     yield 1
#     print("def")
#     print("ghi")
#     yield 11
#     yield 111
#     return 0
# print(fun())
# gen=fun()
# print('1:',next(gen))
# print('2:',next(gen))
# print('3:',next(gen))


# def infinite():
#     n=1
#     while True:
#         return n
#         n+=1

# print( infinite())   #function will always run from 1st line
# print( infinite())


def infinite():
    n=1
    while True:
        yield n
        n+=1

gen=infinite()
print( next(gen))   #function will always run from 1st line
print( next(gen))
print( next(gen))
print( next(gen))
print( next(gen))

# Assignment:- common question of generator in interviews is fibonacci series 