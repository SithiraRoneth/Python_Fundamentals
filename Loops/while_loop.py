m = 5
i = 0 

while i<m:
    print(i, end=" , ")
    i = i + 1
print("End")

# only print even number less than given number

# x = (int)(input("Eneter number :"))
# y = 2
# while y<x:
#     if y == 10:
#         break  # if y == 10 break the execute and end this program
#     else:
#         print(y)
#         y +=2
# print("end")


# total = 0

# while True:
#     num = (int)(input("Enter number :"))
#     if num == 0:
#         break
#     else:
#         total += num
# print(total)


my_list = [3,8,15,10,97,14]
x = 0

for odd in my_list:
    if odd%2==1:
        print(odd)
    else:
        continue
