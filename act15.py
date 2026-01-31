
with open('codingal.txt', 'r') as fp:
    data1 = fp.read()

with open('file1.txt', 'r') as fp:
    data2 = fp.read()

data1 += "\n" + data2

print("Merging two files...")
with open('MergedFile.txt', 'w') as fp:
    fp.write(data1)


inputFile = open('demofile.txt', 'r')
outputFile = open('codingalupdated.txt', 'w')

lines_seen_so_far = set()
print("Eliminating duplicate lines...")

for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)

inputFile.close()
outputFile.close()


import os
print("Checking if my_fi exists or not...")

if os.path.exists("my_fi.txt"):
    os.remove("my_fi.txt")
    print("File deleted successfully.")
else:
    print("The file does not exist.")


with open('codingal.txt', 'w') as file:
    file.write("Hi! I am Penguin and I am 1 yr old")



with open('codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are...")
    for line in data:
        words = line.split()
        print(words)
