# file_1 = open("FileHandeling\my_file.txt")
# # file_content = file_1.read()           # print all lines in text document
# # file_content = file_1.readline()     # print only one line
# file_content = file_1.readlines()

# # print(file_content)
# print(file_content,type(file_content))   #print list type

# file_1.close()  # close object


# 'with' statement for the handeling python

# with open("FileHandeling\my_file.txt","r") as file:
#     content = file.read()
#     print(content)

# write a text

# with open("FileHandeling\my_file_1.txt","w") as file:
#     # content = file.write("Hello world""\nThis is our python")
#     # contnt_list = ["Hello word\n","This is our python"]
#     content = file.writelines(["Hello word\n","This is our python"])
#     print(content)

# # append another line for exisiting doc
# with open("FileHandeling\my_file_1.txt","a") as file:
#     content = file.write("\nWe are global citizen")


#  implement a simple contact management system
# 1. create a program that stores and manage contacts in a file name 'contacts.txt' each contact entry should in to name,phone number,email
# 2. add a new contact(append)
# 3. view all contacts(read and display all the contacts on the file)
# 4. exit the progarm

def addNew():
    with open("FileHandeling\contacts.txt","a") as file:
            name = input("\nEnter Name :")
            contact = input("Enter Contact No :")
            email = input("Enter Email :")
            content = file.write("\n"+name+" "+contact+" "+email)

def viewAll():
    with open("FileHandeling\contacts.txt","r") as file:
            content = file.readlines()
            for contact in content:
                print(contact)

def exitProgram():
    ex = input("Are you sure you want to exit[y/n]")
    if ex == ('y'):
        exit()

print("[1] Add a new\t[2] View All\t[3] Exit")         
while True :
    user = int(input("\nEnter value :"))
    match user:
        case 1:
            addNew()
        case 2:
            viewAll()
        case 3:
            exitProgram()
    

