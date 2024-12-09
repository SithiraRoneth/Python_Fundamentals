my_list_1 = [1,2,3,4,5,6]
# print(my_list_1)
my_list_1.insert(3,"cat")
# print(my_list_1)
my_list_1.append(9)
# print(my_list_1)

my_list_2 = ["fish","parrot"]
my_list_1.extend(my_list_2)
# print(my_list_1)

my_list_1.pop(2)
# print(my_list_1)

# print(len(my_list_1))

my_list = ["dog","apple","parrot","banana"]
my_list.sort()
# print(my_list)

my_list.sort(reverse=True)
# print(my_list)

# print(my_list_1[-9])

# print("custom range",my_list_1[1:3])

my_list_1[2:3] = ["pigeon",10]
# print(my_list_1)

mid = int(len(my_list_1)/2)
# print(mid)

tuple_1 = ("cat",2,5)
tuple_2 = ("rat",9,0)
# print(tuple_1+tuple_2)

# x = int(input("enter velue :"))

# match x :
#     case _ if x<10:
#         print("lower than 10")
#     case _ if x>10:
#         print("greater than 10")
#     case _:
#         print("none")

# numbers = [4,3]

# match numbers:
#     case [x,y]:
#         print(x+y)
#     case [x,y,z]:
#         print(x+y+z)
#     case _:
#         print("the list doesn't contain 2 or 3 numbers")
    
range_1 = (9,2,3)
# print(type(range_1))

# loops 
# fruit = ["mango","apple","watermelon"]

# for x in fruit:
#     # print(x)

num = [1,2,3,4,5]
# for x in num:
#     if x<10:
#         print(x)
#     else:
#         print("none")

# print([x**2 for x in num] )

# my_list = [1,2,3,4,5]

# def calculate_mean(new_list):
#     total = 0
#     for x in new_list:
#         total+=x
#     avg = (total/len(new_list)+1)
#     return avg

# print(calculate_mean(my_list))

my_dict = {
    "name":"John",
    "age":30,
    "is_student":False,
    "grades":[85,90,76],
    "cordinates":[12,23,56,78]
}
# print(type(my_dict))
my_dict["age"] = "50"
# print(my_dict)

my_dict.update({"name":"kumara"})
# print(my_dict)

my_dict.pop("age")
# print(my_dict)

my_dict.popitem()
# print(my_dict)

# print(my_dict.keys())