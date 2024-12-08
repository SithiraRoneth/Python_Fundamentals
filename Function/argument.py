# def add_numbers(a,b=5):
#     return a+b

# print(add_numbers(6,8)) # 14
# print(add_numbers(10)) # 15 because b = 5 

# ----------------------------------------------------------------------

# define a function name calculate_total_cost with the following parameters
# item_price : mandatory | not null
# quantity : mandatory
# discount : optional % applied to the total price
# deafult = should be 0
# tax : optional a % applied to after discount price

def calculate_total_cost(item_price,quantity,discount=0,tax=0):
    total = 0
    total = item_price * quantity
    new_total = total * discount/100
    full_total = total - new_total
    after_tax = full_total + tax

    return after_tax

print(calculate_total_cost(200,3,10,10))


