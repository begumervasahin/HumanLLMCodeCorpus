from bs4 import BeautifulSoup
import requests
import re
import operator
import json
from tabulate import tabulate
import sys
from b9 import get_stop_words
def fonk1(b15):
    b1 = []
    b2 = requests.get(b15)
    b3 = b2.text
    b4 = BeautifulSoup(b3,'lxml')
    for text in b4.findAll('p'):
        if text.text is None:
            continue
        b5 = text.text
        b6 = b5.lower().split()
        for word in b6:
            b7 = fonk2(word)
            if len(b7) > 0:
                b1.append(b7)
    return b1
def fonk2(word):
    b7 = re.sub('[^A-Za-z]+', '', word)
    return b7
def fonk3(b1):
    b8 = {}
    for word in b1:
        if word in b8:
            b8[word] += 1
        else:
            b8[word] = 1
    return b8
def fonk4(frequency_list):
    b9 = get_stop_words('en')
    b10 = []
    for key,value in frequency_list:
        if key not in b9:
            b10.append([key, value])
    return b10
b11 = "https:
b12 = "https:
if(len(sys.argv) < 2):
    print("Enter valid string")
    exit()
b13 = sys.argv[1]
if(len(sys.argv) > 2):
    b14 = True
else:
    b14 = False
b15 = b11 + b13
try:
    b16 = requests.get(b15)
    b17 = json.loads(b16.b5.decode("utf-8"))
    b18 = b17['query']['search'][0]['title']
    b15 = b12 + b18
    b19 = fonk1(b15)
    b20 = fonk3(b19)
    b21 = sorted(b20.items(), key=operator.itemgetter(1), reverse=True)
    if(b14):
        b21 = fonk4(b21)
    a1 = 0
    for key,value in b21:
        a1 = a1 + value
    if len(b21) > 20:
        b21 = b21[:20]
    b22 = []
    for key,value in b21:
        b23 = float(value * 100) / a1
        b22.append([key, value, round(b23, 4)])
    b24 = ['Word', 'Frequency', 'Frequency Percentage']
    print(tabulate(b22, b25 = b24, tablefmt='orgtbl'))
except requests.exceptions.Timeout:
    print("The server didn't respond. Please, try again later.")