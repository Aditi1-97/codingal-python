height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in Kg: "))

BMI = weight/(height/100)**2

print(f"Your BMI is {BMI}")

if BMI < 18.9 :
    print("You are under weight")
elif BMI < 24.9 :
    print("You are fit")
elif BMI < 29.9 :
    print("You are over weight") 
elif BMI < 34.9 :
    print("You are obese")
elif BMI < 39.9 :
    print("You are serious obese")           
