# Object Oriented programming
'''
Object:- Real Time Entity which have characteristics and behaviour and these are defined
class is blue print which can have multiple objects.
classes are define for object
class - object have one to many relationship
'''


# class home:
#     rooms=4  #characterstic (these are called class variable)
#     colour='white'

# # class variable can acessed by both class and object
# # object refer class variable do not store them

# # variable --> object
# # object --> class name() 
# villa=home()
# villa.colour='cremish'
# print('villa',villa.rooms, villa.colour)   #objectname.variablename

# home.colour='blue'
# house=home()
# print("house",house.rooms,house.colour)

# home.rooms=7
# banglow=home()
# print("banglow",banglow.rooms,banglow.colour)


class home:
    rooms=4  
    colour='white'

villa=home()
villa.colour='cremish'
print('villa',villa.rooms, villa.colour)


home.rooms=7
banglow=home()
print("banglow",banglow.rooms,banglow.colour)



house=home()
print("house",house.rooms,house.colour)

'''assignment
1. features of opps polimorphizm, encapulation etc
2. constructure
'''