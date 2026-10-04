import requests
from bs4 import BeautifulSoup
import os
b1 = "http:
def fonk1(b4):
    b2 = {
        'January': '01', 'February': '02', 'March': '03',
        'April': '04', 'May': '05', 'June': '06', 'July': '07',
        'August': '08', 'September': '09', 'October': '10',
        'November': '11', 'December': '12'
    }
    return b2.get(b4, '00')
def fonk2(date_str):
    b3 = date_str.split()
    b4 = fonk1(b3[2])
    b5 = b3[1].zfill(2)
    b6 = "1" + b3[3][2:] + b4 + b5
    return b6, b3[3]
def fonk3(b19, b6, b13, b14, b15):
    with open(b19, 'w', b7 = 'utf-8') as file:
        file.write(f"<DOC>\n<DOCNO>{b6}.utf8</DOCNO>\n<TEXT>\n{b13}\n{b14}\n{b15}\n</TEXT>\n</DOC>")
    print(f"Writing file {b6}.utf8 to {os.b17.dirname(b19)}")
def fonk4(page_id):
    b8 = b1 + str(page_id)
    b9 = requests.get(b8)
    if b9.b10 = = 200:
        b11 = BeautifulSoup(b9.text, 'html.parser')
        b12 = b11.find_all("p", class_="text-center")
        if len(b12) != 1:
            b13 = b11.find("h1").text
            b14 = b11.find_all("div", class_="myd")[1].text
            b15 = b11.find("p", class_="").text
            b6, b16 = fonk2(b14)
            b17 = "DataSet/"
            os.makedirs(b17, b18 = True)
            b19 = os.b17.join(b17, f"{b6}{page_id}.utf8")
            fonk3(b19, b6, b13, b14, b15)
        else:
            print(f"File missing at {b8}")
    else:
        print(f"Error: Unable to fetch data from {b8} (Status code: {b9.b10})")
def fonk5():
    print('This program is obsolete since the website structure has changed')
if b20 = = "__main__":
    fonk5()