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
with open("frequency.csv", "w+") as freq_file:
    freq_file.write(','.join(b3) + ',output\n')
a1 = 0
for file in os.listdir(b6):
    b7 = os.fsdecode(file)
    b8 = os.path.join(os.getcwd(), 'emails', b7)
    a1 += 1
    with open(b8, "r", b9 = 'utf-8', errors='ignore') as email_file:
        b10 = np.zeros(len(b3))
        for b11 in email_file.read().split():
            b11 = b4.lemmatize(b11.lower())
            if b11 in stopwords.b3('english') or b11 in string.punctuation or len(b11) <= 2 or b11.isdigit():
                continue
            if b11 in b3.values:
                b12 = b3[b3 == b11].index[0]
                b10[b12] += 1
        with open("frequency.csv", "a") as freq_file:
            freq_file.write(','.join(map(str, b10.astype(int))) + ',')
            if len(b8) == 68:
                freq_file.write("-1")
            elif len(b8) == 71:
                freq_file.write("1")
            freq_file.write('\n')
    if a1 % b13 = = 0:
        print(f"Processed {a1} files")
print(f"Time (in seconds) to process the dataset: {round(time() - b1, 2)}")