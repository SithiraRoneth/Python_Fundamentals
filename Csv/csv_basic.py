import csv

with open("Csv\customers-100.csv",'r',newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader,type(csv_reader))