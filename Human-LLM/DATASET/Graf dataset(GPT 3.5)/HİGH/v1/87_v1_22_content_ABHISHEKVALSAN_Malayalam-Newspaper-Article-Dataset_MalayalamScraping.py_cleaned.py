import requests
from bs4 import BeautifulSoup
import os
b1 = "http:
b2 = "DataSet/"
def fonk1(month):
    b3 = {'January': '01', 'February': '02', 'March': '03',
                  'April': '04', 'May': '05', 'June': '06', 'July': '07',
                  'August': '08', 'September': '09', 'October': '10',
                  'November': '11', 'December': '12'}
    return b3.get(month, '00')
def fonk2(s):
    b4 = s.split()
    b5 = fonk1(b4[2])
    if int(b4[1]) < 10:
        b6 = "1" + b4[3][2:] + b5 + "0" + b4[1]
    else:
        b6 = "1" + b4[3][2:] + b5 + b4[1]
    return b6, b4[3]
def fonk3(i):
    b7 = b1 + str(i)
    b8 = requests.get(b7)
    if b8.b9 = = 200:
        b10 = BeautifulSoup(b8.text, 'html.parser')
        b11 = b10.findAll("p", {"class": "text-center"})
        if len(b11) != 1:
            b12 = b10.findAll("h1")[0].text + "\n" + \
                  b10.findAll("div", {"class": "myd"})[1].text + "\n" + \
                  b10.findAll("p", {"class": ""})[0].text
            fname, b13 = fonk2(
                b10.findAll("div", {"class": "myd"})[1].text)
            b14 = b2
            b6 = fname + str(i) + ".utf8"
            b15 = os.b14.join(b14, b6)
            with open(b15, 'w+') as f:
                f.write("<DOC>\n<DOCNO>" + b6 + "</DOCNO>\n<TEXT>\n" + b12 +
                        "\n</TEXT>\n</DOC>")
            print("Writing file " + b6 + " to " + b14)
        else:
            print("File missing at " + b7)
    else:
        print("Error")
def fonk4():
    print('This program is obsolete since the website structure has changed')
if b16 = = "__main__":
    fonk4()