import math as m

def calculate_sphere_volume(radius):
    volume = 0
    if(radius>0):
        volume = (4 / 3) * m.pi * (radius ** 3)
        print(volume)
    else:
        print("Give a Positive number")

# calculate_sphere_volume(5)

def sum_of_squares(n):
    if(n>0):
        total = 0
        for x in range(1,n+1):
            total +=x**2

        return print(total)
    else:
        print("give a positive number")
    
# sum_of_squares(5)

def sum_of_digit(n):
    if n == 0:
        return 0
    if n > 0 :
        return (n % 10) + sum_of_digit(n // 10)
    else:
        return print("error")

    
# print(sum_of_digit(9876))

def calculate(operation, **kwargs):
    if operation not in ["sum", "product"]:
        return {"error": "Invalid operation. Use 'sum' or 'product'."}
    
    keys = list(kwargs.keys())
    values = list(kwargs.values())

    if operation == "sum":
        result = sum(values)
    elif operation == "product":
        result = 1
        for value in values:
            result *= value

    return {"keys": keys, "result": result}

# Example usage
# print(calculate(operation="sum", a=5, b=10, c=15))  # {"keys": ["a", "b", "c"], "result": 30}
# print(calculate(operation="product", x=3, y=4))     # {"keys": ["x", "y"], "result": 12}
