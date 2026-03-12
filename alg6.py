number = int(input("Enter your number: "))

# store the original number for comparison later
original_number = number
reversed_number = 0

# reverse the number
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

# check if the original number and the reversed number are the same
if original_number == reversed_number:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")        