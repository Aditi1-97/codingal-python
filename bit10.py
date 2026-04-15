def divide(dividend, divisor):
    if divisor == 0:
       return "Error: Division by zero is not allowed"
    negative = (dividend < 0) != (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0

    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    if negative:
        quotient = -quotient

    return quotient

print(divide(10, 2))
print(divide(15, 4))
print(divide(-20, 5))           