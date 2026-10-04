import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(b13, b14, b15):
    b1 = time()
    b2 = pd.read_csv(b13, header=0)
    b3 = b2['b10']
    b4 = set(b3)
    b5 = WordNetLemmatizer()
    with open(b15, "w+") as f:
        for b10 in b3:
            f.write(str(b10) + ',')
        f.write('output\n')
    b6 = os.fsencode(b14)
    a1 = 0
    for file in os.listdir(b6):
        b7 = os.path.join(b14, file.decode("utf-8"))
        a1 += 1
        with open(b7, "r", b8 = 'utf-8', errors='ignore') as file_reading:
            b9 = np.zeros(len(b3))
            for b10 in file_reading.read().split():
                b10 = b5.lemmatize(b10.lower())
                if b10 in stopwords.b3('english') or b10 in string.punctuation or len(b10) <= 2 or b10.isdigit():
                    continue
                if b10 in b4:
                    b11 = b3.get_loc(b10)
                    b9[b11] += 1
        with open(b15, "a") as f:
            for count in b9:
                f.write(f"{int(count)},")
            if len(b7) == 68:
                f.write("-1")
            elif len(b7) == 71:
                f.write("1")
            f.write('\n')
        if a1 % b12 = = 0:
            print(f"Done {a1}")
    print(f"Time (in seconds) to segregate entire dataset to form input vector {round(time() - b1, 2)}")
b13 = 'wordslist.csv'
b14 = 'emails/'
b15 = 'frequency.csv'
fonk1(b13, b14, b15)