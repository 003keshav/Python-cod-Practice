'''
polymorphism:- It is basically a feature of oops where the object of class or  a method of class behave differently
poly = many or multiple & morphism= forms
method overloading: In polymorphism generally we have same method in a class but different arguments in class 
python m method overloading nhi hoti 
(interview Question)why it is not supported in python? has 2 reasons
1.because it is run time language
2.because of name spacing (Assignment: Name space)
but we can achive it approximetly by using args and kwrgs bot exactly                    
'''
# agar same class m perameters change hote h to use overloading bolte h
# class Regex:
#     def info(self):
#         print("hey")

#     def info(self, a): # it should work as method overloading
#         print("hello")

# r1=Regex()
# r1.info()

'''
method overriding when chid class have same method of parent class with same number of arguments/same signature
and because of method overriding we can achive polymorphism
Example of polymorphism by overriding
'''
# agar different class m perameters change hote h to use overriding bolte h
# class A:
#     def info(self):
#         print("A class info")

# class B:
#     def info(self):
#         print("B class info")

# b1=B()
# b1.info()


class BankAccount:
    bank_name="CBI"
    def __init__(self, acNo, ac_holder, balance):  # are local
        self.acNo=acNo
        self.ac_holder=ac_holder       # self.variable is instance
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount

    def Bank_info(self):
        print("Bank Account Info:: ", self.acNo, self.ac_holder, self.balance, self.bank_name)

# ac1=BankAccount(22082003, "Keshav", 100000)
# print("Normal Account: ", ac1.acNo, ac1.ac_holder, ac1.balance)
# # or
# ac1.Bank_info()


class SavingAccount(BankAccount): #child of bank account
    def __init__(self, s_acNo, s_ac_holder, s_balance):  # are local
        # self.acNo=s_acNo
        # self.ac_holder=s_ac_holder       # self.variable is instance
        # self.balance=s_balance
        super().__init__(s_acNo, s_ac_holder, s_balance)

    def deposit(self, amount):
        if amount>200000:
            print("we can't deposit money")
        else:
            self.balance += amount

    def sav_info(self):
        super().Bank_info() #here it taking values from saving account but function logic is calling from parent class

sa1=SavingAccount(20032208, "keshav Sukhwal", 10000)
# print("Saving: ", sa1.acNo, sa1.ac_holder, sa1.balance, sa1.bank_name)
# or
sa1.deposit(100000)
print(sa1.ac_holder, sa1.balance)


# operator overloading