# inheritance, poly, Encapsulation
# _ : protected
# __: private

# class Bank:
#     def __init__(self, accNo, holder_name, amount):
#         self.accNo=accNo
#         self.holder_name=holder_name
#         self.__amount=amount

#     def Amount_info(self):     #getter method
#         return self.__amount
    
#     def Amount_add(self, deposit):   #setter method
#         self.__amount += deposit

# a1=Bank(2208003, 'Keshav', 1000)
# print(a1.holder_name, a1.accNo)
# print(a1.Amount_info())
# a1.Amount_add(300)
# print(a1.Amount_info())


'''
# Abstraction:
It as a feature of oop's which is use to hide unwanted features or details
to achive an abstraction we have to create an abstract method
abstract method is an method which is not implemented
to achice abstraction we have to make abstract class in which there should  be atleast 1 abstract method

'''
# from abc import ABC, abstractmethod
# # RBI abstract class inherit => abstract base class
# class RBI(ABC):   #here RBI is an abstract class jiska object nhi bana sakte
#     document='aadhar'   #class variable

#     @abstractmethod #decorator
#     def intrest_on_loan(self):
#         print("Interst will be 6%")
#         pass

# class HDFC(RBI):
#     salaryslip=True

#     def intrest_on_loan(self):
#         print("We will take 12%")

# h1=HDFC()
# h1.intrest_on_loan()
# # h2=RBI() not be implemented or not make object


'''
class book and it have book_id, the title, author, price, stock available=True
book_is is private
class student name, id, book borrow will be list
class p_detail which have id, name and same class will have method/function name as position_at_college and pass'''
class liberary:
    def __init__(self, id, name, price, book):
        self.id=id
        self.name=name
        self.price=price
        self.book=book

class book:
    def __init__(self, book_id, title, author, price, stock_avl):
        self.id=book_id
        self.name=title
        self.author=author
        self.price=price
        self.stock=stock_avl

class Person_Detail():
    def __init__(self, id, name):
        self.id=id
        self.name=name

    def position_at_college():
        pass
        
class Student(Person_Detail):
    def __init__(self, id, name, book_borrow):
        super().__init__(id, name)
        self.borrow=book_borrow
   
