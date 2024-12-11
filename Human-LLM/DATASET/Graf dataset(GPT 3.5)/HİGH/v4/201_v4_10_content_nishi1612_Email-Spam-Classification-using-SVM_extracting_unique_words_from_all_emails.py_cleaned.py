import os
import nltk
import time
import string
import operator
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(text):
    b1 = [char for char in text if char not in string.punctuation]
    b1 = ''.join(b1)
    b2 = [b13 for b13 in b1.split() if b13.lower() not in stopwords.b12('english')]
    b2 = ' '.join(b2)
    b3 = [b13.lower() for b13 in b2.split()]
    return b3
b4 = time.time()
b5 = WordNetLemmatizer()
a1 = 0
b6 = {}
b7 = "emails/"
b8 = os.fsencode(b7)
for b9 in os.listdir(b8):
    b9 = b9.decode("utf-8")
    b10 = os.path.join(os.getcwd(), 'emails', b9)
    with open(b10, "r", b11 = 'utf-8', errors='ignore') as file_reader:
        b12 = fonk1(file_reader.read())
        for b13 in b12:
            if not b13.isdigit() and len(b13) > 2:
                b13 = b5.lemmatize(b13)
                if b13 in b6:
                    b6[b13] += 1
                else:
                    b6[b13] = 1
        a1 += 1
        if a1 % b14 = = 0:
            print(f"Processed {a1} files")
b15 = sorted(b6.items(), key=operator.itemgetter(1), reverse=True)
b15 = dict(b15)
with open("wordslist.csv", "w+") as csv_file:
    csv_file.write('b13,count\n')
    for b13, count in b15.items():
        if count < b14:
            break
        csv_file.write(f"{b13},{count}\n")
print(f'Time taken to preprocess emails: {round(time.time() - b4, 2)} seconds')