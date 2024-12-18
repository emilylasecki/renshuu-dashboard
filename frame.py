# frame for GUI elements - load in physical things.
# text elements go in seperate method so reload only changes text - not the Gui

import tkinter as tk
from tkinter import Text
from PIL import ImageTk, Image
from controller import *
from pathlib import Path
import webbrowser

GraphVisible2 = False # use boolean to control what view is loaded

def reload(event=None):
    try:
        count = reloadContent(0)
        i=0
        for element in count:
            i=i+1
            return count
    except:
        pass

def reloadElements(event):
    try:
        count = reloadContent(0)
        i=0
        while i<16:
            count[i] = str(count[i])
            i=i+1
        #   print(count[i])

        test1.set(newVocab + count[0]) # get new count
        test2.set(reviewVocab + count[1])
        test3.set(newKanji + count[4])
        test4.set(reviewKanji + count[5])
        test5.set(newSentences + count[8])
        test6.set(reviewSentences + count[9])
        test7.set(newGrammar + count[12])
        test8.set(reviewGrammar + count[13])
        test9.set(studiedVocab + count[3])
        test10.set(studiedKanji + count[7])
        test11.set(studiedSentences + count[11])
        test12.set(studiedGrammar + count[15])
        createNewFrame()
    except:
        pass
    # reload with new image - don't think image is actually updating

def loadSimpleFrame():
    window.mainloop()
    reload()
   # reloadElements(event=None)

def settingsClick(event=None):

    canvas2.unbind('<Button-1>')
    path= 'Apikey.py'

    def closesettings():
        newWindow.destroy()
        canvas2.bind('<Button-1>', settingsClick)
    
    def updateAPIkey():
        input = inputtxt.get("1.0", "end-1c")
        print(input)
       # print("test")
        # save input to new file
        if not os.path.exists(path):
            with open (path, 'w') as file:
                file.write("api_key"+ "= \"" + input + "\"")
        else:
            os.remove("Apikey.py")
            with open (path, 'w') as file:
                file.write("api_key"+ "= \"" + input + "\"")
        closesettings()
       # reloadElements(event=None)

    # open new frame with settings GUI and info 
    print("settings clicked")
    newWindow = tk.Tk()
    newWindow.title("Settings")
    newWindow.configure(background="#1c5669", borderwidth=19) # renshuu color
    newWindow.minsize(300,300)
    newWindow.maxsize(300,300)
    newWindow.geometry("500x500+1000+300")
    message = tk.Label(newWindow, text="Copy your Renshuu API key and paste it in the box below. Press update and then restart the program to review your Renshuu stats!", wraplength=260, bg="#1c5669", fg="white", anchor="center")
    message.config(font=("UD_Digi_Kyokasho",10, "bold"))
   # message.place(relx = 0.05, rely=0.05)
    inputtxt = tk.Text(newWindow, height=8, width=20)
    inputtxt.place(relx= 0.2, rely=0.35)
    UpdateButton = tk.Button(newWindow, text="Update",  command=updateAPIkey)
    UpdateButton.place(relx=0.42, rely=0.9)
    message.place(relx = 0.01, rely=0.01)
    newWindow.protocol("WM_DELETE_WINDOW", closesettings)
    newWindow.mainloop()
   # reloadContent(input)

def toggleView(event):
    global GraphVisible2
    if GraphVisible2 == True:
        GraphVisible2 = False
        createNewFrame()
    else:
        GraphVisible2 = True
        createNewFrame()

def createNewFrame(): 
    if GraphVisible2 == True:
        frame3.tkraise()
        canvas3.itemconfigure(text1, state='hidden')
        canvas3.itemconfigure(text34, state='normal')
    if GraphVisible2 == False:

        frame2.tkraise()
        canvas3.itemconfigure(text34, state='hidden')
        canvas3.itemconfigure(text1, state='normal')

