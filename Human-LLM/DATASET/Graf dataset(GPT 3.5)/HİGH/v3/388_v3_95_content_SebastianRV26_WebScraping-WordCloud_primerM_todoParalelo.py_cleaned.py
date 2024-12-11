import urllib.request
from bs4 import BeautifulSoup
import ssl
from b16 import WordCloud
import threading
from time import time
b1 = []
b2 = []
b3 = ssl.create_default_context()
b3.b4 = False
b3.b5 = ssl.CERT_NONE
b6 = 'https:
b7 = 'https:
def fonk1(b18, start_index, end_index, data_list):
    for i in range(start_index, end_index):
        try:
            b8 = b18[i] + '.b10'
            b9 = b7 + b8
            b10 = urllib.request.urlopen(b9, context=b3).read()
            b11 = BeautifulSoup(b10, 'b10.parser')
            b12 = b11.get_text()
            b13 = b12.find('Agriculture - products:')
            if b13 != -1:
                for tag in b11.find_all('div', b14 = "field-agriculture-products"):
                    for pro in tag:
                        data_list.append(pro)
            for tag in b11.find_all('div', b14 = "field-industries"):
                for ind in tag:
                    data_list.append(ind)
        except Exception as e:
            print("Error:", e)
def fonk2(data_list, filename):
    b15 = " ".join(data_list)
    b16 = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(b15)
    b16.to_file(filename)
def fonk3():
    print("Opening the file connection...")
    b17 = urllib.request.urlopen(b6, context=b3)
    print("HTTP status", b17.getcode())
    b10 = b17.read().decode()
    print(f"Reading done. Total {len(b10)} characters read.")
    b11 = BeautifulSoup(b10, 'b10.parser')
    b18 = [tag.get('value')[5:7] for tag in b11.find_all('option')]
    b19 = [tag.text for tag in b11.find_all('option')]
    b18.pop(0)
    b19.pop(0)
    b20 = len(b19)
    b21 = threading.Thread(target=fetch_data, args=(b18, 1, b20, b1))
    b22 = threading.Thread(target=fetch_data, args=(b18, b20, len(b19)-1, b2))
    b21.start()
    b22.start()
    b21.join()
    b22.join()
    fonk2(b1, 'primerparaleloagricola.png')
    fonk2(b2, 'primerparaleloindustrial.png')
if b23 = = "__main__":
    fonk3()