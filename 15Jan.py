# Dictionary: A data type to store data in key values
# there is no index 
# keys - unique data/identifier for values
# values - where data is stored and access it with keys
# Dict. are mutuable
# Example:- {book_pageno.(key):chapter(value)}
# we can update value by key and with unique key we can add new value
# Company={101:"Sam",102:"raj",103:"sam"}
# print(Company[102])
# Company[104]="Raju" #we can insert new key and value
# print(Company)
# Company[103]="Samarth" #to update the value
# print(Company)
# Company.pop(103) #to delete we need to give key either it will give error
# print(Company)
# # pop return only value and pop item return both key and values
# x=Company.popitem() #to use popitem we don't use key it only use for last key-values
# print(x)
# print(Company.keys())
# print(Company.items())

# loop type1
# user={101: 'Sam', 102: 'raj', 103: 'Samarth', 104: 'Raju'}
# for i in user:
#     print(i,user[i])

# loop type2
# user={101: 'Sam', 102: 'raj', 103: 'Samarth', 104: 'Raju'}
# for i in user.items():
#     print(i, i[0], i[1])

# loop type3
# user={101: 'Sam', 102: 'raj', 103: 'Samarth', 104: 'Raju'}
# for i in user.values():
#     print(i)

# to make an change in dictionary
user={"salary": 120}
user["salary"]=user["salary"]+100
print(user)