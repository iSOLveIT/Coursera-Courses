import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))



def contents_of_file2(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file
    rows = csv.reader(file)
    next(rows)
    # Process each row
    for row in rows:
      name, color, type_ = row
      # Format the return string for data rows only

      return_string += "a {} {} is {}\n".format(color, name, type_)
  return return_string

#Call the function
print(contents_of_file2("flowers.csv"))


# Labs

"""
You successfully wrote a Python script that achieves two tasks. 
First, it reads a CSV file containing a list of the employees in 
the organization. 
Second, it generates a report of the number of people in each department in a plain text file.

Creating reports using Python is a very useful tool in IT support. 
You will likely complete similar tasks regularly throughout your career, 
so feel free to go through this lab more than once. Remember, practice makes perfect.
"""




def read_employees(csv_file_location):
	csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
	employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
	employee_list = []
	for data in employee_file:
		employee_list.append(data)
	return employee_list

def process_data(employee_list):
	department_list = []
	for employee_data in employee_list:
		department_list.append(employee_data['Department'])
	department_data = {}
	for department_name in set(department_list):
		department_data[department_name] = department_list.count(department_name)
	return department_data


def write_report(dictionary, report_file):
	with open(report_file, "w+") as f:
		for k in sorted(dictionary):
			f.write(str(k)+':'+str(dictionary[k])+'\n')
		f.close()



employee_list = read_employees('/home/student-02-c2583c304a50/data/employees.csv')
dictionary = process_data(employee_list)
write_report(dictionary, '/home/student-02-c2583c304a50/test_report.txt')

