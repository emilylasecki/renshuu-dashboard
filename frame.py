# frame for GUI elements
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Renshuu GUI")
window.configure(background="#1c5669") # renshuu color
window.minsize(500,500)
window.maxsize(500,500)
window.geometry("500x500+1000+300")

path = "kaochan.jpg"
imagetest = (Image.open(path))
img = imagetest.resize((70,70), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
panel = tk.Label(window, image = img, bd=0)
panel.image = img
panel.grid(row =2)
#button = tk.Label(window, image = img)
#button.pack(pady=20)
window.mainloop()