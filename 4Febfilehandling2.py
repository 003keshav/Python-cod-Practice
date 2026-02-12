# Assignment
'''import csv
def read_file(filename):
    with open(filename, "r", newline="", encoding="utf-8") as f:
        print("Inside func")
        reader= csv.DictReader(f)
        for row in reader:
            print(row)

read_file("fact_trip_5000 - fact_trip_5000.csv")   '''

# with open("data1.txt", "r+") as fileobj:
#     content=fileobj.read()
#     fileobj.write("keshav")
#     content=fileobj.read()

# print(content)

# with open("data1.txt", "r+") as fileobj:
#     for var in fileobj:
#         # print(var)
#         wordlist=var.split(",")
#         print(wordlist[1], wordlist[0])


# Assignment1. using csv package read the file --> written in csv format
# 2. Write the file with the new value in the same 

# EXCEPTION HANDLING :- an event or condition by which a program get terminate or give another output
# an mechanism through which we manage / handle those event
'''
to handle this 2 block
1. try: block of code jaha erroe aa saki h 
2. except: block of code by which handle the error
'''

# try:
#     x=10
#     x=x+5
#     print(x)
#     try:
#         z=x+y  # code go for except
#     except Exception as ex:
#         print("we found an error",ex)
#     print(x)
# except Exception as ex: # will give an error and it's type and run again 
#     print("we found an error",ex)

try:
    def calculate(n):
        print(f"Value is {n}")
        try:
            a=int(input("Enter a:"))
            print(f"Value is {a}")
        except Exception as error:
            print("Value of a is incorrect",error)
        print(n+25)

    calculate(1)
except Exception as error:
    print('Issue in function decleration', error)
finally:
    print("inside finally")