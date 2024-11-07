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

#label = tk.Label(window, text="renshuu")
#label.grid()

#text = tk.Text(window)
#myFont = tk.Font(family="UD Digi Kyokasho", size=12)
#text.configure(font=myFont)

l = tk.Label(window, text = "renshuu", width=10, height=2, font="UD_Digi_Kyokasho")
l.grid()
#sample_text = tk.Text( window, height = 10) 
#sample_text.pack() 
#test = ("UD Digi Kyokasho", 20, "bold")
#test.grid()
#window.text = tk.text(window, text="test", fill="white", font='UD Digi Kyokasho')
#button = tk.Label(window, image = img)
#button.pack(pady=20)
#sample_text.configure(font = Font_tuple) 
#window.txt.insert(0, "test")
window.mainloop()