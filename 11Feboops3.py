# class student:
#     college='Officers Trainning Academy'  #class variable
#     def __init__(self, course, city):  #course, city are local
       
#         self.course=course #instance variable can access by object not by class
#         self.city=city   
#     def info(self):
#         print("Data is", self.course, self.city)
    
# raj=student("B.Tech", 'Chennai')
# raj.info()



# class counter:
#     count=0
#     def __init__(self):   
#         counter.count+=1
#         print("Counter value: ", self.count)
# # to do any changes in class variable we do with class name not with self or object
# # agar self ya object se change kre to vo locally hi krega bhar shoe nhi krega
# a=counter()
# b=counter()


# class Employee:
#     def __init__(self, name, email):
#         self.name=name
#         self.email=email
#     def detail(self):
#         print(self, "It has", self.name, self.email)

# abhi=Employee("Abhijeet", 'abhijeet@gmail.com')
# abhi.detail()


# inheretiance is a properties of class can be access by another class

class father: #supaar calss/ Base/ parent
    property=5
    def caretaker(self):
        print("caretaker is shyam ji guard")

# son us child which can access property of parent class (father)
class son(father):  #subclass/ derived class/ child class
    working=None
    def Enquiry(self):
        print("Who will take care of my flat")
        self.caretaker() #calling inheritance properties
        # super(). caretaker()
        super().caretaker() #calling inheritance properties mostly call by super(0)

s1=son()
print(s1.property, s1.working)
s1.Enquiry()
f1=father()
f1.caretaker()