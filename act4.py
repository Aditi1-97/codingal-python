# to ckeck if the user's number is an Armstrong number or not
num = int(input("Enter your number : "))

tem = num # here tem is a variable..
sum = 0

while tem > 0:
    digit = tem % 10
    sum = sum+(digit*digit*digit)
    tem = tem // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
