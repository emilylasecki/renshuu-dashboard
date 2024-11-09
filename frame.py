# frame for GUI elements
import tkinter as tk
from PIL import ImageTk, Image

#create the window
window = tk.Tk()
window.title("Renshuu GUI")
window.configure(background="#1c5669", borderwidth=5) # renshuu color
window.minsize(500,500)
window.maxsize(500,500)
window.geometry("500x500+1000+300")

frame =tk.Frame(window, bg="#1c5669", borderwidth=0, highlightthickness=0)
frame.grid()

canvas = tk.Canvas(frame, bg="#1c5669", width=100, height=100, borderwidth=0, highlightthickness=0)
canvas.grid(row=0, column=0)


character = tk.PhotoImage(file="myKao.png")
imagetest = (Image.open("myKao.png"))
img = imagetest.resize((100,100), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
canvas.create_image(50,50,image=img)  # need to either make all images square and a certain dimension or get this to scale based on the image



"""
#insert image
path = "myKao.png"
#path ="https://www.renshuu.org/img/adventure/f/nryjgbz_100_20240408.png" # use path of user's kao-chan on GUI?
imagetest = (Image.open(path))
img = imagetest.resize((70,70), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
panel = tk.Label(window, image = img, bd=0)
panel.image = img
panel.grid(row=0, column=0) """

#title
l = tk.Label(window, bg="#1c5669", text = "renshuu dashboard \n 毎日がんばってね!", width=15, height=0, font="UD_Digi_Kyokasho", fg="white", anchor="nw")
l.config(font=("UD_Digi_Kyokasho", 20, "bold")) # to bold or not to bold?
l.grid(row=0,column=1)

#headings
l = tk.Label(window, text = "Today's goals:", width=15, height=2, font="UD_Digi_Kyokasho", bg="grey", fg="black", anchor="w")
l.config(font=("UD_Digi_Kyokasho", 12, "bold")) 
l.grid(row=1, column=1)
l = tk.Label(window, text = "Studied Today:", width=15, height=2, font="UD_Digi_Kyokasho", bg="grey", fg="black", anchor="w")
l.config(font=("UD_Digi_Kyokasho", 12, "bold")) 
l.grid(row=1, column=2)

l = tk.Label(window, text = " ", width=6, height=2, font="UD_Digi_Kyokasho", bg="grey", fg="black", anchor="nw")
l.config(font=("UD_Digi_Kyokasho", 12, "bold")) 
l.grid(row=1, column=0)

l = tk.Label(window, text = "Vocab:", width=15, height=2, font="UD_Digi_Kyokasho", bg="grey", fg="black", anchor="nw")
l.config(font=("UD_Digi_Kyokasho", 12, "bold")) 
l.grid(row=2, column=1)

l = tk.Label(window, text = "Vocab:", width=15, height=2, font="UD_Digi_Kyokasho", bg="grey", fg="black", anchor="nw")
l.config(font=("UD_Digi_Kyokasho", 12, "bold")) 
l.grid(row=2, column=2) 
window.mainloop()