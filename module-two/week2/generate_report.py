#!/usr/bin/env python3

import csv
def read_employees(csv_file):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_employees('/home/student-01-624eccec5e47/data/employees.csv')

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictonary = process_data(employee_list)
print(dictonary)

def write_report(dictonary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictonary):
            f.write(str(k)+':'+str(dictonary[k])+'\n')
        f.close

write_report(dictonary, '/home/student-01-624eccec5e47/data/report.txt')