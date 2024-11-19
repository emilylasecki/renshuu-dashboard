from tkinter import *
from PIL import Image, ImageTk

def load_image(frame):
    # Open the image
    image = Image.open("kaochan.jpg") 

    # Resize the image if needed
    #image = image.resize((200, 200), Image.ANTIALIAS)

    # Convert the image to a Tkinter PhotoImage object
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label = Label(frame, image=photo)
    label.image = photo  # Keep reference to the image to avoid garbage collection
    label.pack()

root = Tk()
frame = Frame(root)
frame.pack()

# Load the image into the frame
load_image(frame)

root.mainloop()