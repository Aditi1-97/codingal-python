import tkinter as tk
import random


root = tk.Tk()
root.title("Rock Paper Scissor Game")
root.geometry("400x450")
root.config(bg="lightblue")


choices = ["Rock", "Paper", "Scissor"]


user_score = 0
computer_score = 0


def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    
    comp_label.config(text="Computer chose: " + computer_choice)
    
   
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    
    result_label.config(text=result)
    score_label.config(text=f"Your Score: {user_score}  |  Computer Score: {computer_score}")


def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Your Score: 0  |  Computer Score: 0")
    result_label.config(text="")
    comp_label.config(text="")


tk.Label(root, text="Rock Paper Scissor", 
         font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)


tk.Button(root, text="Rock", width=15, font=("Arial", 12),
          command=lambda: play("Rock")).pack(pady=5)

tk.Button(root, text="Paper", width=15, font=("Arial", 12),
          command=lambda: play("Paper")).pack(pady=5)

tk.Button(root, text="Scissor", width=15, font=("Arial", 12),
          command=lambda: play("Scissor")).pack(pady=5)


comp_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
comp_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="lightblue")
result_label.pack(pady=5)

score_label = tk.Label(root, text="Your Score: 0  |  Computer Score: 0",
                       font=("Arial", 12), bg="lightblue")
score_label.pack(pady=10)


tk.Button(root, text="Reset Game", width=15, bg="red", fg="white",
          command=reset_game).pack(pady=10)

root.mainloop()