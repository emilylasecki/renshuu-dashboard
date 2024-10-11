import requests
import json
import pandas
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