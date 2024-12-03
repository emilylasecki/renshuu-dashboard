# frame for GUI elements - load in physical things.
# text elements go in seperate method so reload only changes text - not the Gui

import tkinter as tk
from PIL import ImageTk, Image
from controller import *
from pathlib import Path

GraphVisible2 = False # use boolean to control what view is loaded

def reload(event=None):
    try:
        count = reloadContent()
        i=0
        for element in count:
          #  print(count[i])
            i=i+1
            return count
    except:
        print("api key invalid")
       # settingsClick()
    #canvas4.pack_forget()

def reloadElements(event): #FIXME add this functionality - currently doesn't operate as expected
   # frame2.forget()  # destroy works but pack doesn't
    count = reloadContent()
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
    # reload with new image - don't think image is actually updating

def loadSimpleFrame():
    window.mainloop()
    reload()
   # reloadElements(event=None)

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
        newWindow.destroy()
        reloadElements(event=None)

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
    newWindow.mainloop()

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
       # canvas5.tkraise()
        canvas3.itemconfigure(text1, state='hidden')
        canvas3.itemconfigure(text34, state='normal')
    if GraphVisible2 == False:
       # canvas5.tag_raise()
        frame2.tkraise()
        canvas3.itemconfigure(text34, state='hidden')
        canvas3.itemconfigure(text1, state='normal')
      #  canvas3.tag_raise("all")
       # canvas3.tag_raise(text34)
        

