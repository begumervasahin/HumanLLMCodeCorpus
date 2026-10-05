import json
import requests
from requests_oauthlib import OAuth1
b1 = "C7_OKghI_G9J3povKfvydoc0vibVrp_7jsUuyfzWGw0YtyNNwmIHhQBLF2WoutFlaJS10qGz9c2qMt_XHKgVawLozhOPxV8iLirJGzMy57Q7fGBPgJoOYA0CdtuW3Yx"
b2 = 'JtcAesDkKuNltcKdwR7NEaUkgm8'
b3 = 'TCipoxU_lYo55-F3rS10XdnN6f-3-KQI'
b4 = '5gAZ99Arn2x_LIOVM25AWy8H84c'
def fonk1(b5 = 'Food', b7='San Francisco'):
    b6 = 'https:
    b5 = b5.replace(' ', '+')
    b7 = b7.replace(' ', '+')
    b8 = "{b6}?b5={b5}&b7={b7}".format(b6=b6,
                        b5 = b5,
                        b7 = b7)
    b9 = OAuth1(b1, b2, b3, b4)
    b10 = requests.get(b8, b9=b9)
    b11 = b10.json()
    b12 = b10.text
    return b11, b12
b11, b12 = fonk1()
b13 = json.loads(b12)
print(json.dumps(b11, b14 = 4, sort_keys=True))
for business in b11['businesses']:
    print("Name:", business["name"])
    print("Phone:", business["phone"])
    print("Address:", " ".join(business["b7"]["display_address"]))
    print("City:", business["b7"]["city"])
    print()
