'''types of methods in OOP's
1. Class Method
2. Static method
3. Instance Method
'''
class python:
    trainer='tushar sir'

    def __init__(self, st_name, st_marks):
        self.st_name=st_name
        self.st_marks=st_marks

    def std_info(self):          #instance method
        print(self.trainer, self.st_name)

    @staticmethod              #static method it can access by class name also and we don't need object to call it
    def batch_info():
        print("Start in January 2026")

    @classmethod             #class method we don't need object to call it
    def trainer_info(cls):
        print("Trainer is:", cls.trainer, cls)

class pythonA2(python):
    trainer="John Snow"
    def __init__(self, pst_name, pst_marks):
        super().__init__(pst_name, pst_marks)

ps1=pythonA2("Max", 98)
ps1.trainer_info()
s1=python("sam", 85)
s1.trainer_info()

# s1=python('sam', 85)
# s1.trainer="John Snow"
# s1.std_info()
# s2=python("Raj", 76)
# s2.std_info()
# s1.batch_info()
# python.batch_info()
