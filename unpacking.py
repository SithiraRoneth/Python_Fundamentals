# my_list = [10,12,5]
# x,y,z = my_list
# print(x,y,z)

# my_tuple = ("car","bike",10) 
# p,q,r = my_tuple
# print(p,q,r)

person = {
    "name":"sithira",
    "age":21,
    "gender":"male"
}

for key,value in person.items():
    print(key,":",value)

# get only key 
for key in person.keys():
    print(key)

# get values 
for value in person.values():
    print(value)