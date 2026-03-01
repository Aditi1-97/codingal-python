def multiply_one_iteration(n, m):
    return n * m

def multiply_n_iterations(n, m):
    result = 0
    for i in range(n):
        result += m
    return result



N = int(input("Enter value of N: "))
M = int(input("Enter value of M: "))


result1 = multiply_one_iteration(N, M)
result2 = multiply_n_iterations(N, M)

print("Result using 1 iteration:", result1)
print("Result using N iterations:", result2)