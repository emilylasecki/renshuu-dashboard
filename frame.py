# frame for GUI elements - load in physical things.
# text elements go in seperate method so reload only changes text - not the Gui

import tkinter as tk
from tkinter import Text
from PIL import ImageTk, Image
from pathlib import Path
import webbrowser
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import requests
import json
import pandas as pd
import os
import sys
from pathlib import Path

GraphVisible2 = False # use boolean to control what view is loaded

profileJson = "profile.json"
schedulesJson = "schedules.json"

home_dir = Path.home()  # use path to save api key to a file that can be modified

path = home_dir / "apikey.txt"

import os
import sys

def resource_path(relative_path):  # configure so pyinstaller can read path names
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#connect to Resnhuu server and load in content as needed
def reloadContent(api):
    api_key_path = resource_path(path)
    with open(api_key_path, "r") as file:
        api_key = file.read()

    """if api !=0:
        api_key = api"""
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }   
    url = 'https://api.renshuu.org/v1/profile/'  # get the number of reviews due today, kaochan, and jlpt
    url2 = 'https://api.renshuu.org/v1/schedule/' # get the lists to extract how many of each type of review is due

    # profile

    response = requests.get(url, headers=headers)

    correctProfilePath = resource_path(profileJson)
    correctSchedulePath = resource_path(schedulesJson)
    correctAPIpath = resource_path(path)

    print("Status code: ", response.status_code)
    x = response.json()

    filter_fields=['adventure_level', 'real_name', 'studied', 'api_usage', 'studied', 'kao', 'level_progress_percs']

    dict_result = { key: x[key]  for key in x if key in filter_fields}

    with open(correctProfilePath, "w") as outfile:  # extract desired fields into json file
        json.dump(dict_result, outfile)


    #schedules

    response = requests.get(url2, headers=headers)
    x = response.json()
    filter_fields=['schedules', 'today']
    dict_result = { key: x[key]  for key in x if key in filter_fields}

    with open(correctSchedulePath, "w") as outfile:  # extract desired fields into another json file - doesn't save with pyinstaller
        json.dump(dict_result, outfile)

    # get counts for the dashboard

    f = open(correctProfilePath)
    profile = json.load(f)
    try:
        downloadKao(profile['kao'], resource_path("myKao.png"))  #FIXME
    except:
        pass

    count = getCounts()
    return count

def downloadKao(image_url, file_dir): 
    response = requests.get(image_url)

    if response.status_code == 200:
        with open(file_dir, "wb") as fp:
            fp.write(response.content)
    else:
        print("Failed to download the image. Status code: {response.status_code}")


# get counts for schedules page
def getCounts():
    correctProfilePath = resource_path(profileJson)
    correctSchedulesPath = resource_path(schedulesJson)
    try:
        f = open(correctProfilePath)
        profile = json.load(f)

        r = open(correctSchedulesPath)
        schedules = json.load(r)
        history = schedules['schedules']

        i=0 
        k=0
        j=0
        l=0
        new_vocab=0
        review_vocab=0
        new_kanji=0
        review_kanji=0
        new_sentences=0
        review_sentences=0
        new_grammar=0
        review_grammar=0
        for schedules in history:
            if "vocab" in schedules['name'] or "Vocab" in schedules['name'] or "Words" in schedules['name'] or "words" in schedules['name']: 
                new_vocab = new_vocab + schedules['today']['new']
                review_vocab = review_vocab + schedules['today']['review']
                i=i+1

        for schedules in history:
            if "kanji" in schedules['name'] or "Kanji" in schedules['name']: 
                new_kanji = new_kanji + schedules['today']['new']
                review_kanji = review_kanji + schedules['today']['review']
                k=k+1

        for schedules in history:
            if "Sentences" in schedules['name'] or "sentences" in schedules['name']: 
                new_sentences = new_sentences + schedules['today']['new']
                review_sentences = review_sentences + schedules['today']['review']
                j=j+1

        for schedules in history: 
            if "" in schedules['name']:
                new_grammar = new_grammar + schedules['today']['new']
                review_grammar = review_grammar + schedules['today']['review']
                l=l+1 


        new_grammar = new_grammar - new_vocab - new_kanji - new_sentences
        review_grammar = review_grammar - review_vocab - review_sentences - review_kanji

        studied_grammar = profile['studied']['today_grammar']
        studied_vocab = profile['studied']['today_vocab']
        studied_kanji = profile['studied']['today_kanji']
        studied_sentences = profile['studied']['today_sent']

        a=0
        b=0
        c=0
        d=0

        # get counts of how many schedules previous data is pulled from
        # ended up not using these
        for schedules in history: 
            if "vocab" in schedules['name'] or "Vocab" in schedules['name'] or "Words" in schedules['name'] or "words" in schedules['name']: 
                if schedules['today']['review']!=0: 
                    a=a+1
        for schedules in history:  
            if "kanji" in schedules['name'] or "Kanji" in schedules['name']: 
                if schedules['today']['review']!=0: 
                    b=b+1
        for schedules in history:  
            if "Sentences" in schedules['name'] or "sentences" in schedules['name']: 
                if schedules['today']['review']!=0: 
                    c=c+1
        for schedules in history:
                if schedules['today']['review']!=0: 
                    d=d+1
        
        d= d -a - b -c


    # use matplotlib to take jlpt progress percents and make a graphic with it
        createGraph(correctProfilePath)

        count = [new_vocab, review_vocab, a, studied_vocab, new_kanji, review_kanji, b, studied_kanji, new_sentences, review_sentences, d, studied_sentences, new_grammar, review_grammar, d, studied_grammar]
        return count
    except:
        print("error occurred")
        count = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        return count

