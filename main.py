# main for running elements to be displayed on GUI
# add a feature so if renshuu is down it displays the message that it is currently unavailable.

import requests
import json
import pandas as pd
from api_key import api_key


#objective
def main():

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }   

    #endpoint = '/v1/profile'
    url = 'https://api.renshuu.org/v1/profile'

    response = requests.get(url, headers=headers)
    #print(response)

    print(response.status_code)
    x = response.json()
    #y = json.loads(x)
    print(json.dumps(x, indent=4, sort_keys=True))

    filter_fields=['adventure_level', 'real_name', 'studied', 'api_usage']

    dict_result = { key: x[key]  for key in x if key in filter_fields}

    toExcel = { key: x[key]  for key in x }

    with open("API_stuff.json", "w") as outfile:  # extract desired fields into json file
        json.dump(dict_result, outfile)

    
    df = pd.read_json("API_stuff.json", lines=True)
    df.to_excel("API_Stuff.xlsx")

    print(dict_result)

   # if key in x if in key in filter_fields:
    #    print(key, x)

    #print(y["adventure_level"])
    #print(response.json())


# reload stats upon click
def reload():
    print("place holder")

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