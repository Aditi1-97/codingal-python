number = 7   

print("Guess the number between 1 and 10")

guess = int(input("Enter your guess: "))

while guess != number:
    if guess < number:
        print("Too low")
    else:
        print("Too high")

    guess = int(input("Try again: "))

print("Correct! You guessed the number 🎉")