def createGraph(correctProfilePath):
    f = open(correctProfilePath)
    profile = json.load(f)
    df = profile['level_progress_percs']

    YAxis = ['Vocab', 'Kanji', 'Grammar', 'Sentences']
    XAxis = [profile['level_progress_percs']['vocab']['n5'], profile['level_progress_percs']['kanji']['n5'],profile['level_progress_percs']['grammar']['n5'],profile['level_progress_percs']['sent']['n5']]
    XAxis2 = [profile['level_progress_percs']['vocab']['n4'], profile['level_progress_percs']['kanji']['n4'],profile['level_progress_percs']['grammar']['n4'],profile['level_progress_percs']['sent']['n4']]
    XAxis3 = [profile['level_progress_percs']['vocab']['n3'], profile['level_progress_percs']['kanji']['n3'],profile['level_progress_percs']['grammar']['n3'],profile['level_progress_percs']['sent']['n3']]
    XAxis4 = [profile['level_progress_percs']['vocab']['n2'], profile['level_progress_percs']['kanji']['n2'],profile['level_progress_percs']['grammar']['n2'],profile['level_progress_percs']['sent']['n2']]
    XAxis5 = [profile['level_progress_percs']['vocab']['n1'], profile['level_progress_percs']['kanji']['n1'],profile['level_progress_percs']['grammar']['n1'],profile['level_progress_percs']['sent']['n1']]

    fid, axs = plt.subplots(5, sharex=True)

    bar0 = axs[0].barh(YAxis, XAxis)
    bar1 = axs[1].barh(YAxis, XAxis2)
    bar2 = axs[2].barh(YAxis, XAxis3)
    bar3 = axs[3].barh(YAxis, XAxis4)
    bar4 = axs[4].barh(YAxis, XAxis5)

    fid.set_size_inches(6,5)

    axs[0].bar_label(bar0, labels=[f"{x:.0f}%" for x in bar0.datavalues], color='white', padding = 3)
    axs[1].bar_label(bar1, labels=[f"{x:.0f}%" for x in bar1.datavalues], color='white', padding=3)
    axs[2].bar_label(bar2, labels=[f"{x:.0f}%" for x in bar2.datavalues], color='white', padding=3)
    axs[3].bar_label(bar3, labels=[f"{x:.0f}%" for x in bar3.datavalues], color='white', padding=3)
    axs[4].bar_label(bar4, labels=[f"{x:.0f}%" for x in bar4.datavalues], color='white', padding=3)

    axs[0].invert_yaxis()
    axs[1].invert_yaxis()
    axs[2].invert_yaxis()
    axs[3].invert_yaxis()
    axs[4].invert_yaxis()

    axs[0].barh(YAxis, XAxis)
    axs[1].barh(YAxis, XAxis2)
    axs[2].barh(YAxis, XAxis3)
    axs[3].barh(YAxis, XAxis4)
    axs[4].barh(YAxis, XAxis5)

    for s in ['top', 'bottom', 'left', 'right']:
        axs[0].spines[s].set_visible(False)
        axs[1].spines[s].set_visible(False)
        axs[2].spines[s].set_visible(False)
        axs[3].spines[s].set_visible(False)
        axs[4].spines[s].set_visible(False)

    axs[0].set_facecolor('#201c1c')
    axs[1].set_facecolor('#201c1c')
    axs[2].set_facecolor('#201c1c')
    axs[3].set_facecolor('#201c1c')
    axs[4].set_facecolor('#201c1c')
    fid.patch.set_facecolor('#201c1c')
    
    axs[0].set_title('N5', color='white')
    axs[1].set_title('N4', color='white')
    axs[2].set_title('N3', color='white')
    axs[3].set_title('N2', color='white')
    axs[4].set_title('N1', color='white')

    axs[0].yaxis.set_ticks(YAxis)
    axs[1].yaxis.set_ticks(YAxis)
    axs[2].yaxis.set_ticks(YAxis)
    axs[3].yaxis.set_ticks(YAxis)
    axs[4].yaxis.set_ticks(YAxis)

    axs[1].xaxis.set_ticks_position('none')
    axs[1].yaxis.set_ticks_position('none')
    axs[1].set_yticklabels(YAxis, fontsize=10, color='white')
    axs[0].xaxis.set_ticks_position('none')
    axs[0].yaxis.set_ticks_position('none')
    axs[0].set_yticklabels(YAxis, fontsize=10, color='white')
    axs[2].xaxis.set_ticks_position('none')
    axs[2].yaxis.set_ticks_position('none')
    axs[2].set_yticklabels(YAxis, fontsize=10, color='white')
    axs[3].xaxis.set_ticks_position('none')
    axs[3].yaxis.set_ticks_position('none')
    axs[3].set_yticklabels(YAxis, fontsize=10, color='white')
    axs[4].xaxis.set_ticks_position('none')
    axs[4].yaxis.set_ticks_position('none')
    axs[4].set_yticklabels(YAxis, fontsize=10, color='white')
    axs[4].axes.get_xaxis().set_visible(False)

    colorsValue = ["#5e5cd0", "#de8117", "#7acc18", "#d61145"]

    axs[0].barh(YAxis, XAxis, color = colorsValue)
    axs[1].barh(YAxis, XAxis2, color = colorsValue)
    axs[2].barh(YAxis, XAxis3, color = colorsValue)
    axs[3].barh(YAxis, XAxis4, color = colorsValue)
    axs[4].barh(YAxis, XAxis5, color = colorsValue)

    plt.savefig(resource_path("my_plot.png"), dpi=300, bbox_inches='tight') 


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

        test1.set(newVocab + count[0]) # get new counts when reload pressed
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

