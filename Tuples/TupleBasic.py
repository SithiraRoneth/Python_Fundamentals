# create tuple
sports = ("Tennis","Cricket","Football")

# print with length
print(sports,"\nlenght of this sport :" , len(sports))

# type of tuple
print(type(sports))

my_tuple = ("Cat",)
print(type(my_tuple)) # without , this symbol print string but using , this symbol then print tuple

# try to change value 
sports_2 = list(sports)
sports_2[2] = "Swimming"
sports = tuple(sports_2)
print(sports,"\ntype of tuple :",type(sports))

# remove index
my_tuple_1 = (10,8,20,5)
my_tuple_2 = (5,9,-1)

my_tuple_3 = list(my_tuple_1)
my_tuple_3.pop(2)
my_tuple_1 = tuple(my_tuple_3)
print("remove index :",my_tuple_1)

# merger 2 tuples
my_tuple_4 = my_tuple_1 + my_tuple_2
print("Merge 2 tuples : ",my_tuple_4)

# sort tuple
my_tuple_5 = list(my_tuple_4)
my_tuple_5.sort()
my_tuple_4 = tuple(my_tuple_5)
print("sort this tuple :" , my_tuple_4)
