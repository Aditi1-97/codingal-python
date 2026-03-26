# program to check if the user entered nunber is odd or even using only bitwise operator
# returns true if n is even, else odd
def isEvenOdd(n):
    # XOR with 1 equals n+1
    if (n ^ 1 == n+1):
        return True;
    else:
        return False;

number = int(input("Enter your number : "))

if isEvenOdd(number):
    print(number, "is Even")
else:
    print(number, "is Odd")    