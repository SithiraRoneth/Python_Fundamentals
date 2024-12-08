def calculate_numbers(a,b):
    print(a+b)

calculate_numbers(10,20)

PI_VALUE = 3.14
def area_of_circle(r):
    return(PI_VALUE)*(r**2)

print(area_of_circle(20))


my_list = [4,8,12,5,9,7]

def calculate_mean(new_list):
    total = 0
    for x in new_list:
        total+=x
    avg = (total/len(new_list)+1)-1
    return avg

print(calculate_mean(my_list))

print(my_list[1:5])
# print(my_list[1:5:2])
# print(my_list[::2])

# def calculate_total_cost(item_price,quantity,discount=0,tax=0):
#     total = 0
#     price = item_price*quantity
#     discounted_price = price*discount/100
#     total = price - discounted_price

#     after_tax = total*tax/100
#     new_total = total+after_tax

#     print(new_total)

# calculate_total_cost(100,3,10,5)