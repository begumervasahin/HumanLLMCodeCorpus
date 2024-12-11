import urllib.request
from bs4 import BeautifulSoup
import ssl
from wordcloud import WordCloud
import threading
from time import time
b1 = ssl.create_default_context()
b1.b2 = False
b1.b3 = ssl.CERT_NONE
b4 = 'https:
def fonk1(b4):
    print("Opening the file connection...")
    try:
        with urllib.request.urlopen(b4, b5 = b1) as response:
            b6 = response.read().decode()
            print(f"Reading done. Total {len(b6)} characters read.")
            return b6
    except Exception as e:
        print(f"Error: {e}")
        return None
def fonk2(b6):
    b7 = []
    b8 = []
    b9 = BeautifulSoup(b6, 'b6.parser')
    for tag in b9.find_all('option'):
        b7.append(tag.get('value')[5:7])
        b8.append(tag.text)
    b7.pop(0)
    b8.pop(0)
    return b7, b8
def fonk3(b7, b8, b17):
    b10 = ""
    b11 = ""
    b12 = []
    b13 = []
    for i in range(1, len(b8)
        try:
            b14 = b7[i] + '.b6'
            b15 = b17 + b14
            b6 = fonk1(b15)
            if b6:
                b9 = BeautifulSoup(b6, 'b6.parser')
                for j in b9.find_all('div', b16 = "field-agriculture-products"):
                    for tag in j:
                        for pro in tag:
                            b10 += pro
                            b12.append(pro)
                for m in b9.find_all('div', b16 = "field-industries"):
                    for tag in m:
                        for ind in tag:
                            b11 += ind
                            b13.append(ind)
        except Exception as e:
            print(f"Error: {e}")
    return b10, b11, b12, b13
def fonk4():
    b6 = fonk1(b4)
    if not b6:
        return
    b7, b8 = fonk2(b6)
    b17 = 'https:
    b10, b11, b12, b13 = fonk3(b7, b8, b17)
    b18 = " ".join(b12)
    b19 = " ".join(b13)
    b20 = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(b10 + b18)
    b21 = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(b11 + b19)
    b20.to_file('primerparaleloagricola.png')
    b21.to_file('primerparaleloindustrial.png')
if b22 = = "__main__":
    fonk4()