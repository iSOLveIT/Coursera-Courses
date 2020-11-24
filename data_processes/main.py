#Imports
import os
import sys
import subprocess


"""Reading Data Interactively"""
def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("24 hours is equivalent to", to_seconds(24, 0, 0), "seconds.", end=" ")

"""Standard Streams"""
# I/O Streams = (STDOUT, STDIN, STDERR)

"""Environment Variables"""
os.environ['DEVELOPER'] = "RANDY"

"""Command-Line Arguments and Exit Status"""
# get command line args passed to a program
print(sys.argv)
# print(sys.exit(1))  # default is 0 which means successful

"""Running System Commands in Python"""
output = subprocess.run(["purple-task"])   # Use the run() method when you just want to know exit status
print(output.stdout) 

# Obtaining the output of a system command
result = subprocess.run(["host", "isolveit.herokuapp.com"], capture_output=True) # Obtain output by setting capture_output = True
print(result.stdout.decode().split('\n'), result.returncode)

"""Advanced Subprocess Management"""
