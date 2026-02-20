# class A:
#     var1=100

# class B(A):
#     def __init__(self, var2):
#         self.var2=var2
        

# b1=B(1500)
# print(b1.var1, b1.var2)

# class BankAccount:
#     bank_name="CBI"
#     def __init__(self, acNo, ac_holder, balance):  # are local
#         self.acNo=acNo
#         self.ac_holder=ac_holder       # self.variable is instance
#         self.balance=balance

#     def Bank_info(self):
#         print("Bank Account Info:: ", self.acNo, self.ac_holder, self.balance, self.bank_name)

# # ac1=BankAccount(22082003, "Keshav", 100000)
# # print("Normal Account: ", ac1.acNo, ac1.ac_holder, ac1.balance)
# # # or
# # ac1.Bank_info()


# class SavingAccount(BankAccount): #child of bank account
#     def __init__(self, s_acNo, s_ac_holder, s_balance):  # are local
#         # self.acNo=s_acNo
#         # self.ac_holder=s_ac_holder       # self.variable is instance
#         # self.balance=s_balance
#         super().__init__(s_acNo, s_ac_holder, s_balance)

#     def sav_info(self):
#         super().Bank_info() #here it taking values from saving account but function logic is calling from parent class

# sa1=SavingAccount(20032208, "keshav Sukhwal", 10000)
# # print("Saving: ", sa1.acNo, sa1.ac_holder, sa1.balance, sa1.bank_name)
# # or
# sa1.sav_info()

# Assignment1
'''class grandfather:
    a=100

class father(grandfather):
    b=200

class son(father):
    c=300

s=son()
print(s.c,s.b,s.a)
f=father()
print(f.a,f.b)
g=grandfather()
print(g.a)'''

# Assignment2
'''class grandfather:
    def __init__(self):
        print("Grandfather's constructor")

class father(grandfather):
    def __init__(self):
        print("father's constructor")
        super().__init__()

class son(father):
    def __init__(self):
        print("son's constructor")
        super().__init__()

s=son()
print(s)
f=father()
print(f)
g=grandfather()
print(g)'''

# Assignment3
class A:
    age=18

class B:
    age=20

class C(A,B):
    year=2026

c1=C()
print(c1.year,c1.age,c1.age)