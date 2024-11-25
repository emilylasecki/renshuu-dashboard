# frame for GUI elements - load in physical things.
# text elements go in seperate method so reload only changes text - not the Gui

import tkinter as tk
from PIL import ImageTk, Image
from controller import *
from pathlib import Path

def reload(event=None):
    count = reloadContent()
    i=0
    for element in count:
        print(count[i])
        i=i+1
        return count
    #canvas4.pack_forget()

def reloadElements(event):
    frame2.destroy()  # destroy works but pack doesn't
    reload()
    createNewFrame()
    # reload with new image - don't think image is actually updating

def settingsClick(event=None):

    path= 'GUI_assets\Apikey.py'
    
    def updateAPIkey():
        input = inputtxt.get("1.0", "end-1c")
        print(input)
        print("test")
        # save input to new file
        if not os.path.exists(path):
            with open (path, 'w') as file:
                file.write("api_key"+ "= \"" + input + "\"")
        else:
            f = open(path, 'w')
            f.write("api_key" +" = \"" + input + "\"")

    # open new frame with settings GUI and info
    print("settings clicked")
    newWindow = tk.Tk()
    newWindow.title("Settings")
    newWindow.configure(background="#1c5669", borderwidth=19) # renshuu color
    newWindow.minsize(300,200)
    newWindow.maxsize(300,200)
    newWindow.geometry("500x500+1000+300")
    inputtxt = tk.Text(newWindow, height=5, width=20)
    inputtxt.pack()
    UpdateButton = tk.Button(newWindow, text="Update",  command=updateAPIkey)
    UpdateButton.pack()

def toggleView(event):
    print("toggle view clicked")

def createNewFrame(): # only reload counts - graph doesn't change fast enough to be relavent ** FIXME **
    frame5 =tk.Frame(window, bg="yellow", borderwidth=5, highlightthickness=0, width=480, height=400)
    frame5.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

    imagetest2 = (Image.open("GUI_assets\my_plot.png"))
    img3 = imagetest2.resize((480,400), Image.Resampling.LANCZOS)
   # image_label2 = tk.Label(frame5, image =imagetest2, borderwidth=0, highlightthickness=0) # FIXME line 61 and 62
   # image_label2.pack()

#create the window
count =reload()
window = tk.Tk()
window.title("Renshuu GUI")
window.configure(background="#1c5669", borderwidth=19) # renshuu color
window.minsize(600,620)
window.maxsize(600,620)
window.geometry("500x500+930+170")

frame =tk.Frame(window, bg="#1c5669", borderwidth=0, highlightthickness=0)
frame.grid()

canvas = tk.Canvas(frame, bg="#1c5669", width=100, height=100, borderwidth=0, highlightthickness=0)
canvas.grid(row=0, column=0)


