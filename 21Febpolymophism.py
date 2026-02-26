# operator overloading
# class A:
#     var="hey"
    
#     def __add__(self, x):
#         print("Calling the add method", self, x)

# a1=A()
# print(a1)
# a2=A()
# print(a2)

# a1+a2
# a1+10
# a2+"hello"

# Encapsulation :-
'''where we try to bind method and variables together
mainly focus to give excess to methods or data
4 keywords:- public, private, protected, default'''
class A:
    _amount=100   # if we add "_" in start of variable it act as protected variable
    __balance=7000000  # if we add "__" in start of variable it act as private variable
    # to access private variable __var => _classname__varname

class B:
    salary=200
    print("inside B class",A._amount)
    print("inside B class", A._A__balance)

a1=A()
print(a1._A__balance, a1._amount)
# here we are accessing both protected and private variable from another class without any relation with variable class

# getter and setter method are used with private method
