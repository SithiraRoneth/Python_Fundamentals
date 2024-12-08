
# add new element custom index 

# my_list.insert(3,"rabbit")
# print(my_list)

# add another new element after the last element

#my_list.append("car")
#print(my_list)

# add another list for this list

# new_list = ["plane",90,40.5,False]
# my_list.extend(new_list)
# print(my_list)
# print(len(my_list))


# remove value from list

# my_list.pop(2)
# print(my_list)
# print(len(my_list))
# del my_list[3]
# print(my_list)

# clear all elements in this list

# my_list.clear()
# print(my_list)
# print(len(my_list))

# sort array(accesnding) 

# my_list = ["dog","apple","parrot","banana"]
# my_list.sort(key=str.lower)
# print(my_list)

# sort array(reverse)
# my_list.sort(reverse=True)
# print(my_list)

# my_list.reverse()
# print(my_list)

# my_list_1 = [-10,-18,12,5,7,12,-3]
# my_list_2 = [8,4,-3,9,2,11]

# my_list_1.extend(my_list_2)
# my_list_1.sort()
# print(my_list_1)

# mid = int(len(my_list_1)/2)
# print("Midian of this array list ",mid ,":",my_list_1[mid])

# q1 = int((len(my_list_1)+1)/4)
# print("25% :",q1,":",my_list_1[q1])

# q3 = int((len(my_list_1)+1)/4*3)
# print("75% :",q3, ":",my_list_1[q3])

my_list3 = [10,50,"Cat",True]
my_list4 = my_list3.copy()
my_list3[0]=80
print(my_list4)
print(my_list3)