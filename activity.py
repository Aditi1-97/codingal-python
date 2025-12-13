# Swapping three numbers

print("Enter three numbers")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Before Swapping")
print("a =", a)
print("b =", b)
print("c =", c)

# swapping logic
a, b, c = b, c, a

print("After Swapping")
print("a =", a)
print("b =", b)
print("c =", c)
