import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(b14):
    b1 = pd.read_csv(b14, header=0)
    return b1['b5'], set(b1['b5'])
def fonk2(b16, words):
    with open(b16, "w") as f:
        f.write(','.join(words) + ',output\n')
def fonk3(b11, words, b9, b10):
    b2 = np.zeros(len(words))
    with open(b11, "r", b3 = 'utf-8', errors='ignore') as file:
        b4 = file.read().split()
        for b5 in b4:
            b5 = b10.lemmatize(b5.lower())
            if b5 in stopwords.words('english') or b5 in string.punctuation or len(b5) <= 2 or b5.isdigit():
                continue
            if b5 in b9:
                b6 = words.get_loc(b5)
                b2[b6] += 1
    return b2
def fonk4(b16, b2, b7):
    with open(b16, "a") as f:
        f.write(','.join(map(str, map(int, b2))) + ',')
        if b7 = = 68:
            f.write("-1")
        elif b7 = = 71:
            f.write("1")
        f.write('\n')
def fonk5(b14, b15, b16):
    b8 = time()
    words, b9 = fonk1(b14)
    b10 = WordNetLemmatizer()
    fonk2(b16, words)
    a1 = 0
    for file in os.listdir(os.fsencode(b15)):
        b11 = os.path.join(b15, file.decode("utf-8"))
        a1 += 1
        b2 = fonk3(b11, words, b9, b10)
        fonk4(b16, b2, len(b11))
        if a1 % b12 = = 0:
            print(f"Processed {a1} files")
    b13 = round(time() - b8, 2)
    print(f"Time (in seconds) to process all emails: {b13}")
b14 = 'wordslist.csv'
b15 = 'emails/'
b16 = 'frequency.csv'
fonk5(b14, b15, b16)