def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n-1)

def calculate_time_complexity(n):
    if n <= 0:
        return 1
    return calculate_time_complexity(n-1)+1

def iterative_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# testing functions
number = 5

print("Recursive Sum Result:", recursive_sum(number))
print("Time Complexity (Recursive): 0(n)")
print("Space Complexity (Rescursive): 0(n)")

print("\nIterative Sum Result:", iterative_sum(number))
print("Time Complexity (Iterative): 0(n)")
print("Space Complexity (Iterative: 0(1))")