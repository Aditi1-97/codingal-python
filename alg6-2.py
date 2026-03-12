# function to find HCF
def find_hcf(a,b):
    hcf = 1

    # loop from i to the smallest number
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            hcf = 1

    return hcf

# function to find LCM
def find_lcm(a,b, hcf):
    lcm = (a*b) // hcf
    return lcm

# main program starts here
print("HCF and LCM Calculator")
print("---------------------") 

# take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# find HCF
hcf_result = find_hcf(num1, num2)

# find lcm
lcm_result = find_lcm(num1,num2, hcf_result)

# display results
print("\nResults: ")
print("HCF of", num1, "and", num2, "is:", hcf_result)
print("LCM of", num1, "and", num2, "is", lcm_result)