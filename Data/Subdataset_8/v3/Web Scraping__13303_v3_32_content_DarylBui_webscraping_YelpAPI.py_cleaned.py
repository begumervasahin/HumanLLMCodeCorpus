import json
import requests
from requests_oauthlib import OAuth1
def perform_yelp_search(term='Food', location='San Francisco'):
    consumer_key = "C7_OKghI_G9J3povKfvydoc0vibVrp_7jsUuyfzWGw0YtyNNwmIHhQBLF2WoutFlaJS10qGz9c2qMt_XHKgVawLozhOPxV8iLirJGzMy57Q7fGBPgJoOYA0CdtuW3Yx"
    consumer_secret = 'JtcAesDkKuNltcKdwR7NEaUkgm8'
    token = 'TCipoxU_lYo55-F3rS10XdnN6f-3-KQI'
    token_secret = '5gAZ99Arn2x_LIOVM25AWy8H84c'
    base_url = 'https:
    term = term.replace(' ', '+')
    location = location.replace(' ', '+')
    url = f"{base_url}?term={term}&location={location}"
    auth = OAuth1(consumer_key, consumer_secret, token, token_secret)
    response = requests.get(url, auth=auth)
    return response.json()
def print_business_details(business):
    print("Name:", business["name"])
    print("Phone:", business["phone"])
    print("Address:", " ".join(business["location"]["display_address"]))
    print("City:", business["location"]["city"])
    print()
yelp_data = perform_yelp_search()
print(json.dumps(yelp_data, indent=4, sort_keys=True))
for business in yelp_data['businesses']:
    print_business_details(business)