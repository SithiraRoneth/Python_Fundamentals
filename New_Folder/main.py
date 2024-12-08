# 1 st way

# import my_calculator.addition
# import my_calculator.substraction

# result_1 = my_calculator.addition.add(10,10)
# result_2 = my_calculator.substraction.sub(90,10)
# print("Add :",result_1)
# print("Sub :",result_2)


# 2 nd way

# from my_calculator import addition
# from my_calculator import substraction

# result_1 = addition.add(90,10)
# result_2 = substraction.sub(90,10)
# print(result_1)
# print(result_2)

# 3 rd way

# from my_calculator.addition import add
# from my_calculator.substraction import sub

# result_1 = add(90,10)
# result_2 = sub(80,10)
# print(result_1)
# print(result_2)

# 4 th way

from my_calculator import add,sub

result_1 = add(90,10)
result_2 = sub(80,10)
print(result_1)
print(result_2)