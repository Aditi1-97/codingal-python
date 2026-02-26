def recursive_sum(n):
    if n <= 0:
        return 0
    
    return n + recursive_sum(n-1)

# function to calculate time complexity (conceptual demonstration)
def calculate_time_complexity(n):
    if n <= 0:
        return 1
    
    return calculate_time_complexity(n-1)+1

number = 5
print("Recursive sum:", recursive_sum(number))
print("Time Complexity Value (conceptual):", calculate_time_complexity(number))
