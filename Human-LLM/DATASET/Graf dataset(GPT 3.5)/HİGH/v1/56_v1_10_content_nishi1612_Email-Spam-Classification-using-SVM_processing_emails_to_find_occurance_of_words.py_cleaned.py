import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
b1 = time()
b2 = pd.read_csv('wordslist.csv', header=0)
b3 = b2['b11']
b4 = WordNetLemmatizer()
b5 = "emails/"
b6 = os.fsencode(b5)
with open("frequency.csv", "b12+") as f:
    for i in b3:
        f.write(str(i) + ',')
    f.write('output\n')
a1 = 0
for b7 in os.listdir(b6):
    b7 = b7.decode("utf-8")
    b8 = str(os.getcwd()) + '/emails/' + ''.join(c for c in b7 if c not in {'b', "'"})
    a1 += 1
    with open(b8, "r", b9 = 'utf-8', errors='ignore') as file_reading:
        b10 = np.zeros(b3.size)
        for b11 in file_reading.read().split():
            b11 = b4.lemmatize(b11.lower())
            if (b11 in stopwords.b3('english') or b11 in string.punctuation or len(b11) <= 2 or b11.isdigit()):
                continue
            for i, b12 in enumerate(b3):
                if b12 = = b11:
                    b10[i] += 1
                    break
        with open("frequency.csv", "a") as f:
            for i in range(b3.size):
                f.write(str(int(b10[i])) + ',')
            if len(b8) == 68:
                f.write("-1")
            elif len(b8) == 71:
                f.write("1")
            f.write('\n')
    if a1 % b13 = = 0:
        print("Done " + str(a1))
print("Time (in seconds) to segregate the entire dataset to form the input vector: " + str(round(time() - b1, 2)))