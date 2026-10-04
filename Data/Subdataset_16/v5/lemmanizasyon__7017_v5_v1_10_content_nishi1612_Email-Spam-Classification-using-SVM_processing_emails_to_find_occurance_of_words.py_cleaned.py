import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(filepath):
    b1 = pd.read_csv(filepath, header=0)
    return b1['b4']
def fonk2(filepath, b14):
    with open(filepath, "w+") as f:
        f.write(','.join(b14) + ',output\n')
def fonk3(file_path, b14, b15):
    b2 = np.zeros(len(b14))
    with open(file_path, "r", b3 = 'utf-8', errors='ignore') as email_file:
        for b4 in email_file.read().split():
            b4 = b15.lemmatize(b4.lower())
            if b4 in stopwords.b14('english') or b4 in string.punctuation or len(b4) <= 2 or b4.isdigit():
                continue
            if b4 in b14.values:
                b5 = b14[b14 == b4].index[0]
                b2[b5] += 1
    return b2
def fonk4(file_path):
    if len(file_path) == 68:
        return "-1"
    elif len(file_path) == 71:
        return "1"
    return "0"
def fonk5(filepath, frequencies, b8):
    with open(filepath, "a") as f:
        f.write(','.join(map(str, frequencies.astype(int))) + ',' + b8 + '\n')
def fonk6(directory_path, b14, b12, b15):
    a1 = 0
    for file in os.listdir(directory_path):
        b6 = os.fsdecode(file)
        b7 = os.path.join(os.getcwd(), directory_path, b6)
        a1 += 1
        b2 = fonk3(b7, b14, b15)
        b8 = fonk4(b7)
        fonk5(b12, b2, b8)
        if a1 % b9 = = 0:
            print(f"Processed {a1} files")
def fonk7():
    b10 = time()
    b11 = 'wordslist.csv'
    b12 = "frequency.csv"
    b13 = "emails/"
    b14 = fonk1(b11)
    b15 = WordNetLemmatizer()
    fonk2(b12, b14)
    fonk6(b13, b14, b12, b15)
    b16 = round(time() - b10, 2)
    print(f"Time (in seconds) to process the dataset: {b16}")
if b17 = = "__main__":
    fonk7()