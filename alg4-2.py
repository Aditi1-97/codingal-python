def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def sum_array(arr, n):
    if n == 0:
      return 0
    return arr[n-1] + sum_array(arr, n-1)

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print("Factorial of 5:", factorial(5))

print("Fibonacci of 6", fibonacci(6))

numbers = [5, 10, 15, 20, 25]
print("Sum of array:", sum_array(numbers, len(numbers)))

print("2 raised to power 5:", power(2,5))