# create simple frame in the instance that the api key is not valid
def loadSimpleFrame():
    window.mainloop()
    reload()

def settingsClick(event=None):

    home_dir = Path.home()

    path = home_dir / "apikey.txt"

    canvas2.unbind('<Button-1>')
    newpath = resource_path(path)

    def closesettings():
        newWindow.destroy()
        try:
            canvas2.bind('<Button-1>', settingsClick)
        except:
            pass
    
    def updateAPIkey():
        input = inputtxt.get("1.0", "end-1c")
        # save input to new file
        if not os.path.exists(newpath):
            with open (newpath, 'w') as file:
                file.write(input)
        else:
            os.remove(newpath)
            with open (newpath, 'w') as file:
                file.write(input)
        closesettings()

    # open new frame with settings GUI and info 
    newWindow = tk.Tk()
    newWindow.title("Settings")
    newWindow.configure(background="#1c5669", borderwidth=19) # renshuu color
    newWindow.minsize(300,300)
    newWindow.maxsize(300,300)
    newWindow.geometry("500x500+1000+300")
    message = tk.Label(newWindow, text="Copy your Renshuu API key and paste it in the box below. Press update and then restart the program to review your Renshuu stats!", wraplength=260, bg="#1c5669", fg="white", anchor="center")
    message.config(font=("UD_Digi_Kyokasho",10, "bold"))
    inputtxt = tk.Text(newWindow, height=8, width=20)
    inputtxt.place(relx= 0.2, rely=0.35)
    UpdateButton = tk.Button(newWindow, text="Update",  command=updateAPIkey)
    UpdateButton.place(relx=0.42, rely=0.9)
    message.place(relx = 0.01, rely=0.01)
    newWindow.protocol("WM_DELETE_WINDOW", closesettings)
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
        canvas3.itemconfigure(text1, state='hidden')
        canvas3.itemconfigure(text34, state='normal')
    if GraphVisible2 == False:

        frame2.tkraise()
        canvas3.itemconfigure(text34, state='hidden')
        canvas3.itemconfigure(text1, state='normal')

