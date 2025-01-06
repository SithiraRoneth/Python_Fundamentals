import math as math

# def make_pretty(func):
#     def inner():
#         print("I got decorator")
#         ordinary()
#     return inner

# def ordinary():
#     print("I am Ordinary")

# get_decorator = make_pretty(ordinary)
# get_decorator()


# @ Symbol with decorators

def make_pretty(func):
    def inner():
        print("I got decorator")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am Ordinary")

# ordinary()

# write a python program with a following requirment 
# 1. create a decorator check_positive that 
#   check if the input to a function is a positive number
#   if the input is not positive print the message line "input must be a postive number"
# 2. use this decorator on a function calculte_square_root
#   take one number as input
#   return the square root of the input number

def check_positive(func):
    # num = int(input("Enter the number :"))
    # if num>0 :
    #     func(num)
    # else:
    #     print("input must be a postive number")
    # return check_positive()
    def inner(num):
        if num>0 :
            func(num)
        else:
            print("input must be a postive number")
        return inner

@check_positive
def calculte_square_root(x):
    return math.sqrt(x)


calculte_square_root(10)
