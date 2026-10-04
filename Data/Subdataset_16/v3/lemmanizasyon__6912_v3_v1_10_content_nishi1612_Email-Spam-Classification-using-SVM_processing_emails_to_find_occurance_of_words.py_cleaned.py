import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(b12):
    b1 = pd.read_csv(b12)
    return b1['b4'].tolist()
def fonk2(b12, headers):
    with open(b12, "w") as file:
        file.write(','.join(headers) + ',output\n')
def fonk3(b12, b6, b7, b8):
    b2 = np.zeros(len(b6))
    with open(b12, "r", b3 = 'utf-8', errors='ignore') as file:
        for b4 in file.read().split():
            b4 = b7.lemmatize(b4.lower())
            if b4 in b8 or b4 in string.punctuation or len(b4) <= 2 or b4.isdigit():
                continue
            if b4 in b6:
                b2[b6.index(b4)] += 1
    return b2
def fonk4(b11):
    return "1" if len(b11) == 71 else "-1"
def fonk5(b12, b2, b13):
    with open(b12, "a") as file:
        file.write(','.join(map(str, map(int, b2))) + ',')
        file.write(b13 + '\n')
def fonk6():
    b5 = time()
    b6 = fonk1('wordslist.csv')
    b7 = WordNetLemmatizer()
    b8 = set(stopwords.b6('english'))
    b9 = "emails/"
    b10 = os.fsencode(b9)
    fonk2("frequency.csv", b6)
    a1 = 0
    for file in os.listdir(b10):
        b11 = os.fsdecode(file)
        b12 = os.path.join(b9, b11)
        a1 += 1
        b2 = fonk3(b12, b6, b7, b8)
        b13 = fonk4(b11)
        fonk5("frequency.csv", b2, b13)
        if a1 % b14 = = 0:
            print(f"Processed {a1} files")
    b15 = round(time() - b5, 2)
    print(f"Time (in seconds) to process the entire dataset: {b15}")
if b16 = = "__main__":
    fonk6()