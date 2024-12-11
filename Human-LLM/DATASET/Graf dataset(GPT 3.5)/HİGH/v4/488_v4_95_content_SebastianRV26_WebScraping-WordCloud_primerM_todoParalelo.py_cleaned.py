import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
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
print("Opening the file connection...")
b5 = urllib.request.urlopen(b4, context=b1)
print("HTTP status", b5.getcode())
b6 = b5.read().decode()
print(f"Reading done. Total {len(b6)} characters read.")
b7 = BeautifulSoup(b6, 'b6.parser')
b8 = []
b9 = []
for tag in b7.find_all('option'):
    b8.append(tag.get('value')[5:7])
    b9.append(tag.text)
b10 = b8.pop(0)
b10 = b9.pop(0)
b11 = 'https:
b12 = ""
b13 = ""
b14 = ""
b15 = ""
b16 = []
b17 = []
def fonk1():
    print("\nIniciando Paralelo\n")
    global b12
    global b13
    for b22 in range(1, len(b9)
        try:
            b18 = b8[b22] + '.b6'
            b19 = b11 + b18
            b6 = urllib.request.urlopen(b19, context=b1).read()
            b7 = BeautifulSoup(b6, 'b6.parser')
            for j in b7.find_all('div', b20 = "field-agriculture-products"):
                for tag in j:
                    for pro in tag:
                        b12 += pro
                        b16.append(pro)
            for m in b7.find_all('div', b20 = "field-industries"):
                for tag in m:
                    for ind in tag:
                        b13 += ind
                        b17.append(ind)
        except:
            pass
def fonk2():
    global b14
    global b15
    b21 = time()
    for b22 in range(len(b9)
        try:
            b18 = b8[b22] + '.b6'
            b19 = b11 + b18
            b6 = urllib.request.urlopen(b19, context=b1).read()
            b7 = BeautifulSoup(b6, 'b6.parser')
            for j in b7.find_all('div', b20 = "field-agriculture-products"):
                for tag in j:
                    for pro in tag:
                        b14 += pro
            for m in b7.find_all('div', b20 = "field-industries"):
                for tag in m:
                    for ind in tag:
                        b15 += ind
        except:
            pass
        if b22 = = 266:
            b23 = time()
            b24 = b23 - b21
            print("\nEl tiempo de ejecucion del paralelo 2 fue :", b24)
            b12 = " ".join(b16)
            b13 = " ".join(b17)
            b25 = b14 + b12
            b26 = b13 + b15
            b27 = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(b25)
            b27.to_file('primerparaleloagricola.png')
            b28 = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(b26)
            b28.to_file('primerparaleloindustrial.png')
threading.Thread(b29 = paralelo1).start()
threading.Thread(b29 = paralelo2).start()