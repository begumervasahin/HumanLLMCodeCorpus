import nltk
import random
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
b1 = BeautifulSoup(open('electronics/positive.b9').read())
b1 = b1.findAll("review_text")
b2 = {}
for b9 in b1:
    b3 = b9.b3.lower()
    b4 = nltk.tokenize.word_tokenize(b3)
    for i in range(len(b4) - 2):
        b5 = (b4[i], b4[i + 2])
        if b5 not in b2:
            b2[b5] = []
        b2[b5].append(b4[i + 1])
b6 = {}
for b5, words in b2.items():
    if len(set(words)) > 1:
        b7 = {}
        a1 = 0
        for word in words:
            if word not in b7:
                b7[word] = 0
            b7[word] += 1
            a1 += 1
        for word, count in b7.items():
            b7[word] = count / a1
        b6[b5] = b7
def fonk1(word_probabilities):
    b8 = random.random()
    a2 = 0
    for word, prob in word_probabilities.items():
        a2 += prob
        if b8 < a2:
            return word
def fonk2():
    b9 = random.choice(b1).b3.lower()
    print('Original b3: \n', b9)
    b4 = nltk.tokenize.word_tokenize(b9)
    for i in range(len(b4) - 2):
        if random.random() < 0.2:
            b5 = (b4[i], b4[i + 2])
            if b5 in b6:
                b10 = fonk1(b6[b5])
                b4[i + 1] = b10
    b11 = ' '.join(b4)
    b11 = b11.replace(" :", ":").replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?").replace("  ' ", "'")
    print("Spun: \n")
    print(b11)
fonk2()