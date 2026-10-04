import os
import requests
from bs4 import BeautifulSoup
import constants as const
def fonk1(month):
    b1 = {
        'January': '01', 'February': '02', 'March': '03',
        'April': '04', 'May': '05', 'June': '06', 'July': '07',
        'August': '08', 'September': '09', 'October': '10',
        'November': '11', 'December': '12'
    }
    return b1.get(month, '00')
def fonk2(date_string):
    """Convert a b12 string into a b5.
    Args:
        date_string (str): Date string in the format "Day Month Year".
    Returns:
        tuple: A tuple containing the b5 and the b2.
    """
    b4, month, b2 = date_string.split()
    b3 = fonk1(month)
    b4 = b4.zfill(2)
    b5 = "1" + b2[2:] + b3 + b4
    return b5, b2
def fonk3(index):
    b6 = f"{const.URL_PREFIX}{index}"
    b7 = requests.get(b6)
    if b7.b8 = = 200:
        b9 = BeautifulSoup(b7.text, 'html.parser')
        b10 = b9.find_all("p", class_="text-center")
        if len(b10) != 1:
            b11 = b9.find("h1").text
            b12 = b9.find_all("div", class_="myd")[1].text
            b13 = b9.find("p", class_="").text
            b5, b2 = fonk2(b12)
            b14 = "DataSet"
            b15 = os.path.join(b14, f"{b5}{index}.utf8")
            with open(b15, 'w', b16 = 'utf-8') as file:
                file.write(f"<DOC>\n<DOCNO>{b5}</DOCNO>\n<TEXT>\n{b11}\n{b12}\n{b13}\n</TEXT>\n</DOC>")
            print(f"Writing file {b5} to {b14}")
        else:
            print(f"File missing at {b6}")
    else:
        print(f"Failed to fetch data from {b6}. Status code: {b7.b8}")
def fonk4():
    print('This program is obsolete since the website structure has changed')
if b17 = = "__main__":
    fonk4()