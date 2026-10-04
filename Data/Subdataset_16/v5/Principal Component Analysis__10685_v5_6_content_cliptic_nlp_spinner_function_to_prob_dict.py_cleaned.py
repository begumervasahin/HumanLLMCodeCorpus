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
    for review in b2.find_all('review_text'):
        b4 = review.get_text().lower()
        b5 = b1.tokenize(b4)
        b3.append(b5)
    b6 = {}
    b7 = {}
    for tokens in b3:
        for index in range(1, len(tokens) - 1):
            b8 = tokens[index - 1]
            b9 = tokens[index]
            b10 = tokens[index + 1]
            if b9 not in b6:
                b6[b9] = [[b8, b10]]
                b7[b9] = 1
            else:
                b6[b9].append([b8, b10])
                b7[b9] += 1
    b11 = {}
    b12 = {}
    for b9, neighbors_list in b6.items():
        for neighbors in neighbors_list:
            neighbors.sort()
            b13 = tuple(neighbors)
            if b13 not in b11:
                b11[b13] = {b9: 1}
                b12[b13] = 1
            else:
                if b9 not in b11[b13]:
                    b11[b13][b9] = 1
                else:
                    b11[b13][b9] += 1
                b12[b13] += 1
    for b13, word_dict in b11.items():
        for word in word_dict:
            word_dict[word] = word_dict[word] / b12[b13]
    return b11
b14 = fonk1('electronics/positive.review')
print(b14[('i', 'this')]['bought'])