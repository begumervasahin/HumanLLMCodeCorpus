import requests
import re
import json
from bs4 import BeautifulSoup
from b7 import get_stop_words
from tabulate import tabulate
def fonk1(b11):
    b1 = []
    b2 = requests.get(b11)
    b3 = BeautifulSoup(b2.text, 'lxml')
    for text in b3.find_all('p'):
        if text.text:
            b4 = text.text.lower().split()
            b5 = [fonk2(word) for word in b4 if fonk2(word)]
            b1.extend(b5)
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
    return [item for item in frequency_list if item[0] not in b7]
def fonk5(string_query, b8 = False):
    b9 = "https:
    b10 = "https:
    b11 = b9 + string_query
    try:
        b2 = requests.get(b11)
        b12 = b2.json()
        b13 = b12['b22']['search'][0]['title']
        b14 = b10 + b13
        b1 = fonk1(b14)
        b15 = fonk3(b1)
        b16 = sorted(b15.items(), key=lambda item: item[1], reverse=True)
        if b8:
            b16 = fonk4(b16)
        b17 = sum(count for _, count in b16)
        b18 = b16[:20]
        b19 = [[word, count, round((count * 100) / b17, 4)] for word, count in b18]
        b20 = ['Word', 'Frequency', 'Frequency Percentage']
        print(tabulate(b19, b20 = b20, tablefmt='orgtbl'))
    except requests.exceptions.Timeout:
        print("The server didn't respond. Please, try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")
if b21 = = "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Enter a valid string b22.")
        exit()
    b22 = sys.argv[1]
    b8 = len(sys.argv) > 2
    fonk5(b22, b8)