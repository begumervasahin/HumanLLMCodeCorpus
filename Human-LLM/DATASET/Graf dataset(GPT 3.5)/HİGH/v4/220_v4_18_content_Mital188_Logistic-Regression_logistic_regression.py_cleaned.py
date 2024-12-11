import glob
import numpy as np
from collections import Counter
from nltk.corpus import stopwords
import string
import sys
def fonk1(filenames, b27):
    b1 = ""
    for file_name in filenames:
        with open(file_name) as file:
            b1 += file.read()
    b2 = str.maketrans('', '', string.punctuation)
    b1 = b1.translate(b2)
    b2 = str.maketrans('', '', string.digits)
    b1 = b1.translate(b2)
    b3 = Counter(b1.split())
    if b27:
        b4 = set(stopwords.words('english'))
        b3 = Counter({word: count for word, count in b3.items() if word not in b4})
    return b3
def fonk2(b9, count):
    b5 = Counter()
    for word, count in b9.items():
        if count >= 2:
            b5[word] = count
    return b5
def fonk3(b27):
    b6 = glob.glob(b21 + "/*.txt")
    b7 = glob.glob(b20 + "/*.txt")
    b8 = fonk1(b6, b27)
    b9 = fonk2(b8, count=4000)
    b10 = []
    for file_name in b7:
        b11 = {}
        with open(file_name) as file:
            b12 = file.read().split()
            b13 = Counter(b12)
            for word in b9:
                b11[word] = b13[word]
            b11["Probability_of_class"] = 0.0
            b11["Class_of_file"] = 0
            b10.append(b11)
    for file_name in b6:
        b11 = {}
        with open(file_name) as file:
            b12 = file.read().split()
            b13 = Counter(b12)
            for word in b9:
                b11[word] = b13[word]
            b11["Probability_of_class"] = 0.0
            b11["Class_of_file"] = 1
            b10.append(b11)
    return b10, b9
def fonk4(a3, b18, b10):
    for b11 in b10:
        b14 = sum(b18[word] * b11[word] for word in b18)
        if b14 < 700:
            b15 = np.exp(a3 + b14) / (1 + np.exp(a3 + b14))
        else:
            b15 = 1.0
        b11["Probability_of_class"] = b15
    return b10
def fonk5(b18, n, lam, b10):
    for word in b18:
        b16 = sum(b11[word] * (b11["Class_of_file"] - b11["Probability_of_class"]) for b11 in b10)
        b18[word] += n * b16 - n * lam * b18[word]
    return b18
def fonk6(b18):
    a1 = 0
    a2 = 0
    for file_name in b23:
        with open(file_name) as file:
            b12 = file.read().split()
            b13 = Counter(b12)
            b14 = sum(b18[word] * b13[word] for word in b18)
            if b14 < 700:
                b15 = np.exp(1 + b14) / (1 + np.exp(1 + b14))
            else:
                b15 = 1.0
            if b15 > 0.9:
                a1 += 1
            a2 += 1
    for file_name in b22:
        with open(file_name) as file:
            b12 = file.read().split()
            b13 = Counter(b12)
            b14 = sum(b18[word] * b13[word] for word in b18)
            if b14 < 700:
                b15 = np.exp(1 + b14) / (1 + np.exp(1 + b14))
            else:
                b15 = 1.0
            if b15 < 0.9:
                a1 += 1
            a2 += 1
    return a1 / a2
def fonk7(iterations, n, lam, b27):
    b10, b9 = fonk3(b27)
    a3 = 1.0
    b17 = {word: 1.0 for word in b9}
    b10 = fonk4(a3, b17, b10)
    b18 = b17
    for _ in range(iterations):
        b18 = fonk5(b18, n, lam, b10)
        b10 = fonk4(a3, b18, b10)
    b19 = fonk6(b18)
    if b27:
        print("Logistic Regression - filtered - Total Accuracy - {:.2f}%".format(b19 * 100))
    else:
        print("Logistic Regression - unfiltered - Total Accuracy - {:.2f}%".format(b19 * 100))
b20 = sys.argv[1]
b21 = sys.argv[2]
b22 = glob.glob(sys.argv[3] + "/*.txt")
b23 = glob.glob(sys.argv[4] + "/*.txt")
b24 = float(sys.argv[5])
b25 = int(sys.argv[6])
b26 = float(sys.argv[7])
fonk7(b25, b26, b24, b27 = 0)
fonk7(b25, b26, b24, b27 = 1)