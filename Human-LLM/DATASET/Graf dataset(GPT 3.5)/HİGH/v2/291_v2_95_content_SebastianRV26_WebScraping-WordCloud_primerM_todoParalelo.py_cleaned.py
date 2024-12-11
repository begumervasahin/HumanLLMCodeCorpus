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
b1 = []
b2 = []
b3 = ssl.create_default_context()
b3.b4 = False
b3.b5 = ssl.CERT_NONE
b6 = 'https:
b7 = 'https:
b8 = []
b9 = []
def fonk1():
    print("\nIniciando Paralelo 1\n")
    for b18 in range(1, len(b27)
        try:
            b10 = b26[b18] + '.b12'
            b11 = b7 + b10
            b12 = urllib.request.urlopen(b11, context=b3).read()
            b13 = BeautifulSoup(b12, 'b12.parser')
            b14 = b13.get_text()
            b15 = b14.find('Agriculture - products:')
            if b15 != -1:
                print(b18)
                for j in b13.find_all('div', b16 = "field-agriculture-products"):
                    for tag in j:
                        for pro in tag:
                            b1.append(pro)
            for m in b13.find_all('div', b16 = "field-industries"):
                for tag in m:
                    for ind in tag:
                        b2.append(ind)
        except Exception as e:
            print("Error:", e)
def fonk2():
    print("\nIniciando Paralelo 2\n")
    b17 = time()
    for b18 in range(len(b27)
        try:
            b10 = b26[b18] + '.b12'
            b11 = b7 + b10
            b12 = urllib.request.urlopen(b11, context=b3).read()
            b13 = BeautifulSoup(b12, 'b12.parser')
            b14 = b13.get_text()
            b15 = b14.find('Agriculture - products:')
            if b15 != -1:
                print(b18)
                for j in b13.find_all('div', b16 = "field-agriculture-products"):
                    for tag in j:
                        for pro in tag:
                            b1.append(pro)
            for m in b13.find_all('div', b16 = "field-industries"):
                for tag in m:
                    for ind in tag:
                        b2.append(ind)
        except Exception as e:
            print("Error:", e)
        if b18 = = 266:
            b19 = time()
            b20 = b19 - b17
            print ("\nEl tiempo de ejecucion del paralelo 2 fue:", b20)
            b21 = " ".join(b1)
            b22 = " ".join(b2)
            b23 = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(b21)
            b23.to_file('primerparaleloagricola.png')
            b24 = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(b22)
            b24.to_file('primerparaleloindustrial.png')
print("Opening the file connection...")
b25 = urllib.request.urlopen(b6, context=b3)
print("HTTP status", b25.getcode())
b12 = b25.read().decode()
print(f"Reading done. Total {len(b12)} characters read.")
b13 = BeautifulSoup(b12, 'b12.parser')
b26 = [tag.get('value')[5:7] for tag in b13.find_all('option')]
b27 = [tag.text for tag in b13.find_all('option')]
b26.pop(0)
b27.pop(0)
threading.Thread(b28 = paralelo1).start()
threading.Thread(b28 = paralelo2).start()