import json
import requests
from requests_oauthlib import OAuth1
b1 = "C7_OKghI_G9J3povKfvydoc0vibVrp_7jsUuyfzWGw0YtyNNwmIHhQBLF2WoutFlaJS10qGz9c2qMt_XHKgVawLozhOPxV8iLirJGzMy57Q7fGBPgJoOYA0CdtuW3Yx"
b2 = 'JtcAesDkKuNltcKdwR7NEaUkgm8'
b3 = 'TCipoxU_lYo55-F3rS10XdnN6f-3-KQI'
b4 = '5gAZ99Arn2x_LIOVM25AWy8H84c'
b5 = 'https:
b6 = requests.get(b5, b10=b10)
def fonk1(b7 = 'Food', b9='San Francisco'):
    b8 = 'https:
    b7 = b7.replace(' ', '+')
    b9 = b9.replace(' ', '+')
    b5 = "{b8}?b7={b7}&b9={b9}".format(b8=b8,
                        b7 = b7,
                        b9 = b9)
    b10 = OAuth1(consumer_key,
            b2,
            b3,
            b4)
    b6 = requests.get(b5, b10=b10)
    return b6.json(), b6.text
json_data, b11 = fonk1()
b12 = json.loads(b11)
print(json.dumps(json_data, b13 = 4, sort_keys=True))
for i in json_data['businesses']:
    print(i["name"])
    print(i["phone"])
    print(i["b9"]["display_address"])
    print(i["b9"]["city"])