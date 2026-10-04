import requests
from bs4 import BeautifulSoup
import os
b1 = 'https:
def fonk1(month):
    b2 = {
        'January': '01', 'February': '02', 'March': '03',
        'April': '04', 'May': '05', 'June': '06', 'July': '07',
        'August': '08', 'September': '09', 'October': '10',
        'November': '11', 'December': '12'
    }
    return b2.get(month, '00')
def fonk2(date_str):
    b3 = date_str.split()
    b4 = fonk1(b3[2])
    b5 = b3[1].zfill(2)
    b6 = "1" + b3[3][2:] + b4 + b5
    return b6, b3[3]
def fonk3(index):
    b7 = b1 + str(index)
    b8 = requests.get(b7)
    if b8.b9 = = 200:
        b10 = BeautifulSoup(b8.text, 'html.parser')
        b11 = b10.findAll("p", {"class": "text-center"})
        if len(b11) != 1:
            b12 = b10.find("h1").text
            b13 = b10.findAll("div", {"class": "myd"})[1].text
            b14 = b10.find("p", {"class": ""}).text
            b6, b15 = fonk2(b13)
            b16 = "DataSet/"
            b17 = os.b16.join(b16, f"{b6}{index}.utf8")
            with open(b17, 'w+', b18 = 'utf-8') as file:
                file.write(f"<DOC>\n<DOCNO>{b6}</DOCNO>\n<TEXT>\n{b12}\n{b13}\n{b14}\n</TEXT>\n</DOC>")
            print(f"Writing file {b6} to {b16}")
        else:
            print(f"File missing at {b7}")
    else:
        print(f"Error fetching data from {b7}")
def fonk4():
    print('This program is obsolete since the website structure has changed')
if b19 = = "__main__":
    fonk4()