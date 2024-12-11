import glob
from collections import Counter
from nltk.corpus import stopwords
import string
import numpy as np
import sys
b1 = sys.argv[1]
b2 = sys.argv[2]
b3 = sys.argv[3]
b4 = sys.argv[4]
b5 = float(sys.argv[5])
b6 = int(sys.argv[6])
b7 = float(sys.argv[7])
b8 = glob.glob(b1 + "/*.txt")
b9 = glob.glob(b2 + "/*.txt")
b10 = glob.glob(b3 + "/*.txt")
b11 = glob.glob(b4 + "/*.txt")
def fonk1(filename, stop_words):
    b12 = ""
    for file_name in filename:
        with open(file_name, 'r') as file:
            b12 += file.read()
    b13 = str.maketrans('', '', string.punctuation)
    b12 = b12.translate(b13)
    b13 = str.maketrans('', '', string.digits)
    b12 = b12.translate(b13)
    b12 = Counter(b12.split())
    if stop_words:
        b12 = Counter([word for word in b12 if word not in stopwords.words('english')])
    return b12
def fonk2(b16, count):
    b14 = Counter({word: count for word, count in b16.items() if count >= 2})
    return b14
def fonk3(b24):
    b15 = fonk1(b9, b24)
    b16 = fonk2(b15, count=4000)
    b17 = []
    for file_name in b8:
        b18 = {}
        with open(file_name, 'r') as file:
            b19 = file.read().split(" ")
            b19 = Counter(b19)
            for word in b16:
                b18[word] = (b19[word])
            b18["Probability_of_class"] = 0.0
            b18["Class_of_file"] = 0
            b17.append(b18)
    for file_name in b9:
        b18 = {}
        with open(file_name, 'r') as file:
            b19 = file.read().split(" ")
            b19 = Counter(b19)
            for word in b16:
                b18[word] = (b19[word])
            b18["Probability_of_class"] = 0.0
            b18["Class_of_file"] = 1
            b17.append(b18)
    return b17, b16
def fonk4(a5, b22, feature_mat):
    for b18 in feature_mat:
        a1 = 0
        for word in b22:
            a1 += b22[word] * b18[word]
        if a1 < 700:
            b20 = np.exp(np.array(a5 + a1, dtype=np.float)) / (1 + np.exp(np.array(a5 + a1, dtype=np.float)))
        else:
            b20 = 1.0
        b18["Probability_of_class"] = b20
    return feature_mat
def fonk5(b22, n, lam, b17):
    for word in b22:
        a2 = 0.0
        for b18 in b17:
            a2 += b18[word] * (b18["Class_of_file"] - b18["Probability_of_class"])
        b22[word] += n * a2 - n * lam * b22[word]
    return b22
def fonk6(b22):
    a3 = 0
    a4 = 0
    for file_name in b11:
        with open(file_name, 'r') as file:
            b19 = file.read().split(" ")
            b19 = Counter(b19)
            a1 = 0
            a4 += 1
            for word in b22:
                a1 += b22[word] * b19[word]
            if a1 < 700:
                b20 = np.exp(np.array(1 + a1, dtype=np.float)) / (1 + np.exp(np.array(1 + a1, dtype=np.float)))
            else:
                b20 = 1.0
            if b20 > 0.9:
                a3 += 1
    for file_name in b10:
        with open(file_name, 'r') as file:
            b19 = file.read().split(" ")
            b19 = Counter(b19)
            a1 = 0
            a4 += 1
            for word in b22:
                a1 += b22[word] * b19[word]
            if a1 < 700:
                b20 = np.exp(np.array(1 + a1, dtype=np.float)) / (1 + np.exp(np.array(1 + a1, dtype=np.float)))
            else:
                b20 = 1.0
            if b20 < 0.9:
                a3 += 1
    return a3 / a4
def fonk7(b25, n, lam, b24):
    b17, b16 = fonk3(b24)
    a5 = 1.0
    b21 = {word: 1.0 for word in b16}
    b17 = fonk4(a5, b21, b17)
    b22 = b21
    for i in range(b25):
        b22 = fonk5(b22, n, lam, b17)
        b17 = fonk4(a5, b22, b17)
    b23 = fonk6(b22)
    if b24 = = 1:
        print("Logistic Regression - filtered - Total Accuracy - {:.2f}".format(b23 * 100))
    else:
        print("Logistic Regression - unfiltered - Total Accuracy - {:.2f}".format(b23 * 100))
fonk7(b25 = b6, n=b7, lam=b5, b24=0)
fonk7(b25 = b6, n=b7, lam=b5, b24=1)