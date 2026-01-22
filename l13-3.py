# Get file names from user
file1 = input("Enter the name of the destination file: ")
file2 = input("Enter the name of the source file to append: ")

with open(file2, 'r') as f2, open(file1, 'a') as f1:
    f1.write("\n" + f2.read())

print(f"Successfully appended contents of {file2} to {file1}")    