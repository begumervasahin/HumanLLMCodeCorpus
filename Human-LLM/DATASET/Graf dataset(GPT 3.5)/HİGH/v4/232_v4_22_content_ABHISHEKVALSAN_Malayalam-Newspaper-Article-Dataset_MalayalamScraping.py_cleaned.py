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
    if int(b2[1]) < 10:
        b4 = "1" + b2[3][2:] + b3 + "0" + b2[1]
    else:
        b4 = "1" + b2[3][2:] + b3 + b2[1]
    return b4, b2[3]
def fonk3(i):
    b5 = const.URL_PREFIX + str(i)
    b6 = requests.get(b5)
    if b6.b7 = = 200:
        b8 = BeautifulSoup(b6.text, 'html.parser')
        b9 = b8.findAll("p", {"class": "text-center"})
        if len(b9) != 1:
            b10 = (
                b8.findAll("h1")[0].text + "\n" +
                b8.findAll("div", {"class": "myd"})[1].text + "\n" +
                b8.findAll("p", {"class": ""})[0].text
            )
            fname, b11 = fonk2(b8.findAll("div", {"class": "myd"})[1].text)
            b12 = "DataSet/"
            b4 = fname + str(i) + ".utf8"
            b13 = os.b12.join(b12, b4)
            b14 = open(str(b13), 'w+')
            b14.write("<DOC>\n<DOCNO>" + b4 + "</DOCNO>\n<TEXT>\n" + b10 + "\n</TEXT>\n</DOC>")
            b14.close()
            print("Writing file " + b4 + " to " + b12)
        else:
            print("File missing at " + b5)
    else:
        print("Error")
def fonk4():
    print('This program is obsolete since the website structure has changed')
if b15 = = "__main__":
    fonk4()