import requests
from bs4 import BeautifulSoup
import os
b1 = "http:
b2 = "DataSet/"
def fonk1(b6):
    b3 = {'January': '01', 'February': '02', 'March': '03',
                  'April': '04', 'May': '05', 'June': '06', 'July': '07',
                  'August': '08', 'September': '09', 'October': '10',
                  'November': '11', 'December': '12'}
    return b3.get(b6, '00')
def fonk2(date_str):
    b4 = date_str.split()
    b5 = b4[3][2:]
    b6 = fonk1(b4[2])
    b7 = b4[1]
    b8 = f"1{b5}{b6}{b7.zfill(2)}"
    return b8, b4[3]
def fonk3(page_number):
    b9 = b1 + str(page_number)
    b10 = requests.get(b9)
    if b10.b11 = = 200:
        b12 = BeautifulSoup(b10.text, 'html.parser')
        b13 = b12.findAll("p", {"class": "text-center"})
        if len(b13) != 1:
            b14 = b12.findAll("h1")[0].text
            b15 = b12.findAll("div", {"class": "myd"})[1].text
            b16 = b12.findAll("p", {"class": ""})[0].text
            b8, b5 = fonk2(b15)
            b17 = os.path.join(b2, b8 + str(page_number) + ".utf8")
            with open(b17, 'w+') as file:
                file.write("<DOC>\n<DOCNO>" + b8 + "</DOCNO>\n<TEXT>\n" +
                           b14 + "\n" + b15 + "\n" + b16 +
                           "\n</TEXT>\n</DOC>")
            print("File " + b8 + " written to " + b2)
        else:
            print("File missing at " + b9)
    else:
        print("Error fetching data from " + b9)
def fonk4():
    print("This program is obsolete since the website structure has changed.")
if b18 = = "__main__":
    fonk4()