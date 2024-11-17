# frame for GUI elements - load in physical things.
# text elements go in seperate method so reload only changes text - not the Gui
#from main import data  # for bringing in specific vars later
import tkinter as tk
from PIL import ImageTk, Image
from controller import *

#create the window
def main():
    reload()
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
    canvas.create_image(50,50,image=img)  # potential change, image is squashed. Acceptable the way it is but could look better

#title
    l = tk.Label(window, bg="#1c5669", text = "renshuu dashboard \n 毎日がんばってね!", width=15, height=0, font="UD_Digi_Kyokasho", fg="white", anchor="nw")
    l.config(font=("UD_Digi_Kyokasho", 20, "bold")) # to bold or not to bold?
    l.grid(row=0,column=1)

# settings button
    frame =tk.Frame(window, bg="#1c5669", borderwidth=0, highlightthickness=0)
    frame.grid(row=0, column=3)

    canvas2 = tk.Canvas(frame, bg="orange", width=130, height=100, borderwidth=0, highlightthickness=0)
#canvas2.grid()

    img2 = tk.PhotoImage(file="settings.png")
    imagetest2 = (Image.open("settings.png"))
    img2 = imagetest2.resize((30,30), Image.Resampling.LANCZOS)
    img2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(30,30, image=img2)
    canvas2.grid()
    frame2 =tk.Frame(window, bg="#201c1c", borderwidth=5, highlightthickness=0, width=425, height=340)
    frame2.place(relx=0.5, rely=0.6, anchor=tk.CENTER) # kissing my dreams of rounded corners goodbye


    # create condition for this to show later: dispalys graph on frame
    imagetest2 = (Image.open("graph2.png"))
    img3 = imagetest2.resize((400,350), Image.Resampling.LANCZOS)
    img3 = ImageTk.PhotoImage(img3)
    image_label2 = tk.Label(frame2, image =img3)
    image_label2.pack()



    window.mainloop()

    # if view is jlpt progress
        # display that stuff

    # if view is word of the day  # do i want to keep word of the day?
        # display that stuff

    # if view is schedules
        # display that stuff

    # for each view either have to create a new file that this can read from, or pass it from controller

def reload():
    count = reloadContent()
    i=0
    for element in count:
        print(count[i])
        i=i+1



# add buttons for each view


# now alter here depending on what view is selected

# daily review, daily word, jlpt progress




if __name__ == "__main__":
    main()