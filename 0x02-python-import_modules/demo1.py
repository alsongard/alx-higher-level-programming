#!/usr/bin/python3
import sys
# iterate through the args
if len(sys.argv) > 1:
    file_name = sys.argv[1] # argv is list
    # to read the contents
    try:
        with open(file_name, "r") as file:
            contents = file.read()
            print(f"The file contents are {contents}")
    except:
        print(f"File name {file_name} not found")
else:
    print("Next time be sure to pass a file as argument")
