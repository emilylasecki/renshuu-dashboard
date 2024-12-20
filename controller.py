# main for running elements to be displayed on GUI
# add a feature so if renshuu is down it displays the message that it is currently unavailable.


import requests
import json
import pandas as pd
try:
    from Apikey import api_key
except:
    pass
from jlptProgressGraph import *

profileJson = "GUI_assets\profile.json"
schedulesJson = "GUI_assets\schedules.json"

path= "Apikey.py"

#connect to Resnhuu server and load in content as needed
def reloadContent(api):
    """if api !=0:
        api_key = api"""
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }   
    url = 'https://api.renshuu.org/v1/profile/'  # get the number of reviews due today, kaochan, and jlpt
    url2 = 'https://api.renshuu.org/v1/schedule/' # get the lists to extract how many of each type of review is due

    # part 1 - profile

    response = requests.get(url, headers=headers)

    print("Status code: ", response.status_code)
    x = response.json()

    filter_fields=['adventure_level', 'real_name', 'studied', 'api_usage', 'studied', 'kao', 'level_progress_percs']

    dict_result = { key: x[key]  for key in x if key in filter_fields}

    with open(profileJson, "w") as outfile:  # extract desired fields into json file
        json.dump(dict_result, outfile)
    
    #schedules

    response = requests.get(url2, headers=headers)
    x = response.json()
    filter_fields=['schedules', 'today']
    dict_result = { key: x[key]  for key in x if key in filter_fields}

    with open(schedulesJson, "w") as outfile:  # extract desired fields into another json file
        json.dump(dict_result, outfile)

    # get counts for the dashboard

    f = open(profileJson)
    profile = json.load(f)
    try:
        downloadKao(profile['kao'], "GUI_assets\myKao.png")  #FIXME
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
    try:
        f = open(profileJson)
        profile = json.load(f)

        r = open(schedulesJson)
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

      #  print(review_vocab)


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
         # ended up not using these counts
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
        createGraph(profileJson)

        count = [new_vocab, review_vocab, a, studied_vocab, new_kanji, review_kanji, b, studied_kanji, new_sentences, review_sentences, d, studied_sentences, new_grammar, review_grammar, d, studied_grammar]
        return count
    except:
      #  print("api key still not valid")
        count = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        return count

