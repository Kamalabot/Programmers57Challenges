#Lets make something complicated with dicts
import datetime as dt

"""Program takes in a list of employee records in dictionary format 
and returns a list of employee records with the following fields:
"full name", "Job Title", "Seperation Date" """

employee_records = [{'First Name': 'John', 'Last Name': 'Johnson', 'Seperation date': '2016-12-31', 'Job Title': 'Manager'},
                    {'First Name': 'Tou', 'Last Name': 'Xiong', 'Seperation date': '2016-10-05', 'Job Title': 'Software Engineer'},
                    {'First Name': 'Michaela', 'Last Name': 'Michaelson', 'Seperation date': '2015-12-19', 'Job Title': 'District Manager'},
                    {'First Name': 'Jake', 'Last Name': 'Jacobson', 'Seperation date': '', 'Job Title': 'Programmer'},
                    {'First Name': 'Jacquelyn', 'Last Name': 'Jackson', 'Seperation date': '', 'Job Title': 'DBA'},
                    {'First Name': 'Sally', 'Last Name': 'Weber', 'Seperation date': '2015-12-18', 'Job Title': 'Web Developer'}]
for record in employee_records:
    record['Full Name'] = record['First Name'] + ' ' + record['Last Name']
    record['Separation Date'] = dt.datetime.strptime(record['Seperation date'], '%Y-%m-%d') if record['Seperation date'] else 'Still with us'

employee_records.sort(key=lambda x: x['Full Name'], reverse=False)

print("Name         |Job Title          |Separation Date                ")  
print("-----------------------------------------------------------------")

use_key = ['Full Name', 'Job Title', 'Separation Date']

for record in employee_records:
    [print(record[key],end="        ") for key in use_key]
    print('\n')

""" We extend the program to include filtering by first name and
last name"""

search = input("Enter the search string: ")

print("Results: ")


print("Name         |Job Title          |Separation Date                ")  
print("-----------------------------------------------------------------")

for record in employee_records:
    if search.lower() in record['Last Name'].lower() or search.lower() in record['First Name'].lower():
        #print(search)
        #print(record)
        print(record['Full Name'], end="        ")
        print(record['Job Title'], end="        ")
        print(record['Separation Date'])

