
file_read = open('act13.txt', 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()



file_write = open('act13.txt', 'w')
file_write.write("Hi! I am Penguin. I am 1 yr. old")
file_write.close()



file_append = open('act13.txt', 'a')
file_append.write("\nI love to code")
file_append.close()



file = open("act13.txt", "r")
Counter = 0

Content = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

file.close()

print("This is the number of lines in the file:")
print(Counter)


file1 = input("Enter the name of the destination file: ")
file2 = input("Enter the name of the source file to append: ")

with open(file2, 'r') as f2, open(file1, 'a') as f1:
    f1.write("\n" + f2.read())

print(f"Successfully appended contents of {file2} to {file1}")
