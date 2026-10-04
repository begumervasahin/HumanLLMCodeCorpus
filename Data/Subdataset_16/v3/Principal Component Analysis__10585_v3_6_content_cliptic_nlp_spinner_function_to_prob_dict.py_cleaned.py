import nltk
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
b1 = RegexpTokenizer(r'\w+')
def fonk1(html_txt_link):
    with open(html_txt_link, 'r') as file:
        b2 = BeautifulSoup(file.read(), features="html.parser")
    b3 = []
    for review in b2.find_all('b4'):
        b4 = review.get_text().lower()
        b5 = b1.tokenize(b4)
        b3.append(b5)
    return b3
def fonk2(b3):
    b6 = {}
    b7 = {}
    for tokens in b3:
        for idx, token in enumerate(tokens):
            if 0 < idx < len(tokens) - 1:
                if token not in b6:
                    b6[token] = [[tokens[idx - 1], tokens[idx + 1]]]
                    b7[token] = 1
                else:
                    b6[token].append([tokens[idx - 1], tokens[idx + 1]])
                    b7[token] += 1
    return b6, b7
def fonk3(b6):
    b8 = {}
    b9 = {}
    for token, pairs in b6.items():
        for pair in pairs:
            pair.sort()
            b10 = tuple(pair)
            if b10 not in b8:
                b8[b10] = {token: 1}
                b9[b10] = 1
            else:
                if token not in b8[b10]:
                    b8[b10][token] = 1
                else:
                    b8[b10][token] += 1
                b9[b10] += 1
    for b10, token_counts in b8.items():
        for token in token_counts:
            token_counts[token] /= b9[b10]
    return b8
def fonk4(html_txt_link):
    b3 = fonk1(html_txt_link)
    b6, b11 = fonk2(b3)
    b8 = fonk3(b6)
    return b8
b12 = fonk4('electronics/positive.review')
print(b12[('i', 'this')]['bought'])