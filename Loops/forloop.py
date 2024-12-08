fruits = ["apple","watermalon","banana"]

for fruit in fruits:
    print(fruit)

my_list = [2,5,8]
output_list = []

# for x in my_list:
#     output_list.append(x*x)
# print(output_list)

print([x**2 for x in my_list])

# square of 1 to 10 and print only even
print([x**2 for x in range(1,11) if x%2==0])