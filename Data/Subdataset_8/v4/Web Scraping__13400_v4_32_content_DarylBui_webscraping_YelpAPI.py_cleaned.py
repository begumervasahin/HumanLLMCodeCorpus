import json
import requests
from requests_oauthlib import OAuth1
api_key = "C7_OKghI_G9J3povKfvydoc0vibVrp_7jsUuyfzWGw0YtyNNwmIHhQBLF2WoutFlaJS10qGz9c2qMt_XHKgVawLozhOPxV8iLirJGzMy57Q7fGBPgJoOYA0CdtuW3Yx"
consumer_secret = 'JtcAesDkKuNltcKdwR7NEaUkgm8'
token = 'TCipoxU_lYo55-F3rS10XdnN6f-3-KQI'
token_secret = '5gAZ99Arn2x_LIOVM25AWy8H84c'
def do_search(term='Food', location='San Francisco'):
    base_url = 'https:
    term = term.replace(' ', '+')
    location = location.replace(' ', '+')
    url = "{base_url}?term={term}&location={location}".format(base_url=base_url,
                        term=term,
                        location=location)
    auth = OAuth1(api_key, consumer_secret, token, token_secret)
    response = requests.get(url, auth=auth)
    json_data = response.json()
    text_data = response.text
    return json_data, text_data
json_data, text_data = do_search()
python_data = json.loads(text_data)
print(json.dumps(json_data, indent=4, sort_keys=True))
for business in json_data['businesses']:
    print("Name:", business["name"])
    print("Phone:", business["phone"])
    print("Address:", " ".join(business["location"]["display_address"]))
    print("City:", business["location"]["city"])
    print()
