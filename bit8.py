def findMissing(arr, n):

    xor_all = 0
    for i in range(1, n+1):
        xor_all = xor_all ^ i

    xor_arr = 0
    for num in arr:
        xor_arr = xor_arr ^ num

    return xor_all ^ xor_arr

arr = []
n = int(input("Enter value of n (total numbers): "))

print("Enter", n-1, "numbers:")
for i in range(n-1):
    num = int(input("Enter number: "))
    arr.append(num)

print("\nMissing number is: ", findMissing(arr,n))    