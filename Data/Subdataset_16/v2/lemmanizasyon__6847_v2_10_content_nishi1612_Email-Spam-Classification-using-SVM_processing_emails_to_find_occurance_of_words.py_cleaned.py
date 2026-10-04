import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(b15, b16, b17):
    b1 = time()
    b2 = pd.read_csv(b15, header=0)
    b3 = b2['b11']
    b4 = set(b3)
    b5 = WordNetLemmatizer()
    with open(b17, "w") as f:
        f.write(','.join(b3) + ',output\n')
    b6 = os.fsencode(b16)
    a1 = 0
    for file in os.listdir(b6):
        b7 = os.path.join(b16, file.decode("utf-8"))
        a1 += 1
        with open(b7, "r", b8 = 'utf-8', errors='ignore') as file:
            b9 = np.zeros(len(b3))
            b10 = file.read().split()
            for b11 in b10:
                b11 = b5.lemmatize(b11.lower())
                if b11 in stopwords.b3('english') or b11 in string.punctuation or len(b11) <= 2 or b11.isdigit():
                    continue
                if b11 in b4:
                    b12 = b3.get_loc(b11)
                    b9[b12] += 1
        with open(b17, "a") as f:
            f.write(','.join(map(str, map(int, b9))) + ',')
            if len(b7) == 68:
                f.write("-1")
            elif len(b7) == 71:
                f.write("1")
            f.write('\n')
        if a1 % b13 = = 0:
            print(f"Processed {a1} files")
    b14 = round(time() - b1, 2)
    print(f"Time (in seconds) to process all emails: {b14}")
b15 = 'wordslist.csv'
b16 = 'emails/'
b17 = 'frequency.csv'
fonk1(b15, b16, b17)