character = tk.PhotoImage(file="GUI_assets\myKao.png")
imagetest = (Image.open("GUI_assets\myKao.png"))
img = imagetest.resize((100,100), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
canvas.create_image(50,50,image=img)  # potential change, image is squashed. Acceptable the way it is but could look better

#title
l = tk.Label(window, bg="#1c5669", text = "renshuu dashboard \n 毎日がんばってね!", width=15, height=0, font="UD_Digi_Kyokasho", fg="white", anchor="nw")
l.config(font=("UD_Digi_Kyokasho", 20, "bold")) 
l.grid(row=0,column=1)

# settings button
frame =tk.Frame(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=50, height =50)
frame.place(relx=0.9, rely=0.0)

canvas2 = tk.Canvas(frame, bg="#1c5669", borderwidth=0, highlightthickness=0, width=50, height=50)

img2 = tk.PhotoImage(file="GUI_assets\settings.png")
imagetest2 = (Image.open("GUI_assets\settings.png"))
img2 = imagetest2.resize((30,30), Image.Resampling.LANCZOS)
img2 = ImageTk.PhotoImage(img2)
canvas2.create_image(30,30, image=img2)
canvas2.grid()
canvas2.bind('<Button-1>', settingsClick) #activate settingsClick when clicked
canvas2.config(cursor="hand2") # make different cursor on hover

    # frame for content

frame4 =tk.Frame(window, bg="#201c1c", borderwidth=5, highlightthickness=0, width=480, height=400)
frame4.place(relx=0.5, rely=0.56, anchor=tk.CENTER)


frame2 =tk.Frame(window, bg="#201c1c", borderwidth=5, highlightthickness=0, width=480, height=400)
frame2.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

# FIXME create toggle view here
"""   # create condition for this to show later: displays graph on frame
imagetest2 = (Image.open("GUI_assets\my_plot.png"))
img3 = imagetest2.resize((480,400), Image.Resampling.LANCZOS) 
img3 = ImageTk.PhotoImage(img3)
image_label2 = tk.Label(frame2, image =img3, borderwidth=0, highlightthickness=0)
image_label2.pack()"""

#l = tk.Label(window, bg="#1c5669", text = "renshuu dashboard \n 毎日がんばってね!", width=15, height=0, font="UD_Digi_Kyokasho", fg="white", anchor="nw")
#l.config(font=("UD_Digi_Kyokasho", 20, "bold")) 
#l.grid(row=0,column=1)

#for reference
# count = [new_vocab, review_vocab, a, studied_vocab, new_kanji, review_kanji, b, studied_kanji, new_sentences, review_sentences, d, studied_sentences, new_grammar, review_grammar, d, studied_grammar]
i=0
while i<16:
    count[i] = str(count[i])
    i=i+1

text = tk.Label(frame2, text= "Today's Goals ", bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 20)) 
text.place(relx=0.05, rely=0.05)

text = tk.Label(frame2, text= "New Vocab: " + count[0], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.05, rely=0.2)

text = tk.Label(frame2, text= "Review Vocab: " + count[1], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.05, rely=0.3)

text = tk.Label(frame2, text= "New Kanji: " + count[4], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.05, rely=0.4)

text = tk.Label(frame2, text= "Review Kanji: " + count[5], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.05, rely=0.5)

text = tk.Label(frame2, text= "New Sentences: " + count[8], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.05, rely=0.6)

text = tk.Label(frame2, text= "Review Sentences: " + count[9], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.05, rely=0.7)

text = tk.Label(frame2, text= "New Grammar: " + count[12], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.05, rely=0.8)

text = tk.Label(frame2, text= "Review Grammar: " + count[13], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.05, rely=0.9)

text = tk.Label(frame2, text= "Today Done ", bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 20)) 
text.place(relx=0.6, rely=0.05)

text = tk.Label(frame2, text= "Studied Vocab: " + count[3], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.6, rely=0.2)

text = tk.Label(frame2, text= "Studied Kanji: " + count[7], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.6, rely=0.3)

text = tk.Label(frame2, text= "Studied Sentences: " + count[11], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.6, rely=0.4)

text = tk.Label(frame2, text= "Studied Grammar: " + count[15], bg="#201c1c", fg="white")
text.config(font=("UD_Digi_Kyokasho", 14)) 
text.place(relx=0.6, rely=0.5)


    # button on bottom of frame to change view
canvas3 = tk.Canvas(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=300, height=50)
canvas3.place(relx=0.6, rely=0.92)
text = canvas3.create_text(120, 30, text="View JLPT Progress Graph >>", fill="white", width="300", font=("UD_Digi_Kyokasho", 12, "bold"), anchor="center")
canvas3.tag_bind(text, "<Button-1>", toggleView)
canvas3.config(cursor="hand2")
    #View JLPT Progress Graph >>
    #View Daily Goals >>

    #reload button
canvas4 = tk.Canvas(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=60, height=60)
canvas4.place(relx=0.7, rely=0.03)
text2 = canvas4.create_text(30, 20, text="Reload Stats", fill="white", width="60", font=("UD_Digi_Kyokasho", 12, "bold"), anchor="center")
canvas4.tag_bind(text2, "<Button-1>", reloadElements)
canvas4.config(cursor="hand2")

window.mainloop()