def moreInfo(event=None): # create a GUI that gives info on how counts are calculated
    
    def closeFrame():
        moreInfoWindow.destroy()
        canvas7.bind("<Button-1>", moreInfo)

    def openGitHub():
        webbrowser.open_new("https://github.com/emilylasecki/RenshuuAPI")
        
    canvas7.unbind("<Button-1>")
    print("button clicked")
    moreInfoWindow = tk.Tk()
    moreInfoWindow.title("About renshuu dashboard")
    moreInfoWindow.configure(background="#201c1c", borderwidth=10)
    moreInfoWindow.minsize(400,550)
    moreInfoWindow.maxsize(400,550)
    text = Text(moreInfoWindow)
    text2 = Text(moreInfoWindow)
    text3 = tk.Label(moreInfoWindow, text="https://github.com/emilylasecki/RenshuuAPI")
    text.insert(tk.INSERT, 'How are counts calculated?\n\n')
    text.insert(tk.INSERT, "Because Renshuu API doesn't provide schedule types,\nthe category of each schedule is determined by \nkeywords in the title. Schedules with \"words\" or \n\"vocab\" are vocab, schedules with \"kanji\" are kanji, \nschedules with \"sentences\" are sentences, and \nschedules with none of these keywords are grammar. \nPlease confirm that your schedules follow this naming \nconvention to get accurate results. Renshuu \nAPI also doesn't have a built in way to track whether \nmultiple schedules contain duplicate words. Make \nsure to pause old schedules to midigate overcounting.")
    text2.insert(tk.INSERT, "\n\nWhy do I have to restart the whole program to update\nthe API key?\n\n")
    text2.insert(tk.INSERT, "Python caches the values of non-json files that cannot\nbe updated during run time. To combat this, restarting \nthe entire program clears the cache and allows these \nfiles to update. This is also the case for the MyKao \ncharacter that appears on the frame and the \nJLPT Progress Graph.")
    text2.insert(tk.INSERT, "\n\n\nTo read more about the development of this program \nvisit")
    text.place(relx=0.03, rely=0.04)
    text2.place(relx=0.03, rely=0.44)
    text3.place(relx=0.11, rely=0.865)
    text3.bind("<Button-1>", lambda e: openGitHub())
    text3.config(cursor="hand2")
    text.tag_add("vocab", "5.23", "6.17")
    text.tag_add("kanji", "6.18", "6.51")
    text.tag_add("sentences", "7.0", "7.40")
    text.tag_add("grammar", "7.41", "8.49")
    text.tag_add("highlight", "12.44", "13.52")
    text2.tag_add("anotherHighlight", "7.43", "9.15")
    text2.config(state=tk.DISABLED, font=("UD_Digi_Kyokasho", 10, "bold"), bg="#201c1c", borderwidth=0, fg="white")
    text.config(state=tk.DISABLED, font=("UD_Digi_Kyokasho", 10, "bold"), bg="#201c1c", borderwidth=0, fg="white")
    text3.config(font=("UD_Digi_Kyokasho", 10, "bold"), bg="#201c1c", borderwidth=0, fg="white")
    text.tag_config("vocab", foreground="#5e5cd0")
    text.tag_config("kanji", foreground="#de8117")
    text.tag_config("sentences", foreground="#d61145")
    text.tag_config("grammar", foreground="#7acc18")
    text.tag_config("highlight", foreground="yellow")
    text2.tag_config("anotherHighlight", foreground="yellow")

    okButton = tk.Button(moreInfoWindow, text="Close",  command=closeFrame)
    okButton.place(relx=0.44, rely=0.93)

    moreInfoWindow.protocol("WM_DELETE_WINDOW", closeFrame)

    moreInfoWindow.mainloop()

