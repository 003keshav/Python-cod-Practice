# file handling
# machanism to handle files to read or write
'''
1 step file open
2 step file read/write
3 step file close 
'''
'''
by default read hoti h
mode--> r+
w+ -> phale ka content delete kr deta h
r -> read only
w -> write only'''
# to read a file
# f=open('data1.txt')
# print(f)
# print(f.read())
# f.close()

# to write in file 
# f=open('data1.txt',"w")
# f.write("SAm")
# f.close


# to both read and write
# f=open("data1.txt", "r+")
# out=f.read()
# f.write(" Indian Army")
# f.close
# print(out)
# print(f)

# f=open("data1.txt", "r+")
# f.write(" Indian Army")
# out=f.read()
# f.close
# print(out)

# to change curser position f.seek()
# to check curser position f.tell()

# with open('data1.txt', 'r+') as f:
#     f.write("9 Para SF")
#     print(f.read())


# with open('data1.txt', 'r+') as f:
#     for k in f:
#        print(k)


# with open('data1.txt', 'r+') as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())


# with open('data1.txt', 'r+') as f:
#     SF=f.readlines()
#     for s in SF:
#         print(s.strip())


# def file_read(filename):
#     with open(filename, "r") as f:
#         print("Inside func")
#         for line in f:
#             print(line.strip(), type(int(line.strip()) ))

# file_read("data1.txt")
# def prime_check(n):
#     count=0
#     for i in range(2,n):
#         if n%i==0:
#             count+=1
#     if count==0:
#         print(n,"Prime ")
#     else:
#         print(n, "is not prime")

# def file_read(filename):
#     with open(filename, "r") as f:
#         print("Inside func")
#         for line in f:
#             # print(line.strip(), type(int(line.strip()) ))
#             n=int(line.strip())
#             prime_check(n)


# file_read('data1.txt')