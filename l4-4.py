num = int(input("Enter your number : "))

if num > 1 :
    for i in range(2, num):
        if num % i == 0:
            print(num, "is NOT a Prime number.")
            break
    else:
        print(num, "is a Prime number.")


else:
    print("Your number is not a prime number")