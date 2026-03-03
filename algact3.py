import math

def myfunction(n):
    first_loop_count = n + 1

    j = 1
    second_loop_count = 0
    while j <= n + 1:
        second_loop_count += 1
        j = j * 2

    third_loop_count = 100

    total_operations = first_loop_count + second_loop_count + third_loop_count

    print("First loop runs:", first_loop_count, "times")
    print("Second loop runs:", second_loop_count, "times")
    print("Third loop runs:", third_loop_count, "times")
    print("Total operations:", total_operations)

    
    print("Time Complexity: O(n)")



myfunction(1000)