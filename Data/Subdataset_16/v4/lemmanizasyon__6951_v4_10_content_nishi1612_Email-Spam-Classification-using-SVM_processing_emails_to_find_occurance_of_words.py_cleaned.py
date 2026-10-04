import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
b1 = time()
b2 = pd.read_csv('wordslist.csv')
b3 = b2['b10']
b4 = WordNetLemmatizer()
b5 = "emails/"
b6 = os.fsencode(b5)
with open("frequency.csv", "w") as f:
    f.write(','.join(b3) + ',output\n')
a1 = 0
for file in os.listdir(b6):
    b7 = os.path.join(b5, file.decode("utf-8"))
    with open(b7, "r", b8 = 'utf-8', errors='ignore') as file_reading:
        b9 = np.zeros(b3.size)
        for b10 in file_reading.read().split():
            b10 = b4.lemmatize(b10.lower())
            if (b10 in stopwords.b3('english') or
                b10 in string.punctuation or
                len(b10) <= 2 or
                b10.isdigit()):
                continue
            if b10 in b3.values:
                b9[b3[b3 = = b10].index[0]] += 1
    with open("frequency.csv", "a") as f:
        f.write(','.join(map(str, map(int, b9))) + ',')
        f.write("-1" if len(b7) == 68 else "1")
        f.write('\n')
    a1 += 1
    if a1 % b11 = = 0:
        print(f"Processed {a1} files")
print(f"Time (in seconds) to process dataset: {round(time() - b1, 2)}")