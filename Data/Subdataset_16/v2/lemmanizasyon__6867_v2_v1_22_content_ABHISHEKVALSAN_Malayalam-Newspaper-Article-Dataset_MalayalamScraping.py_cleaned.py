import requests
from bs4 import BeautifulSoup
import os
b1 = "http:
b2 = "DataSet/"
def fonk1(b5):
    b3 = {
        'January': '01', 'February': '02', 'March': '03',
        'April': '04', 'May': '05', 'June': '06', 'July': '07',
        'August': '08', 'September': '09', 'October': '10',
        'November': '11', 'December': '12'
    }
    return b3.get(b5, '00')
def fonk2(date_str):
    b4 = date_str.split()
    b5 = fonk1(b4[2])
    b6 = b4[1]
    b7 = b4[3][2:]
    if int(b6) < 10:
        b8 = f"1{b7}{b5}0{b6}"
    else:
        b8 = f"1{b7}{b5}{b6}"
    return b8, b4[3]
def fonk3(page_number):
    b9 = f"{b1}{page_number}"
    b10 = requests.get(b9)
    if b10.b11 = = 200:
        b12 = BeautifulSoup(b10.text, 'html.parser')
        b13 = b12.find_all("p", class_="text-center")
        if len(b13) != 1:
            b14 = b12.find("h1").text
            b15 = b12.find_all("div", class_="myd")[1].text
            b16 = b12.find("p", class_="").text
            b17 = f"{b14}\n{b15}\n{b16}"
            b8, b18 = fonk2(b15)
            b8 = f"{b8}{page_number}.utf8"
            b19 = os.path.join(b2, b8)
            os.makedirs(b2, b20 = True)
            with open(b19, 'w+', b21 = 'utf-8') as file:
                file.write(f"<DOC>\n<DOCNO>{b8}</DOCNO>\n<TEXT>\n{b17}\n</TEXT>\n</DOC>")
            print(f"Writing file {b8} to {b2}")
        else:
            print(f"File missing at {b9}")
    else:
        print(f"Error fetching data from {b9}")
def fonk4():
    print('This program is obsolete since the website structure has changed')
if b22 = = "__main__":
    fonk4()