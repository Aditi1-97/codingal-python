n = int(input("Enter a number: "))

if n == 0:
    print("No set bits")
else:
    posi = 1
    while n > 0:
        if n % 2 == 1:
            print("Position of rightmost set bit is:", posi)
            break
        n = n // 2
        posi += 1