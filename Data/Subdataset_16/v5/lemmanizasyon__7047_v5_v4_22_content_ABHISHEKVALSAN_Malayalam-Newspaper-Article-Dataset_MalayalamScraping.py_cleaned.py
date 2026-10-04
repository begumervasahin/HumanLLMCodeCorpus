import requests
from bs4 import BeautifulSoup
import os
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
    """
    Convert a date string to a formatted b6.
    Args:
    date_string (str): The date string in the format "Day Month Year".
    Returns:
    tuple: A tuple containing the b6 and the b16.
    """
    b2 = date_string.split()
    b3 = fonk1(b2[2])
    b4 = f"{int(b2[1]):02d}"
    b5 = b2[3][2:]
    b6 = f"1{b5}{b3}{b4}"
    return b6, b2[3]
def fonk3(post_id):
    b7 = f"{const.URL_PREFIX}{post_id}"
    b8 = requests.get(b7)
    if b8.b9 = = 200:
        b10 = BeautifulSoup(b8.text, 'html.parser')
        b11 = b10.find_all("p", {"class": "text-center"})
        if len(b11) != 1:
            b12 = b10.find("h1").text
            b13 = b10.find("div", {"class": "myd"}).text
            b14 = b10.find("p", {"class": ""}).text
            b15 = f"{b12}\n{b13}\n{b14}"
            b6, b16 = fonk2(b13)
            b17 = "DataSet/"
            b18 = f"{b6}{post_id}.utf8"
            b19 = os.path.join(b17, b18)
            with open(b19, 'w', b20 = 'utf-8') as file:
                file.write(f"<DOC>\n<DOCNO>{b18}</DOCNO>\n<TEXT>\n{b15}\n</TEXT>\n</DOC>")
            print(f"Writing file {b18} to {b17}")
        else:
            print(f"File missing at {b7}")
    else:
        print(f"Error fetching data from {b7}")
def fonk4():
    print('This program is obsolete since the website structure has changed')
if b21 = = "__main__":
    fonk4()