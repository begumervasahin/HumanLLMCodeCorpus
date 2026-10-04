import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
b1 = time()
b2 = pd.read_csv('wordslist.csv')
b3 = b2['b12'].tolist()
b4 = WordNetLemmatizer()
b5 = "emails/"
b6 = os.fsencode(b5)
with open("frequency.csv", "w") as freq_file:
    b7 = ','.join(b3) + ',output\n'
    freq_file.write(b7)
a1 = 0
for file in os.listdir(b6):
    b8 = os.fsdecode(file)
    b9 = os.path.join(b5, b8)
    a1 += 1
    with open(b9, "r", b10 = 'utf-8', errors='ignore') as email_file:
        b11 = np.zeros(len(b3))
        for b12 in email_file.read().split():
            b12 = b4.lemmatize(b12.lower())
            if b12 in stopwords.b3('english') or b12 in string.punctuation or len(b12) <= 2 or b12.isdigit():
                continue
            if b12 in b3:
                b11[b3.index(b12)] += 1
        with open("frequency.csv", "a") as freq_file:
            freq_file.write(','.join(map(str, map(int, b11))) + ',')
            b13 = "1" if len(b8) == 71 else "-1"
            freq_file.write(b13 + '\n')
    if a1 % b14 = = 0:
        print(f"Processed {a1} files")
b15 = round(time() - b1, 2)
print(f"Time (in seconds) to process the entire dataset: {b15}")