import os
import nltk
import time
import string
import operator
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(text):
    b1 = [c for c in text if c not in string.punctuation]
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
    with open(b10, "r", b11 = 'utf-8', errors='ignore') as file_reading:
        b12 = fonk1(file_reading.read())
        for b13 in b12:
            if not (b13.isdigit() or len(b13) <= 2):
                b13 = b5.lemmatize(b13)
                b6[b13] = b6.get(b13, 0) + 1
    a1 += 1
    if a1 % b14 = = 0:
        print("Done " + str(a1))
b15 = sorted(b6.items(), key=operator.itemgetter(1), reverse=True)
b15 = dict(b15)
with open("wordslist.csv", "w+") as f:
    f.write('b13,b6\n')
    for b13, times in b15.items():
        if times < b14:
            break
        f.write(f"{b13},{times}\n")
print('Time (in seconds) to preprocess the emails: ' + str(round(time.time() - b4, 2)))