import requests
from bs4 import BeautifulSoup
import re
import operator
import json
from tabulate import tabulate
from b7 import get_stop_words
def fonk1(url):
    b1 = []
    b2 = requests.get(url)
    b3 = BeautifulSoup(b2.text, 'lxml')
    for paragraph in b3.find_all('p'):
        if paragraph.text:
            b4 = paragraph.text.lower().split()
            for word in b4:
                b5 = fonk2(word)
                if b5:
                    b1.append(b5)
    return b1
def fonk2(word):
    return re.sub('[^a-z]+', '', word)
def fonk3(b1):
    b6 = {}
    for word in b1:
        b6[word] = b6.get(word, 0) + 1
    return b6
def fonk4(frequency_list):
    b7 = set(get_stop_words('en'))
    return [[word, freq] for word, freq in frequency_list if word not in b7]
def fonk5(b21):
    b8 = "https:
    b9 = "https:
    b2 = requests.get(b8 + b21)
    b10 = b2.json()
    b11 = b10['b21']['search'][0]['title']
    return b9 + b11
def fonk6(word_frequencies):
    b12 = sum(freq for _, freq in word_frequencies)
    b13 = word_frequencies[:20]
    b14 = [
        [word, freq, round(freq * 100 / b12, 4)]
        for word, freq in b13
    ]
    b15 = ['Word', 'Frequency', 'Frequency Percentage']
    print(tabulate(b14, b16 = b15, tablefmt='orgtbl'))
def fonk7(b21, b17 = False):
    try:
        b18 = fonk5(b21)
        b1 = fonk1(b18)
        b6 = fonk3(b1)
        b19 = sorted(b6.items(), key=operator.itemgetter(1), reverse=True)
        if b17:
            b19 = fonk4(b19)
        fonk6(b19)
    except requests.exceptions.Timeout:
        print("The server didn't respond. Please, try again later.")
if b20 = = "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Enter a valid string")
        sys.exit(1)
    b21 = sys.argv[1]
    b17 = len(sys.argv) > 2
    fonk7(b21, b17)