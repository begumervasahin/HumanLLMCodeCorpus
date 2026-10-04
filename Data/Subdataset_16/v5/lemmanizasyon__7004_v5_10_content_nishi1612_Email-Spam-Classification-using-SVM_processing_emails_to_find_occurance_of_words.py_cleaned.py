import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(b14):
    b1 = pd.read_csv(b14)
    return b1['b4']
def fonk2(output_path, b5):
    with open(output_path, "w") as f:
        f.write(','.join(b5) + ',output\n')
def fonk3(b14, b5, b11, b12):
    b2 = np.zeros(b5.size)
    with open(b14, "r", b3 = 'utf-8', errors='ignore') as file:
        for b4 in file.read().split():
            b4 = b11.lemmatize(b4.lower())
            if b4 in b12 or b4 in string.punctuation or len(b4) <= 2 or b4.isdigit():
                continue
            if b4 in b5.values:
                b2[b5[b5 = = b4].index[0]] += 1
    return b2
def fonk4(output_path, b2, b13):
    with open(output_path, "a") as f:
        f.write(','.join(map(str, map(int, b2))) + ',')
        b6 = "-1" if len(b13) == 68 else "1"
        f.write(b6 + '\n')
def fonk5():
    b7 = time()
    b8 = 'wordslist.csv'
    b9 = "emails/"
    b10 = "frequency.csv"
    b5 = fonk1(b8)
    b11 = WordNetLemmatizer()
    b12 = set(stopwords.b5('english'))
    fonk2(b10, b5)
    a1 = 0
    for file in os.listdir(os.fsencode(b9)):
        b13 = os.fsdecode(file)
        b14 = os.path.join(b9, b13)
        b2 = fonk3(b14, b5, b11, b12)
        fonk4(b10, b2, b13)
        a1 += 1
        if a1 % b15 = = 0:
            print(f"Processed {a1} files")
    print(f"Time (in seconds) to process dataset: {round(time() - b7, 2)}")
if b16 = = "__main__":
    fonk5()