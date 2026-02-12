# class home:
#     rooms=4  
#     colour='white'

#     def info(self):
#         print("Values:", self.rooms, self.colour)

# villa=home()
# villa.colour='golden'
# villa.info()


# h2=home()
# h2.info()


# constructor is an method use to initialize memory address for an object
# class home():
#     def __init__(self): #sef is variable that reffers to current object reference
#         print("Calling constructor",self)  # we can use another variable then self but we not do for gerneralization
    
# h1=home() #h1 is variable also known as object
# print("h1 memory:",h1)

# h2=home()
# print("h2 memory:",h2)


class home():
    def __init__(self, colour, rooms):
        # self.colour='white'
        # print("Colour is:", self.colour)
        print("Colour is:", colour)
        self.colour=colour
        print("Rooms are:", rooms)
        self.rooms=rooms

h1=home("cremish",7)
print("h1:",h1.colour)
print("h1:",h1.rooms)


h2=home("golden",4)
print("h2:",h2.colour)
print("h2:",h2.rooms)
