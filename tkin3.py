from tkinter import *
from tkinter import messagebox

# setup tkinter window
root = Tk()
root.geometry("200x200")

# function for displaying warning msg
#this will be called once the button is clicked
# messagebox.showwarning("Window name", "Text to be displayed")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus found.")

# Adding button widget to window
button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=80)

# entering main event loop
root.mainloop()