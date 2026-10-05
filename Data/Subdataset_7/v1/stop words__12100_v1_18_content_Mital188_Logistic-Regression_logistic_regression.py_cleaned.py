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
def fonk2(b15, count):
    a1 = 0
    for word in list(b15):
        if b15[word] < 2 and a1 < count:
            a1 += 1
            del b15[word]
    return b15
def fonk3(b23):
    b14 = fonk1(b9, b23)
    b15 = b14
    b15 = fonk2(b15, count=4000)
    b16 = []
    for file_name in b8:
        b17 = {}
        with open(file_name, 'r') as file:
            b18 = file.read().split(" ")
            b18 = Counter(b18)
            for words in b15:
                b17[words] = (b18[words])
            b17["Probability_of_class"] = 0.0
            b17["Class_of_file"] = 0
            b16.append(b17)
    for file_name in b9:
        b17 = {}
        with open(file_name, 'r') as file:
            b18 = file.read().split(" ")
            b18 = Counter(b18)
            for words in b15:
                b17[words] = (b18[words])
            b17["Probability_of_class"] = 0.0
            b17["Class_of_file"] = 1
            b16.append(b17)
    return b16, b15
def fonk4(a6, weights, feature_mat):
    for b17 in feature_mat:
        a2 = 0
        for words in weights:
            a2 += weights[words] * b17[words]
        if a2 < 700:
            b19 = np.exp(np.array(a6 + a2, dtype=np.float)) / (1 + np.exp(np.array(a6 + a2, dtype=np.float)))
        else:
            b19 = 1.0
        b17["Probability_of_class"] = b19
    return feature_mat
def fonk5(weights, n, lam, b16):
    for b21 in weights:
        a3 = 0.0
        for b17 in b16:
            a3 += b17[b21] * (b17["Class_of_file"] - b17["Probability_of_class"])
        weights[b21] = weights[b21] + n * a3 - n * lam * weights[b21]
    return weights
def fonk6(weights):
    a4 = 0
    a5 = 0
    for file_name in b11:
        with open(file_name, 'r') as file:
            b18 = file.read().split(" ")
            b18 = Counter(b18)
            a2 = 0
            a5 += 1
            for words in weights:
                a2 += weights[words] * b18[words]
            if a2 < 700:
                b19 = np.exp(np.array(1 + a2, dtype=np.float)) / (1 + np.exp(np.array(1 + a2, dtype=np.float)))
            else:
                b19 = 1.0
            if b19 > 0.9:
                a4 += 1
    for file_name in b10:
        with open(file_name, 'r') as file:
            b18 = file.read().split(" ")
            b18 = Counter(b18)
            a2 = 0
            a5 += 1
            for words in weights:
                a2 += weights[words] * b18[words]
            if a2 < 700:
                b19 = np.exp(np.array(1 + a2, dtype=np.float)) / (1 + np.exp(np.array(1 + a2, dtype=np.float)))
            else:
                b19 = 1.0
            if b19 < 0.9:
                a4 += 1
    return a4 / a5
def fonk7(b24, n, lam, b23):
    b16, b15 = fonk3(b23)
    a6 = 1.0
    b20 = {word: 1.0 for word in b15}
    b16 = fonk4(a6, b20, b16)
    b21 = b20
    for i in range(b24):
        b21 = fonk5(b21, n, lam, b16)
        b16 = fonk4(a6, b21, b16)
    b22 = fonk6(b21)
    if b23 = = 1:
        print("Logistic Regression - filtered - Total Accuracy - {:.2f}".format(b22 * 100))
    else:
        print("Logistic Regression - unfiltered - Total Accuracy - {:.2f}".format(b22 * 100))
fonk7(b24 = b6, n=b7, lam=b5, b23=0)
fonk7(b24 = b6, n=b7, lam=b5, b23=1)