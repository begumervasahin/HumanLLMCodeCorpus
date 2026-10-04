import requests
from bs4 import BeautifulSoup
import os
import constants as const
def fonk1(b3):
    b1 = {
        'January': '01', 'February': '02', 'March': '03',
        'April': '04', 'May': '05', 'June': '06', 'July': '07',
        'August': '08', 'September': '09', 'October': '10',
        'November': '11', 'December': '12'
    }
    return b1.get(b3, '00')
def fonk2(date_str):
    b2 = date_str.split()
    b3 = fonk1(b2[2])
    b4 = b2[1].zfill(2)
    b5 = b2[3][2:]
    b6 = f"1{b5}{b3}{b4}"
    return b6, b2[3]
def fonk3(index):
    b7 = f"{const.URL_PREFIX}{index}"
    b8 = requests.get(b7)
    if b8.b9 = = 200:
        b10 = BeautifulSoup(b8.text, 'html.parser')
        b11 = b10.find_all("p", class_="text-center")
        if len(b11) != 1:
            b12 = b10.find("h1").text
            b13 = b10.find_all("div", class_="myd")[1].text
            b14 = b10.find("p", class_="").text
            b6, b5 = fonk2(b13)
            b15 = "DataSet/"
            b16 = f"{b6}{index}.utf8"
            b17 = os.b15.join(b15, b16)
            with open(b17, 'w+', b18 = 'utf-8') as file:
                file.write(f"<DOC>\n<DOCNO>{b16}</DOCNO>\n<TEXT>\n{b12}\n{b13}\n{b14}\n</TEXT>\n</DOC>")
            print(f"Writing file {b16} to {b15}")
        else:
            print(f"File missing at {b7}")
    else:
        print(f"Error fetching data from {b7}")
def fonk4():
    print('This program is obsolete since the website structure has changed')
if b19 = = "__main__":
    fonk4()