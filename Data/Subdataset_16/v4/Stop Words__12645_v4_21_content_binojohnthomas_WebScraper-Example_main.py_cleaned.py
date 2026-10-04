import requests
from bs4 import BeautifulSoup
import re
import operator
import json
from tabulate import tabulate
from b7 import get_stop_words
def fonk1(b11):
    b1 = []
    b2 = requests.get(b11)
    b3 = BeautifulSoup(b2.text, 'lxml')
    for text in b3.find_all('p'):
        if text.text:
            b4 = text.text.lower().split()
            for word in b4:
                b5 = fonk2(word)
                if b5:
                    b1.append(b5)
    return b1
def fonk2(word):
    return re.sub('[^A-Za-z]+', '', word)
def fonk3(b1):
    b6 = {}
    for word in b1:
        b6[word] = b6.get(word, 0) + 1
    return b6
def fonk4(frequency_list):
    b7 = set(get_stop_words('en'))
    return [[word, freq] for word, freq in frequency_list if word not in b7]
def fonk5(b24, b8 = False):
    b9 = "https:
    b10 = "https:
    b11 = b9 + b24
    b2 = requests.get(b11)
    b12 = b2.json()
    b13 = b12['b24']['search'][0]['title']
    b14 = b10 + b13
    b15 = fonk1(b14)
    b16 = fonk3(b15)
    b17 = sorted(b16.items(), key=operator.itemgetter(1), reverse=True)
    if b8:
        b17 = fonk4(b17)
    b18 = sum(freq for _, freq in b17)
    b19 = b17[:20]
    b20 = [
        [word, freq, round(freq * 100 / b18, 4)]
        for word, freq in b19
    ]
    b21 = ['Word', 'Frequency', 'Frequency Percentage']
    print(tabulate(b20, b22 = b21, tablefmt='orgtbl'))
if b23 = = "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Enter a valid string")
        sys.exit(1)
    b24 = sys.argv[1]
    b8 = len(sys.argv) > 2
    try:
        fonk5(b24, b8)
    except requests.exceptions.Timeout:
        print("The server didn't respond. Please, try again later.")