def moreInfo(event=None): # create a GUI that gives info on how counts are calculated
    
    def closeFrame():
        moreInfoWindow.destroy()
        try:
            canvas7.bind("<Button-1>", moreInfo)
        except:
            pass

    def openGitHub():
        webbrowser.open_new("https://github.com/emilylasecki/renshuu-dashboard")
        
    canvas7.unbind("<Button-1>")
    moreInfoWindow = tk.Tk()
    moreInfoWindow.title("About renshuu dashboard")
    moreInfoWindow.configure(background="#201c1c", borderwidth=10)
    moreInfoWindow.minsize(400,550)
    moreInfoWindow.maxsize(400,550)
    text = Text(moreInfoWindow)
    text2 = Text(moreInfoWindow)
    text3 = tk.Label(moreInfoWindow, text="https://github.com/emilylasecki/renshuu-dashboard")
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

def goToRenshuu():
    webbrowser.open_new("https://www.renshuu.org")


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

    imgpath = resource_path("myKao.png")
    character = tk.PhotoImage(file=imgpath)
    imagetest = (Image.open(imgpath))
    img = imagetest.resize((100,100), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(50,50,image=img)  # potential change, image is squashed. Acceptable the way it is but could look better"""

    #title
    l = tk.Label(window, bg="#1c5669", text = "renshuu dashboard \n 毎日がんばってね!", width=15, height=0, font="UD_Digi_Kyokasho", fg="white", anchor="nw")
    l.bind("<Button-1>", lambda e: goToRenshuu())
    l.config(font=("UD_Digi_Kyokasho", 20, "bold"), cursor="hand2")
    l.grid(row=0,column=1)

    # settings button
    frame =tk.Frame(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=50, height =50)
    frame.place(relx=0.9, rely=0.0)

    canvas2 = tk.Canvas(frame, bg="#1c5669", borderwidth=0, highlightthickness=0, width=50, height=50)

    img2 = tk.PhotoImage(file=resource_path("settings.png"))
    imagetest2 = (Image.open(resource_path("settings.png")))
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

    l = tk.Label(frame2, bg="#201c1c", text = "Invalid API Key. Configure API key in settings!", width=480, height=0, font="UD_Digi_Kyokasho", fg="white", anchor="nw")
    l.place(relx = 0.05, rely = 0.5)
    canvas6 = tk.Canvas(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=40, height=40)
    imgforFrame = (Image.open(resource_path("ButtonReload.png")))
    imgagain = imgforFrame.resize((40,40), Image.Resampling.LANCZOS)
    imgAgain = ImageTk.PhotoImage(imgagain)

    canvas7 = tk.Canvas(window,bg="#1c5669", borderwidth=0, highlightthickness=0, width=40, height=40)
    i = Image.open(resource_path("questionMarkButton.png"))
    i2 = i.resize((40,40), Image.Resampling.LANCZOS)
    i3 = ImageTk.PhotoImage(i2)
    canvas7.create_image(40,40, image=i3, anchor="se")
    canvas7.place(relx=0.00, rely=0.93)
    canvas7.bind("<Button-1>", moreInfo)
    canvas7.config(cursor="hand2")

    imagetest2 = (Image.open(resource_path("my_plot.png")))
    img3 = imagetest2.resize((480,400), Image.Resampling.LANCZOS) 
    img3 = ImageTk.PhotoImage(img3)
    image_label2 = tk.Label(frame3, image =img3, borderwidth=0, highlightthickness=0)
    image_label2.pack()

    i=0
    while i<16:
        count[i] = str(count[i])
        i=i+1

    canvas6.create_image(40,40, image=imgAgain, anchor="se")
    canvas6.place(relx=0.75, rely=0.05)
    canvas6.bind("<Button-1>", reloadElements)
    canvas6.config(cursor="hand2")

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

    window.mainloop()
except:
    loadSimpleFrame()