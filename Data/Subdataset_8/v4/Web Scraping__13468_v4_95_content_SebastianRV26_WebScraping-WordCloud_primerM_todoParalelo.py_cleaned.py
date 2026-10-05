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
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'https:
print("Opening the file connection...")
uh = urllib.request.urlopen(url, context=ctx)
print("HTTP status", uh.getcode())
html = uh.read().decode()
print(f"Reading done. Total {len(html)} characters read.")
soup = BeautifulSoup(html, 'html.parser')
country_codes = []
country_names = []
for tag in soup.find_all('option'):
    country_codes.append(tag.get('value')[5:7])
    country_names.append(tag.text)
temp = country_codes.pop(0)
temp = country_names.pop(0)
urlbase = 'https:
productos_Agricolas = ""
productos_Industriales = ""
productos_Agricolas2 = ""
productos_Industriales2 = ""
listAgricola = []
lisIndustrial = []
def paralelo1():
    print("\nIniciando Paralelo\n")
    global productos_Agricolas
    global productos_Industriales
    for i in range(1, len(country_names)
        try:
            country_html = country_codes[i] + '.html'
            url_to_get = urlbase + country_html
            html = urllib.request.urlopen(url_to_get, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            for j in soup.find_all('div', id="field-agriculture-products"):
                for tag in j:
                    for pro in tag:
                        productos_Agricolas += pro
                        listAgricola.append(pro)
            for m in soup.find_all('div', id="field-industries"):
                for tag in m:
                    for ind in tag:
                        productos_Industriales += ind
                        lisIndustrial.append(ind)
        except:
            pass
def paralelo2():
    global productos_Agricolas2
    global productos_Industriales2
    tiempo_inicial = time()
    for i in range(len(country_names)
        try:
            country_html = country_codes[i] + '.html'
            url_to_get = urlbase + country_html
            html = urllib.request.urlopen(url_to_get, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            for j in soup.find_all('div', id="field-agriculture-products"):
                for tag in j:
                    for pro in tag:
                        productos_Agricolas2 += pro
            for m in soup.find_all('div', id="field-industries"):
                for tag in m:
                    for ind in tag:
                        productos_Industriales2 += ind
        except:
            pass
        if i == 266:
            tiempo_final = time()
            tiempo_ejecucion = tiempo_final - tiempo_inicial
            print("\nEl tiempo de ejecucion del paralelo 2 fue :", tiempo_ejecucion)
            productos_Agricolas = " ".join(listAgricola)
            productos_Industriales = " ".join(lisIndustrial)
            A = productos_Agricolas2 + productos_Agricolas
            I = productos_Industriales + productos_Industriales2
            agricultural_wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(A)
            agricultural_wordcloud.to_file('primerparaleloagricola.png')
            industrial_wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(I)
            industrial_wordcloud.to_file('primerparaleloindustrial.png')
threading.Thread(target=paralelo1).start()
threading.Thread(target=paralelo2).start()