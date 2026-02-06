import random 
import tkinter as tk

def generate_password():
    length = int(entry.get())
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&"
    password = ""

    for i in range(length):
        password += random.choice(characters)

    result_label.config(text="Password: " + password)


window = tk.Tk()
window.title("Password Generator 🔑")
window.geometry("300x200")


label = tk.Label(window, text="Enter Password Length 📏")
label.pack(pady=5)


entry = tk.Entry(window)
entry.pack(pady=5)

button = tk.Button(window, text="Generate Password", command=generate_password)
button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=5)

window.mainloop()
