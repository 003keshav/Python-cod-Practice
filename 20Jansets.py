# Set is a data type
# myset=set({})  #for empty set
# print(type(myset)) 

# set are unordered (there is no index positions)
myset={4,6,"sam"} #for data variable
print(type(myset))
print(myset)

myset.add(22) # to add single value at any position
print(myset)
myset.update("hey") #to add Iterable
print(myset)
myset.remove(4)   # to delete
print(myset)
# to delete the element --> will not give error if element is not present
myset.discard("abc")
print(myset)

myset2={4,5,6,7,8,9,10}
# myset.union(myset2)
# myset.intersection(myset2)
print(myset.union(myset2))
print(myset.intersection(myset2))
print(myset.difference(myset2))
print(myset2.difference(myset))
help(set)