import nltk
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import csv
from nltk.tokenize import RegexpTokenizer
b1 = RegexpTokenizer(r'\w+')
def fonk1(html_txt_link):
    b2 = BeautifulSoup(open(html_txt_link).read(), features="html.parser")
    b3 = []
    for i in b2.find_all('review_text'):
        b4 = i.get_text()
        b4 = b4.lower()
        b5 = b1.tokenize(b4)
        b3.append(b5)
    b6 = {}
    b7 = {}
    for i in b3:
        a1 = 0
        for n in i:
            if a1 != 0 and a1 != (len(i)-1):
                if n not in b6:
                    b6[i[a1]] = [[i[a1-1], i[a1+1]]]
                    b7[i[a1]] = 1
                else:
                    b6[i[a1]].append([i[a1-1], i[a1+1]])
                    b7[i[a1]] += 1
            a1 += 1
    b8 = {}
    b9 = {}
    for key in b6.keys():
        for b10 in b6[key]:
            b10.sort()
            b10 = tuple(b10)
            if b10 not in b8:
                b8[b10] = {key: 1}
                b9[b10] = 1
            else:
                if key not in b8[b10].keys():
                    b8[b10][key] = 1
                else:
                    b8[b10][key] += 1
                b9[b10] += 1
    for key in b8.keys():
        for b10 in b8[key]:
            b8[key][b10] = b8[key][b10] / b9[key]
    return b8
b11 = fonk1('electronics/positive.review')
print(b11[('i', 'this')]['bought'])