from __future__ import print_function, division
from future.utils import iteritems
from builtins import range
import nltk
import random
import numpy as np
from bs4 import BeautifulSoup
b1 = BeautifulSoup(open('electronics/positive.b9').read())
b1 = b1.findAll('review_text')
b2 = {}
for b9 in b1:
    b3 = b9.text.lower()
    b4 = nltk.tokenize.word_tokenize(b3)
    for i in range(len(b4) - 2):
        b5 = (b4[i], b4[i+2])
        if b5 not in b2:
            b2[b5] = []
        b2[b5].append(b4[i+1])
b6 = {}
for b5, words in iteritems(b2):
    if len(set(words)) > 1:
        b7 = {}
        a1 = 0
        for b10 in words:
            if b10 not in b7:
                b7[b10] = 0
            b7[b10] += 1
            a1 += 1
        for b10, c in iteritems(b7):
            b7[b10] = float(c) / a1
        b6[b5] = b7
def fonk1(b7):
    b8 = random.random()
    a2 = 0
    for b10, p in iteritems(b7):
        a2 += p
        if b8 < a2:
            return b10
def fonk2():
    b9 = random.choice(b1)
    b3 = b9.text.lower()
    print("Original:", b3)
    b4 = nltk.tokenize.word_tokenize(b3)
    for i in range(len(b4) - 2):
        if random.random() < 0.2:
            b5 = (b4[i], b4[i+2])
            if b5 in b6:
                b10 = fonk1(b6[b5])
                b4[i+1] = b10
    print("Spun:")
    print(" ".join(b4).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!"))
if b11 = = '__main__':
    fonk2()