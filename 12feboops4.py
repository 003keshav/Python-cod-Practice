# constructor is function use to initialize the memory address for object __init__
# class Registration:
#     def __init__(self, name, age, email):
#         self.name=name
#         self.age=age
#         self.email=email

#     def userinfo(self):
#         print("User details are:", self.name, self.age, self.email)

        
# class Organization(Registration):   #child class  child(parent)
#     def __init__(self, oname, oage, oemail):
#         super().__init__()


# regex=Organization("Regex", 2020, "regex@gmail.com")




# class TataOrganization:
#     name="Tata & Sons's Organization" # class variable

#     def orginfo(self): # Instance method :- only object can run this
#         print("We are:", self.name)

# class Tatamoters(TataOrganization): #child class of tata organization
#     def motersinfo(self):           #Instance method :- only object can run this
#         print("We are Tata Moters")
#         super().orginfo()

# t1=Tatamoters()  #tata moter object
# print(Tatamoters.name)  #parent class object call with class
# print(t1.name)          #parent class object call with object
# t1.orginfo()    #parent class instance method using the object
# t1.motersinfo()

# class A classvariable company constructor m email declare  krna h
#  class B classvariable year object banage b ke ander a ki properties inharit kena h or  company name access hogi
# b class cannot access email at same moment
# b m constructor banega or self m ek paremeter banega 

# constructor chaining

# ASSIGNMENT
class A:
    name="REGex Software"
    def __init__(self, email):
        self.email=email
        print("Email is ", self.email)

class B(A):
    year=2020

s1=B()
print(s1.name)