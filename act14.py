
with open("codingal.txt", "w") as file:
    file.write("Hello Students!\n")
    file.write("Welcome to Python file handling.\n")
    file.write("This file is used to demonstrate reading methods.\n")


print("Using read()")
with open("codingal.txt", "r") as file:
    content = file.read()
    print(content)


print("Using read(20)")
with open("codingal.txt", "r") as file:
    content = file.read(20)
    print(content)


print(" Using readline()")
with open("codingal.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)


print("Using readlines()")
with open("codingal.txt", "r") as file:
    lines = file.readlines()
    print(lines)


print("Using for loop")
with open("codingal.txt", "r") as file:
    for line in file:
        print(line)
