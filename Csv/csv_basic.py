import csv

# with open("Csv\customers-100.csv",'r',newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # print(csv_reader,type(csv_reader))
#     for row in csv_reader:
#         print(row,type(row))

# how to write a csv

# csv_file_path = 'Csv\my_file_csv.csv'

# filed_name = ["Name","Age","City"]

# data = [{"Name":"sithira","Age":21,"City":"Thalahena"},{"Name":"Piumini","Age":21,"City":"Panadura"},{"Name":"Minura","Age":21,"City":"Moratuwa"}]

# with open("Csv\my_file_csv.csv",'w',newline='') as file:
#     csv_writer = csv.DictWriter(file,fieldnames=filed_name)
#     csv_writer.writeheader()
#     for row in data:
#         csv_writer.writerow(row)
#     print(f"CSV data has been written to {csv_file_path}")

# with open("Csv\my_file_csv.csv",'r') as file:
#     rows = csv.DictReader(file)
#     for row in rows:
#         print(row,type(row))


# You are task with creating with a python program to manage a company's employee record stored in csv files.the program should read 
# the employee details from a csv file, filter the record based on a condition and write the filter records to a new csv file.abs
# input files : employee.csv
# contain the following feilds EmployeeID,Name,Department,Salary
# 1 john it 50000
# 2 jane hr 55000

# ouput files : high_salary_employee.csv
# you will create this file it should contain records whose salary's are about 57,000.The field sholud remain the same

# task 1 - read the input file use csv.reader() to read employee.csv and display the all the records on the console
# task 2 - filter the record identify employee's with a salary > 57000
# task 3 - right the filter records use csv.DictWriter() to write the filter records to a new file name 'high_salary_employee.csv'  

employee_csv_path = "Csv\employee.csv"

with open('Csv\employee.csv','r',newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

filtered_salary = []

with open('Csv\employee.csv','r',newline='') as file:
    data = csv.DictReader(file)
    for row in data:
        if int(row["Salary"]) >57000:
            filtered_salary.append(row)

with open('Csv\high_salary_employee.csv','w',newline='') as file:
    field_name = ["EmployeeID","Name","Department","Salary"]
    writer = csv.DictWriter(file,fieldnames=field_name)
    writer.writeheader()
    writer.writerows(filtered_salary)
