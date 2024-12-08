#  create dictionary
dict_1 = {
    "name":"sugar",
    "weight":"1kg",
    "price":145.70
}
print(dict_1,"\n",type(dict_1),"\nlength of this dict_1:",len(dict_1))

# access single item usin key
print(dict_1["weight"])

# data types
my_dict = {
    "name":"John",
    "age":30,
    "is_student":False,
    "grades":[85,90,76],
    "cordinates":[12,23,56,78]
}
# print(my_dict)

# update value

# my_dict["age"] = "40"
# print(my_dict)

# update full item with name and values
my_dict.update({"name":"Sithira"})
print(my_dict)

# add new item 
my_dict["color"] = "Blue"
print(my_dict)

# delete item
my_dict.pop("is_student")
print(my_dict)

# delete last item
my_dict.popitem()
print(my_dict)

# to get all keys of a dictionary
print(my_dict.keys())

# destroy dictionary(delete dictionary)
# del my_dict
# print(my_dict)

# clear items in dictionary
my_dict.clear()
print(my_dict)