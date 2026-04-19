# Program to find longest consecutive 1's

num = int(input("Enter a number: "))

count = 0
max_count = 0

while num > 0:
    if num % 2 == 1:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

    num = num // 2

print("Longest consecutive 1's:", max_count)