#create the window
try:
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

   # frame4 =tk.Frame(window, bg="#201c1c", borderwidth=5, highlightthickness=0, width=480, height=400)
   # frame4.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

    frame3 =tk.Frame(window, bg="#201c1c", borderwidth=5, highlightthickness=0, width=480, height=400)
    frame3.place(relx=0.5, rely=0.56, anchor=tk.CENTER)


    frame2 =tk.Frame(window, bg="#201c1c", borderwidth=5, highlightthickness=0, width=480, height=400)
    frame2.place(relx=0.5, rely=0.56, anchor=tk.CENTER)



    # create condition for this to show later: displays graph on frame
    imagetest2 = (Image.open("GUI_assets\my_plot.png"))
    img3 = imagetest2.resize((480,400), Image.Resampling.LANCZOS) 
    img3 = ImageTk.PhotoImage(img3)
    image_label2 = tk.Label(frame3, image =img3, borderwidth=0, highlightthickness=0)
    image_label2.pack()

   # l = tk.Label(frame2, )
    l = tk.Label(frame2, bg="#1c5669", text = "Invalid API Key. Configure API key in settings!", width=500, height=0, font="UD_Digi_Kyokasho", fg="white", anchor="nw")
    l.place(relx = 0.01, rely = 0.5)

    canvas4 = tk.Canvas(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=60, height=60)
    canvas4.place(relx=0.7, rely=0.03)
    text2 = canvas4.create_text(30, 20, text="Reload Stats", fill="white", width="60", font=("UD_Digi_Kyokasho", 12, "bold"), anchor="center")
    canvas4.tag_bind(text2, "<Button-1>", reloadElements)
    canvas4.config(cursor="hand2")

    #for reference
    # count = [new_vocab, review_vocab, a, studied_vocab, new_kanji, review_kanji, b, studied_kanji, new_sentences, review_sentences, d, studied_sentences, new_grammar, review_grammar, d, studied_grammar]
    i=0
    while i<16:
        count[i] = str(count[i])
        i=i+1

    l.destroy()


    #text0 = tk.StringVar(frame2,"Today's Goals")
    text = tk.Label(frame2, text="Today's Goals", bg="#201c1c", fg="white")
    text.config(font=("UD_Digi_Kyokasho", 20)) 
    text.place(relx=0.05, rely=0.05)


    test1 = tk.StringVar()
    newVocab = "New Vocab: "
    test1.set(newVocab + count[0])
    text2 = tk.Label(frame2, textvariable= test1, bg="#201c1c", fg="white")
    text2.config(font=("UD_Digi_Kyokasho", 14)) 
    text2.place(relx=0.05, rely=0.2)

    test2 = tk.StringVar()
    reviewVocab = "Review Vocab: "
    test2.set(reviewVocab + count[1])
    text3 = tk.Label(frame2, textvariable= test2, bg="#201c1c", fg="white")
    text3.config(font=("UD_Digi_Kyokasho", 14)) 
    text3.place(relx=0.05, rely=0.3)

    test3 = tk.StringVar()
    newKanji = "New Kanji: "
    test3.set(newKanji + count[4])
    text4 = tk.Label(frame2, textvariable=test3, bg="#201c1c", fg="white")
    text4.config(font=("UD_Digi_Kyokasho", 14)) 
    text4.place(relx=0.05, rely=0.4)

    test4 = tk.StringVar()
    reviewKanji = "Review Kanji: "
    test4.set(reviewKanji + count[5])
    text5 = tk.Label(frame2, textvariable=test4, bg="#201c1c", fg="white")
    text5.config(font=("UD_Digi_Kyokasho", 14)) 
    text5.place(relx=0.05, rely=0.5)

    test5 = tk.StringVar()
    newSentences = "New Sentecnes: "
    test5.set(newSentences + count[8])
    text6 = tk.Label(frame2, textvariable=test5, bg="#201c1c", fg="white")
    text6.config(font=("UD_Digi_Kyokasho", 14)) 
    text6.place(relx=0.05, rely=0.6)

    test6= tk.StringVar()
    reviewSentences = "Review Sentences: "
    test6.set(reviewSentences + count[9])
    text7 = tk.Label(frame2, textvariable=test6, bg="#201c1c", fg="white")
    text7.config(font=("UD_Digi_Kyokasho", 14)) 
    text7.place(relx=0.05, rely=0.7)

    test7 = tk.StringVar()
    newGrammar = "New Grammar: "
    test7.set(newGrammar + count[12])
    text8 = tk.Label(frame2, textvariable=test7, bg="#201c1c", fg="white")
    text8.config(font=("UD_Digi_Kyokasho", 14)) 
    text8.place(relx=0.05, rely=0.8)

    test8 = tk.StringVar()
    reviewGrammar = "Review Grammar: "
    test8.set(reviewGrammar + count[13])
    text9 = tk.Label(frame2, textvariable=test8, bg="#201c1c", fg="white")
    text9.config(font=("UD_Digi_Kyokasho", 14)) 
    text9.place(relx=0.05, rely=0.9)

    text10 = tk.Label(frame2, text= "Today Done ", bg="#201c1c", fg="white")
    text10.config(font=("UD_Digi_Kyokasho", 20)) 
    text10.place(relx=0.6, rely=0.05)

    test9 = tk.StringVar()
    studiedVocab = "Studied Vocab: "
    test9.set(studiedVocab + count[3])
    text11 = tk.Label(frame2, textvariable=test9, bg="#201c1c", fg="white")
    text11.config(font=("UD_Digi_Kyokasho", 14)) 
    text11.place(relx=0.6, rely=0.2)

    test10 = tk.StringVar()
    studiedKanji = "Studied Kanji: "
    test10.set(studiedKanji + count[7])
    text12 = tk.Label(frame2, textvariable=test10, bg="#201c1c", fg="white")
    text12.config(font=("UD_Digi_Kyokasho", 14)) 
    text12.place(relx=0.6, rely=0.3)

    test11 = tk.StringVar()
    studiedSentences = "Studied Sentences: "
    test11.set(studiedSentences + count[11])
    text13 = tk.Label(frame2, textvariable=test11, bg="#201c1c", fg="white")
    text13.config(font=("UD_Digi_Kyokasho", 14)) 
    text13.place(relx=0.6, rely=0.4)

    test12 = tk.StringVar()
    studiedGrammar= "Studied Grammar: "
    test12.set(studiedGrammar + count[15])
    text14 = tk.Label(frame2, textvariable=test12, bg="#201c1c", fg="white")
    text14.config(font=("UD_Digi_Kyokasho", 14)) 
    text14.place(relx=0.6, rely=0.5)


        # button on bottom of frame to change view
    canvas3 = tk.Canvas(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=300, height=50)
    text34 = canvas3.create_text(120, 30, text="View Daily Goals >>", fill="white", width="300", font=("UD_Digi_Kyokasho", 12, "bold"), anchor="center")
    canvas3.tag_bind(text34, "<Button-1>", toggleView)
    canvas3.config(cursor="hand2")
    canvas3.place(relx=0.6, rely=0.92)

   # canvas5 = tk.Canvas(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=300, height=50)
    text1 = canvas3.create_text(120, 30, text="View JLPT Progress Graph >>", fill="white", width="300", font=("UD_Digi_Kyokasho", 12, "bold"), anchor="center")
    canvas3.tag_bind(text1, "<Button-1>", toggleView)

    canvas3.itemconfigure(text34, state='hidden')
   # canvas5.config(cursor="hand2")
   # canvas5.place(relx=0.6, rely=0.92)
    #View JLPT Progress Graph >>
    #View Daily Goals >>

    window.mainloop()
except:
    loadSimpleFrame()


