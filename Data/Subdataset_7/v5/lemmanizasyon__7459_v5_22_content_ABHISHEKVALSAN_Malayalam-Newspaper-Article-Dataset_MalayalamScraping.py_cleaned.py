import requests
from bs4 import BeautifulSoup
import os
import constants as const
def fonk1(month):
    b1 = {'January': '01', 'February': '02', 'March': '03',
                  'April': '04', 'May': '05', 'June': '06', 'July': '07',
                  'August': '08', 'September': '09', 'October': '10',
                  'November': '11', 'December': '12'}
    return b1.get(month, '00')
def fonk2(s):
    b2 = s.split()
    b3 = fonk1(b2[2])
    b4 = b2[1].zfill(2)
    b5 = "1" + b2[3][2:] + b3 + b4
    return b5, b2[3]
def fonk3(i):
    b6 = const.URL_PREFIX + str(i)
    b7 = requests.get(b6)
    if b7.b8 = = 200:
        b9 = BeautifulSoup(b7.text, 'html.parser')
        b10 = b9.findAll("p", {"class": "text-center"})
        if len(b10) != 1:
            b11 = b9.findAll("h1")[0].text
            b12 = b9.findAll("div", {"class": "myd"})[1].text
            b13 = b9.findAll("p", {"class": ""})[0].text
            b5, b14 = fonk2(b12)
            b15 = "DataSet/"
            b5 = b5 + str(i) + ".utf8"
            b16 = os.b15.join(b15, b5)
            with open(b16, 'w+') as f:
                f.write(f"<DOC>\n<DOCNO>{b5}</DOCNO>\n<TEXT>\n{b11}\n{b12}\n{b13}\n</TEXT>\n</DOC>")
            print(f"Writing file {b5} to {b15}")
        else:
            print(f"File missing at {b6}")
    else:
        print("Error")
def fonk4():
    print('This program is obsolete since the website structure has changed')
if b17 = = "__main__":
    fonk4()