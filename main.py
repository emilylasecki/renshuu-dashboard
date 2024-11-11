# main for running elements to be displayed on GUI
# add a feature so if renshuu is down it displays the message that it is currently unavailable.

import requests
import json
import pandas as pd
from api_key import api_key


#connect to Resnhuu server and load in content as needed
def main():

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }   
    url = 'https://api.renshuu.org/v1/profile/'  # get the number of reviews due today
    url2 = 'https://api.renshuu.org/v1/schedule/' # get the lists to extract how many of each type of review is due

    # part 1 - profile

    response = requests.get(url, headers=headers)

    print(response.status_code)
    x = response.json()
    print(json.dumps(x, indent=4, sort_keys=True))

    filter_fields=['adventure_level', 'real_name', 'studied', 'api_usage', 'studied', 'kao']

    dict_result = { key: x[key]  for key in x if key in filter_fields}

    with open("profile.json", "w") as outfile:  # extract desired fields into json file
        json.dump(dict_result, outfile)

    
    df = pd.read_json("profile.json", lines=True)
    df.to_excel("API_Stuff.xlsx")

   # print(dict_result)

    # part 2 - schedules

    response = requests.get(url2, headers=headers)
    x = response.json()
    print(json.dumps(x, indent=4, sort_keys=True))
    filter_fields=['schedules', 'today']
    dict_result = { key: x[key]  for key in x if key in filter_fields}

    with open("schedules.json", "w") as outfile:  # extract desired fields into another json file
        json.dump(dict_result, outfile)
        #data = json.load(outfile)

    f = open('profile.json')
    file = json.load(f)
    name = file['kao']
    print(name)

    r = open('schedules.json')
    file2 = json.load(r)
    history = file2['schedules']

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
            new_vocab = new_vocab + schedules['today']['review']
            review_vocab = review_vocab + schedules['today']['new']
            i=i+1

    for schedules in history:
        if "kanji" in schedules['name'] or "Kanji" in schedules['name']: 
            new_kanji = new_kanji + schedules['today']['review']
            review_kanji = review_kanji + schedules['today']['new']
            k=k+1

    for schedules in history:
        if "Sentences" in schedules['name'] or "sentences" in schedules['name']: 
            new_sentences = new_sentences + schedules['today']['review']
            review_sentences = review_sentences + schedules['today']['new']
            j=j+1

    for schedules in history:  # FIXME grammar not returning proper values
        if "Sentences" not in schedules['name'] or "sentences" not in schedules['name'] or "kanji" not in schedules['name'] or "Kanji" not in schedules['name'] or "vocab" not in schedules['name'] or "Vocab" not in schedules['name'] or "Words" not in schedules['name'] or "words" not in schedules['name']:
            new_grammar = new_grammar + schedules['today']['review']
            review_grammar = review_grammar + schedules['today']['new']
            l=l+1



    #print(",".join(map(str, data)))
    print(new_vocab, review_vocab)
    print(new_kanji, review_kanji)
    print(new_sentences, review_sentences)
    print(new_grammar, review_grammar)
    print(i)
    print(k)
    print(j)
    print(l)

    #history2 = file['studied']

    grammar = file['studied']['today_grammar']
    vocab = file['studied']['today_vocab']
    kanji = file['studied']['today_kanji']
    sentences = file['studied']['today_sent']

    print(grammar, vocab, kanji, sentences)

    #name = file2['schedules']['id']
    #val = m['name']
    #print(val)

# reload stats upon click
# placeholder fucntion, all of main will go in here later
def reload():

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }   

    #endpoint = '/v1/profile'
    url = 'https://api.renshuu.org/v1/profile'

    response = requests.get(url, headers=headers)

    print(response.status_code) # 200 is good
    x = response.json()
    print(json.dumps(x, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()