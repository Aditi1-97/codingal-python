from tkinter import *
from PIL import Image, ImageTk

# Create main window
root = Tk()
root.title("Image")
root.geometry("400x400")

# Open the image
upload = Image.open("img1.jpg")

# (Optional) Resize image if it's too big
upload = upload.resize((300, 250))

# Convert image to Tkinter format
image = ImageTk.PhotoImage(upload)

# Create label to display image
label = Label(root, image=image)
label.image = image   # Keep reference (VERY IMPORTANT)
label.place(x=50, y=50)

# Text label
label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.place(x=40, y=330)

# Run the window
root.mainloop()
