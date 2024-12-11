import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import threading
from time import time
b1 = []
b2 = []
b3 = ssl.create_default_context()
b3.b4 = False
b3.b5 = ssl.CERT_NONE
b6 = 'https:
print("Opening the file connection...")
b7 = urllib.request.urlopen(b6, context=b3)
print("HTTP status",b7.getcode())
b8 = b7.read().decode()
print(f"Reading done. Total {len(b8)} characters read.")
b9 = BeautifulSoup(b8, 'b8.parser')
b10 = []
b11 = []
for tag in b9.find_all('option'):
    b10.append(tag.get('value')[5:7])
    b11.append(tag.text)
b12 = b10.pop(0)
b12 = b11.pop(0)
b13 = 'https:
global b16
global b17
global b23
global b24
global b14
global b15
b14 = []
b15 = []
global tiempo_ejecucion_p1
def fonk1():
    print("\nIniciando Paralelo\n")
    b16 = ""
    b17 = ""
    for b26 in range(1,len(b11)
        try:
            b18 = b10[b26]+'.b8'
            b19 = b13+b18
            b8 = urllib.request.urlopen(b19, context=b3).read()
            b9 = BeautifulSoup(b8, 'b8.parser')
            b20 = b9.get_text()
            b21 = b20.find('Agriculture - products:')
            if b21!=-1:
                    print(b26)
                    for j in b9.find_all('div',b22 = "field-agriculture-products"):
                        for tag in j:
                            for pro in tag:
                                b16 = b16+pro
                                b14.append(pro)
            for m in b9.find_all('div',b22 = "field-industries"):
                for tag in m:
                    for ind in tag:
                        b17 = b17+ind
                        b15.append(ind)
        except:
            pass
def fonk2():
    b23 = ""
    b24 = ""
    b25 = time()
    for b26 in range(len(b11)
        try:
            b18 = b10[b26]+'.b8'
            b19 = b13+b18
            b8 = urllib.request.urlopen(b19, context=b3).read()
            b9 = BeautifulSoup(b8, 'b8.parser')
            b20 = b9.get_text()
            b21 = b20.find('Agriculture - products:')
            if b21!=-1:
                    print(b26)
                    for j in b9.find_all('div',b22 = "field-agriculture-products"):
                        for tag in j:
                            for pro in tag:
                                b23 = b23+pro
            for m in b9.find_all('div',b22 = "field-industries"):
                for tag in m:
                    for ind in tag:
                        b24 = b24+ind
        except:
            pass
        if b26 = = 266:
            b27 = time()
            b28 = b27 - b25
            print ("\nEl tiempo de ejecucion del paralelo 2 fue :",b28)
            b16 = " ".join(b14)
            b17 = " ".join(b15)
            b29 = b23 + b16
            b30 = b17 + b24
            b31 = WordCloud(width = 800, height = 800,
                      b32 = 'white',
                                  b33 = 10).generate(b29)
            b31.to_file('primerparaleloagricola.png')
            b34 = WordCloud(width = 800, height = 800,
                                  b32 = 'white',
                                  b33 = 10).generate(b30)
            b34.to_file('primerparaleloindustrial.png')
threading.Thread(b35 = paralelo1).start()
threading.Thread(b35 = paralelo2).start()