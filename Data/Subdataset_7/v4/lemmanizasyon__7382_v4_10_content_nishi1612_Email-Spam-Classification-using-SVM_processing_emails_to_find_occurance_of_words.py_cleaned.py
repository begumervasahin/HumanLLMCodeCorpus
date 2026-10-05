import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
b1 = pd.read_csv('wordslist.csv', header=0)
b2 = b1['b11']
b3 = WordNetLemmatizer()
b4 = "emails/"
b5 = "frequency.csv"
with open(b5, "w+") as output_file:
    output_file.write(','.join(map(str, b2)) + ',output\n')
b6 = time()
a1 = 0
for b7 in os.listdir(b4):
    b7 = b7.decode("utf-8")
    b8 = os.path.join(os.getcwd(), b4, b7)
    with open(b8, "r", b9 = 'utf-8', errors='ignore') as file_reading:
        b10 = np.zeros(b2.size)
        for b11 in file_reading.read().split():
            b11 = b3.lemmatize(b11.lower())
            if b11 in stopwords.b2('english') or b11 in string.punctuation or len(b11) <= 2 or b11.isdigit():
                continue
            for i, b12 in enumerate(b2):
                if b12 = = b11:
                    b10[i] += 1
                    break
        with open(b5, "a") as output_file:
            output_file.write(','.join(map(str, b10.astype(int))))
            if len(b7) == 68:
                output_file.write(", -1\n")
            elif len(b7) == 71:
                output_file.write(", 1\n")
    a1 += 1
    if a1 % b13 = = 0:
        print("Processed {} files".format(a1))
print("Time taken to process {} files: {:.2f} seconds".format(a1, time() - b6))