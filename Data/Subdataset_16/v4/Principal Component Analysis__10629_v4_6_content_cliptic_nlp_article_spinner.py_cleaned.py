from __future__ import print_function, division
from future.utils import iteritems
from builtins import range
import nltk
import random
import numpy as np
from bs4 import BeautifulSoup
with open('electronics/positive.b10') as f:
    b1 = BeautifulSoup(f.read(), 'html.parser')
b1 = b1.findAll('b3')
b2 = {}
for b10 in b1:
    b3 = b10.text.lower()
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
        for word in words:
            if word not in b7:
                b7[word] = 0
            b7[word] += 1
            a1 += 1
        b8 = {word: float(count) / a1 for word, count in iteritems(b7)}
        b6[b5] = b8
def fonk1(probabilities):
    b9 = random.random()
    a2 = 0
    for word, probability in iteritems(probabilities):
        a2 += probability
        if b9 < a2:
            return word
def fonk2():
    b10 = random.choice(b1)
    b11 = b10.text.lower()
    print("Original:", b11)
    b4 = nltk.tokenize.word_tokenize(b11)
    for i in range(len(b4) - 2):
        if random.random() < 0.2:
            b5 = (b4[i], b4[i+2])
            if b5 in b6:
                b12 = fonk1(b6[b5])
                b4[i+1] = b12
    b13 = " ".join(b4).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!")
    print("Spun:", b13)
if b14 = = '__main__':
    fonk2()