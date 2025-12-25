def fact(n):
    if n == 0 :
        return 1
    else :
        return n * fact(n-1)
    
num = int(input("Enter your number to check the factorial:"))    

print("The factorial result is: ", fact(num))