# csv file write and read
try:
    import csv
    def file_read(filename):
        
            try:
                # to write data in csv file
                with open(filename, "w", newline="", encoding="utf-8") as file:
                    writer=csv.writer(file)
                    writer.writerow(["Name, Degree, Role"])
                    writer.writerow(["Keshav,B.Tech,Special Forces Operative"])
            except Exception as error:
                print("Enter error:", error)

            try:
                # to read data from csv file
                with open(filename, "r", newline="", encoding="utf-8") as file:    
                    reader=csv.DictReader(file)
                    for row in reader:
                         print(row)
            except Exception as error:
                print("Enter error:", error)

    file_read(r"D:\Vscode\python\Loops\sam.csv")
except Exception as error:
    print("Enter Error:",error)


'''
generator is kind of gunction which generate values infinetely
without loading  the complete data in memory
generator should have yield keyword 
we can say it is lazy function
'''


# pascal triangle
# n=5
# mainlist=[]
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         if k==0 or k==i:
#             print(1, end=" ")
#         else:
#             print("*", emd=" ")
    
#     print("")