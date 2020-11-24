with open("dummy.txt", "r+") as f:
    file_content = f.readlines()
    added = f.writelines("\n".join(file_content))

number_lines = sum([1 for i in file_content])

print(file_content)
print(f"Number of lines: {number_lines}")


import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as f:
    f.write(comments)
  
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))


import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    file.write("")

  # Return the list of files in the new directory
  return os.listdir(".")

print(new_directory("PythonPrograms", "script.py"))

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as file:
    file.write("")

  modify = os.path.getmtime(filename)
  timestamp = datetime.datetime.fromtimestamp(modify)
  # Convert the timestamp into a readable format, then into a string
  new = timestamp.strftime("%Y-%m-%d")
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{0}".format(new))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd