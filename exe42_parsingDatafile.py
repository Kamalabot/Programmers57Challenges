#Parsing a datafile

import csv

"""Program takes a comma separated data file 
and returns a ordered data"""


input_file = input("Enter the input filename:\n")

file_data = []

with open(input_file) as f:
    csv_file = csv.reader(f)
    data = list(csv_file)
    for data_row in data:
        file_data.append({'Last' : data_row[0], 'First' : data_row[1], 
        'Salary' : data_row[2]})

print("Last     First        Salary")
print("-----------------------------")
#print(file_data)
[print(f"{record['Last']}   {record['First']}   {record['Salary']}") for record in file_data]