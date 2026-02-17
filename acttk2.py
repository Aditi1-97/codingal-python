import random
from tkinter import *

# Create main window
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="lightblue")

choices = ["Rock 🪨", "Paper 📄", "Scissors ✂️"]

# Function to play game
def play(user_choice):
    computer_choice = random.choice(choices)

    computer_label.config(text="Computer chose: " + computer_choice)

    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win! 🎉"
    else:
        result = "You Lose! 😏"

    result_label.config(text=result)


title = Label(root, text="Rock Paper Scissors", 
              font=("Arial", 18, "bold"), bg="lightblue")
title.pack(pady=20)


rock_btn = Button(root, text="Rock", width=12, 
                  command=lambda: play("Rock"))
rock_btn.pack(pady=5)

paper_btn = Button(root, text="Paper", width=12, 
                   command=lambda: play("Paper"))
paper_btn.pack(pady=5)

scissors_btn = Button(root, text="Scissors", width=12, 
                      command=lambda: play("Scissors"))
scissors_btn.pack(pady=5)


computer_label = Label(root, text="", font=("Arial", 12), bg="lightblue")
computer_label.pack(pady=15)


result_label = Label(root, text="", font=("Arial", 14, "bold"), bg="lightblue")
result_label.pack()


root.mainloop()
