# a = 10
# if a<0:
#     print("This is a negative number")
# elif a>0:
#     print("This is a positive number")
# else:
#     print("This is zero")


# x = (int)(input("Enter Your marks :"))
# if(85<=x<=100):
#     print("A")
# elif(75<=x<85):
#     print("B")
# elif(65<=x<75):
#     print("C")
# elif(55<=x<65):
#     print("D")
# else:
#     print("F")

a = 25
b = 50
c = 50

if a>b and a>c:
    print("A")
elif b>a and b>c:
    print("B")
elif c>a and c>b:
    print("C")
elif a==b or a==c or b==c :
    print("Two values are same")