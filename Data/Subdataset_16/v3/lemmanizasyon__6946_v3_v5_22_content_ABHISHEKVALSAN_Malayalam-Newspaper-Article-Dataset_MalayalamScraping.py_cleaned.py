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
    b6 = f"1{b3[3][2:]}{b4}{b5}"
    return b6, b3[3]
def fonk3(index):
    b7 = f"{b1}{index}"
    b8 = requests.get(b7)
    if b8.status_code != 200:
        print(f"Error fetching data from {b7}")
        return
    b9 = BeautifulSoup(b8.text, 'html.parser')
    b10 = b9.find_all("p", class_="text-center")
    if len(b10) == 1:
        print(f"File missing at {b7}")
        return
    b11 = b9.find("h1").text
    b12 = b9.find_all("div", class_="myd")[1].text
    b13 = b9.find("p", class_="").text
    b6, b14 = fonk2(b12)
    b15 = "DataSet"
    if not os.path.exists(b15):
        os.makedirs(b15)
    b16 = os.path.join(b15, f"{b6}{index}.utf8")
    with open(b16, 'w+', b17 = 'utf-8') as file:
        file.write(
            f"<DOC>\n"
            f"<DOCNO>{b6}</DOCNO>\n"
            f"<TEXT>\n"
            f"{b11}\n"
            f"{b12}\n"
            f"{b13}\n"
            f"</TEXT>\n"
            f"</DOC>"
        )
    print(f"Writing file {b6} to {b15}")
def fonk4():
    print('This program is obsolete since the website structure has changed')
if b18 = = "__main__":
    fonk4()