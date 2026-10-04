from __future__ import print_function, division
from future.utils import iteritems
from builtins import range
import nltk
import random
import numpy as np
from bs4 import BeautifulSoup
def fonk1(file_path):
    with open(file_path) as f:
        return BeautifulSoup(f.read(), 'html.parser').findAll('b2')
def fonk2(b14):
    b1 = {}
    for b10 in b14:
        b2 = b10.text.lower()
        b3 = nltk.tokenize.word_tokenize(b2)
        for i in range(len(b3) - 2):
            b4 = (b3[i], b3[i + 2])
            if b4 not in b1:
                b1[b4] = []
            b1[b4].append(b3[i + 1])
    return b1
def fonk3(b1):
    b5 = {}
    for b4, words in iteritems(b1):
        if len(set(words)) > 1:
            b6 = {}
            a1 = 0
            for word in words:
                b6[word] = b6.get(word, 0) + 1
                a1 += 1
            b7 = {word: float(count) / a1 for word, count in iteritems(b6)}
            b5[b4] = b7
    return b5
def fonk4(probabilities):
    b8 = random.random()
    a2 = 0
    for word, probability in iteritems(probabilities):
        a2 += probability
        if b8 < a2:
            return word
def fonk5(b10, b5, b9 = 0.2):
    b3 = nltk.tokenize.word_tokenize(b10.text.lower())
    for i in range(len(b3) - 2):
        if random.random() < b9:
            b4 = (b3[i], b3[i + 2])
            if b4 in b5:
                b3[i + 1] = fonk4(b5[b4])
    return " ".join(b3).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!")
def fonk6(b14, b5):
    b10 = random.choice(b14)
    b11 = b10.text.lower()
    print("Original:", b11)
    b12 = fonk5(b10, b5)
    print("Spun:", b12)
if b13 = = '__main__':
    b14 = fonk1('electronics/positive.b10')
    b1 = fonk2(b14)
    b5 = fonk3(b1)
    fonk6(b14, b5)