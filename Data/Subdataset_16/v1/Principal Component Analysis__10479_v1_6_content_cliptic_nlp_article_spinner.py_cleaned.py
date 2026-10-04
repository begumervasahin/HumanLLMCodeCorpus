from __future__ import print_function, division
from future.utils import iteritems
from builtins import range
import nltk
import random
import numpy as np
from bs4 import BeautifulSoup
with open('electronics/positive.b10', 'b9', b1 = 'utf-8') as file:
    b2 = BeautifulSoup(file.read(), 'html.parser').findAll('review_text')
b3 = {}
for b10 in b2:
    b4 = b10.text.lower()
    b5 = nltk.tokenize.word_tokenize(b4)
    for i in range(len(b5) - 2):
        b6 = (b5[i], b5[i+2])
        if b6 not in b3:
            b3[b6] = []
        b3[b6].append(b5[i+1])
b7 = {}
for b6, words in iteritems(b3):
    if len(set(words)) > 1:
        b8 = {}
        a1 = 0
        for b11 in words:
            if b11 not in b8:
                b8[b11] = 0
            b8[b11] += 1
            a1 += 1
        for b11, c in iteritems(b8):
            b8[b11] = float(c) / a1
        b7[b6] = b8
def fonk1(b8):
    b9 = random.random()
    a2 = 0
    for b11, p in iteritems(b8):
        a2 += p
        if b9 < a2:
            return b11
def fonk2():
    b10 = random.choice(b2)
    b4 = b10.text.lower()
    print("Original:", b4)
    b5 = nltk.tokenize.word_tokenize(b4)
    for i in range(len(b5) - 2):
        if random.random() < 0.2:
            b6 = (b5[i], b5[i+2])
            if b6 in b7:
                b11 = fonk1(b7[b6])
                b5[i+1] = b11
    print("Spun:")
    print(" ".join(b5).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!"))
if b12 = = '__main__':
    fonk2()