import glob
from collections import Counter
from nltk.corpus import stopwords
import string
import numpy as np
import sys
def fonk1(filenames, b24):
    b1 = ""
    for filename in filenames:
        with open(filename, 'r') as file:
            b1 += file.read()
    b2 = str.maketrans('', '', string.punctuation + string.digits)
    b1 = b1.translate(b2)
    b3 = Counter(b1.split())
    if b24:
        b3 = Counter([word for word in b3 if word not in stopwords.words('english')])
    return b3
def fonk2(b3):
    b4 = sum(b3.values())
    return {word: count / b4 for word, count in b3.items()}
def fonk3(b3, b8):
    return {word: b3.get(word, 0) / (b8.get(word, 0) + len(b8)) for word in b8}
def fonk4(test_files, b10, b11, b8):
    a1 = 0.0
    a2 = 0.0
    for filename in test_files:
        with open(filename, 'r') as file:
            b5 = file.read()
        b5 = Counter(b5.split())
        a3 = 1.0
        a4 = 1.0
        for word in b5:
            if word in b8:
                a3 *= b10.get(word, 0)
                a4 *= b11.get(word, 0)
        if a3 + a4:
            if a3 / (a3 + a4) > 0.5:
                a1 += 1
            else:
                a2 += 1
    return a1, a2
def fonk5(train_ham, train_spam, b8):
    for word in b8:
        train_ham[word] += 1
        train_spam[word] += 1
    return train_ham, train_spam
def fonk6(b17, b18, b19, b20, b24):
    b6 = fonk1(b17, b24)
    b7 = fonk1(b18, b24)
    b8 = b6 + b7
    train_ham_smoothed, b9 = fonk5(b6, b7, b8)
    b10 = fonk3(train_ham_smoothed, b8)
    b11 = fonk3(b9, b8)
    a1, a2 = fonk4(b19, b10, b11, b8)
    b12 = len(b19)
    b13 = len(b20)
    b14 = a1 / b12 if b12 > 0 else 0
    b15 = a2 / b13 if b13 > 0 else 0
    print(f"Ham Accuracy: {b14}")
    print(f"Spam Accuracy: {b15}")
if b16 = = "__main__":
    b17 = glob.glob(sys.argv[1] + "/*.txt")
    b18 = glob.glob(sys.argv[2] + "/*.txt")
    b19 = glob.glob(sys.argv[3] + "/*.txt")
    b20 = glob.glob(sys.argv[4] + "/*.txt")
    b21 = float(sys.argv[5])
    b22 = int(sys.argv[6])
    b23 = float(sys.argv[7])
    fonk6(b17, b18, b19, b20, b24 = False)
    fonk6(b17, b18, b19, b20, b24 = True)