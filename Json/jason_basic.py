import json

# json_file_path = "Json\example_1.json"

# # Reading Json Data

# with open(json_file_path,"r") as json_file:
#     data = json.load(json_file)

#     print(data,type(data))

# # convert dictionary to json

# data = {
#     "name":"John Nash",
#     "age":30,
#     "city":"New York"
# }

json_file_path = "Json/test.json"

# with open(json_file_path,"w") as json_file :
#     json_data = json.dumps(data,indent=4) 
#     json_file.write(json_data)
# print(f"Json data has been written to {json_file_path}")

# You are given a json file name "students.json" wich contains information about student and their grades 
# 1. read the json file
# 2. display the name of all students who scored above 75
# 3. add the new student record to the file 
# 4. save the updated data back to the json file

# [
#     {"name":"Alice","grade":85},
#     {"name":"Bob","grade":72},
#     {"name":"Charlie","grade":90}
# ]

with open(json_file_path,'r') as json_file:
    student = json.load(json_file)
    for x in student:
        if (x["grade"]>75):
            print(x["name"])

    new_data = {
        "name":"Sithira",
        "grade":98
    }
    student.append(new_data)

with open(json_file_path,'w') as json_file:
    new_one = json.dumps(student,indent=4)
    json_file.write(new_one)
    print(json_file)

