# response_code = 200

# match response_code:
#     case 200:
#         print("ok")
#     case 201:
#         print("created")
#     case 404:
#         print("not found")
#     case 500:
#         print("internal server error")
#     case _:
#         print("something else")

# ---------------------------------------------------------------------------------
# switch case

# x = (int)(input("enter value:"))
# match x:
#     case 0:
#         print("zero")
#     case -1:
#         print("negative")
#     case 1:
#         print("positive")
#     case _ if x>1:
#         print("positive number greater than one")
#     case _ if x<-1:
#         print("negative number less than negative one")
#     case _:
#         print("unmatch number")


# ---------------------------------------------------------------------------------
# matching by the length of an interable

numbers = [4,3,2]

match numbers:
    case [x,y]:
        print(x+y)
    case [x,y,z]:
        print(x+y+z)
    case _:
        print("the list doesn't contain 2 or 3 numbers")

x_list = [2,31]

match x_list:
    case []:
        print("empty")
    case [x]:
        print("one element")
    case [x,y]:
        print("two element")
    case _:
        print("this is something else")

