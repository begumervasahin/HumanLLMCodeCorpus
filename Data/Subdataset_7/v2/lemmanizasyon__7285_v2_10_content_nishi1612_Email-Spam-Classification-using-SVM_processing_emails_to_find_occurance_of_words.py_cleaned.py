import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(filename):
    b1 = pd.read_csv(filename, header=0)
    return b1['b2']
def fonk2(b2, lemmatizer, b10):
    b2 = lemmatizer.lemmatize(b2.lower())
    return b2 if b2 not in b10 and b2 not in string.punctuation and len(b2) > 2 and not b2.isdigit() else None
def fonk3(file_path, b8, lemmatizer, b10):
    b3 = np.zeros(len(b8))
    with open(file_path, "r", b4 = 'utf-8', errors='ignore') as file_reading:
        for b2 in file_reading.read().split():
            b5 = fonk2(b2, lemmatizer, b10)
            if b5:
                for i, b6 in enumerate(b8):
                    if b6 = = b5:
                        b3[i] += 1
                        break
    return b3
def fonk4(filename, b8):
    with open(filename, "b6+") as f:
        f.write(','.join(map(str, b8)) + ',output\n')
def fonk5():
    b7 = time()
    b8 = fonk1('wordslist.csv')
    b9 = WordNetLemmatizer()
    b10 = set(stopwords.b8('english'))
    fonk4("frequency.csv", b8)
    b11 = os.fsencode("emails/")
    a1 = 0
    for b12 in os.listdir(b11):
        b12 = b12.decode("utf-8")
        b13 = str(os.getcwd()) + '/emails/' + ''.join(c for c in b12 if c not in {'b', "'"})
        a1 += 1
        b3 = fonk3(b13, b8, b9, b10)
        with open("frequency.csv", "a") as f:
            f.write(','.join(map(str, b3)))
            f.write("-1" if len(b13) == 68 else "1")
            f.write('\n')
        if a1 % b14 = = 0:
            print("Done " + str(a1))
    print("Time (in seconds) to segregate the entire dataset to form the input vector: " + str(round(time() - b7, 2)))
if b15 = = "__main__":
    fonk5()