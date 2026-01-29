# check if a file exists
import os
print("Checking if my_file exists or not...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

# create a new if it doesn't
        