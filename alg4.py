def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        print(f"Step {steps}: Checking index {mid}, value {arr[mid]}")

        if arr[mid] == target:
            print("Found the number!")
            print("Total steps:", steps)
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1

    print("Number not found")
    return -1
            
# try it
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
binary_search(numbers, 19)            