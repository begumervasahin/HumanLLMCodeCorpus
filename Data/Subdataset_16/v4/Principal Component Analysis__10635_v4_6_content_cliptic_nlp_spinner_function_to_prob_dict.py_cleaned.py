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
        for index, token in enumerate(tokens):
            if 0 < index < len(tokens) - 1:
                b8 = tokens[index - 1]
                b9 = tokens[index + 1]
                if token not in b6:
                    b6[token] = [[b8, b9]]
                    b7[token] = 1
                else:
                    b6[token].append([b8, b9])
                    b7[token] += 1
    b10 = {}
    b11 = {}
    for key, value_list in b6.items():
        for value in value_list:
            value.sort()
            b12 = tuple(value)
            if b12 not in b10:
                b10[b12] = {key: 1}
                b11[b12] = 1
            else:
                if key not in b10[b12]:
                    b10[b12][key] = 1
                else:
                    b10[b12][key] += 1
                b11[b12] += 1
    for b12, word_dict in b10.items():
        for word in word_dict:
            word_dict[word] = word_dict[word] / b11[b12]
    return b10
b13 = fonk1('electronics/positive.review')
print(b13[('i', 'this')]['bought'])