try:
    count =reload()
    window = tk.Tk()
    window.title("renshuu dashboard")
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
    #canvas2.place(relx=0.2, rely=0.9)
    canvas2.grid()
    canvas2.bind('<Button-1>', settingsClick) #activate settingsClick when clicked
    canvas2.config(cursor="hand2") # make different cursor on hover

        # frame for content

    frame3 =tk.Frame(window, bg="#201c1c", borderwidth=5, highlightthickness=0, width=480, height=400)
    frame3.place(relx=0.5, rely=0.56, anchor=tk.CENTER)


    frame2 =tk.Frame(window, bg="#201c1c", borderwidth=5, highlightthickness=0, width=480, height=400)
    frame2.place(relx=0.5, rely=0.56, anchor=tk.CENTER)



    imagetest2 = (Image.open("GUI_assets\my_plot.png"))
    img3 = imagetest2.resize((480,400), Image.Resampling.LANCZOS) 
    img3 = ImageTk.PhotoImage(img3)
    image_label2 = tk.Label(frame3, image =img3, borderwidth=0, highlightthickness=0)
    image_label2.pack()

    l = tk.Label(frame2, bg="#201c1c", text = "Invalid API Key. Configure API key in settings!", width=480, height=0, font="UD_Digi_Kyokasho", fg="white", anchor="nw")
    l.place(relx = 0.05, rely = 0.5)
    canvas6 = tk.Canvas(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=40, height=40)
    imgforFrame = (Image.open("GUI_assets\ButtonReload.png"))
    imgagain = imgforFrame.resize((40,40), Image.Resampling.LANCZOS)
    imgAgain = ImageTk.PhotoImage(imgagain)

    canvas6.create_image(40,40, image=imgAgain, anchor="se")
    canvas6.place(relx=0.75, rely=0.05)
    canvas6.bind("<Button-1>", reloadElements)
    canvas6.config(cursor="hand2")
   

    canvas7 = tk.Canvas(window,bg="#1c5669", borderwidth=0, highlightthickness=0, width=40, height=40)
    i = Image.open("GUI_assets\questionMarkButton.png")
    i2 = i.resize((40,40), Image.Resampling.LANCZOS)
    i3 = ImageTk.PhotoImage(i2)
    canvas7.create_image(40,40, image=i3, anchor="se")
    canvas7.place(relx=0.00, rely=0.93)
    canvas7.bind("<Button-1>", moreInfo)
    canvas7.config(cursor="hand2")

    i=0
    while i<16:
        count[i] = str(count[i])
        i=i+1

    l.destroy()


    text = tk.Label(frame2, text="Today's Goals:", bg="#201c1c", fg="white")
    text.config(font=("UD_Digi_Kyokasho", 20)) 
    text.place(relx=0.05, rely=0.02)


    test1 = tk.StringVar()
    newVocab = "New Vocab: "
    test1.set(newVocab + count[0])
    text2 = tk.Label(frame2, textvariable= test1, bg="#201c1c", fg="white")
    text2.config(font=("UD_Digi_Kyokasho", 14)) 
    text2.place(relx=0.05, rely=0.6)

    test2 = tk.StringVar()
    reviewVocab = "Review Vocab: "
    test2.set(reviewVocab + count[1])
    text3 = tk.Label(frame2, textvariable= test2, bg="#201c1c", fg="white")
    text3.config(font=("UD_Digi_Kyokasho", 14)) 
    text3.place(relx=0.05, rely=0.15 )

    test3 = tk.StringVar()
    newKanji = "New Kanji: "
    test3.set(newKanji + count[4])
    text4 = tk.Label(frame2, textvariable=test3, bg="#201c1c", fg="white")
    text4.config(font=("UD_Digi_Kyokasho", 14)) 
    text4.place(relx=0.05, rely=0.7)

    test4 = tk.StringVar()
    reviewKanji = "Review Kanji: "
    test4.set(reviewKanji + count[5])
    text5 = tk.Label(frame2, textvariable=test4, bg="#201c1c", fg="white")
    text5.config(font=("UD_Digi_Kyokasho", 14)) 
    text5.place(relx=0.05, rely=0.25)

    test5 = tk.StringVar()
    newSentences = "New Sentences: "
    test5.set(newSentences + count[8])
    text6 = tk.Label(frame2, textvariable=test5, bg="#201c1c", fg="white")
    text6.config(font=("UD_Digi_Kyokasho", 14)) 
    text6.place(relx=0.05, rely=0.8)

    test6= tk.StringVar()
    reviewSentences = "Review Sentences: "
    test6.set(reviewSentences + count[9])
    text7 = tk.Label(frame2, textvariable=test6, bg="#201c1c", fg="white")
    text7.config(font=("UD_Digi_Kyokasho", 14)) 
    text7.place(relx=0.05, rely=0.35)

    test7 = tk.StringVar()
    newGrammar = "New Grammar: "
    test7.set(newGrammar + count[12])
    text8 = tk.Label(frame2, textvariable=test7, bg="#201c1c", fg="white")
    text8.config(font=("UD_Digi_Kyokasho", 14)) 
    text8.place(relx=0.05, rely=0.9)

    test8 = tk.StringVar()
    reviewGrammar = "Review Grammar: "
    test8.set(reviewGrammar + count[13])
    text9 = tk.Label(frame2, textvariable=test8, bg="#201c1c", fg="white")
    text9.config(font=("UD_Digi_Kyokasho", 14)) 
    text9.place(relx=0.05, rely=0.45)

    text10 = tk.Label(frame2, text= "Today Done: ", bg="#201c1c", fg="white")
    text10.config(font=("UD_Digi_Kyokasho", 20)) 
    text10.place(relx=0.55, rely=0.02)

    test9 = tk.StringVar()
    studiedVocab = "Studied Vocab: "
    test9.set(studiedVocab + count[3])
    text11 = tk.Label(frame2, textvariable=test9, bg="#201c1c", fg="white")
    text11.config(font=("UD_Digi_Kyokasho", 14)) 
    text11.place(relx=0.55, rely=0.15)

    test10 = tk.StringVar()
    studiedKanji = "Studied Kanji: "
    test10.set(studiedKanji + count[7])
    text12 = tk.Label(frame2, textvariable=test10, bg="#201c1c", fg="white")
    text12.config(font=("UD_Digi_Kyokasho", 14)) 
    text12.place(relx=0.55, rely=0.25)

    test11 = tk.StringVar()
    studiedSentences = "Studied Sentences: "
    test11.set(studiedSentences + count[11])
    text13 = tk.Label(frame2, textvariable=test11, bg="#201c1c", fg="white")
    text13.config(font=("UD_Digi_Kyokasho", 14)) 
    text13.place(relx=0.55, rely=0.35)

    test12 = tk.StringVar()
    studiedGrammar= "Studied Grammar: "
    test12.set(studiedGrammar + count[15])
    text14 = tk.Label(frame2, textvariable=test12, bg="#201c1c", fg="white")
    text14.config(font=("UD_Digi_Kyokasho", 14)) 
    text14.place(relx=0.55, rely=0.45)


        # button on bottom of frame to change view
    canvas3 = tk.Canvas(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=300, height=50)
    text34 = canvas3.create_text(120, 30, text="<< View Daily Goals", fill="white", width="300", font=("UD_Digi_Kyokasho", 12, "bold"), anchor="center")
    canvas3.tag_bind(text34, "<Button-1>", toggleView)
    canvas3.config(cursor="hand2")
    canvas3.place(relx=0.6, rely=0.92)

    text1 = canvas3.create_text(120, 30, text="View JLPT Progress Graph >>", fill="white", width="300", font=("UD_Digi_Kyokasho", 12, "bold"), anchor="center")
    canvas3.tag_bind(text1, "<Button-1>", toggleView)

    canvas3.itemconfigure(text34, state='hidden')
    #View JLPT Progress Graph >>
    #View Daily Goals >>

    window.mainloop()
except:
    loadSimpleFrame()