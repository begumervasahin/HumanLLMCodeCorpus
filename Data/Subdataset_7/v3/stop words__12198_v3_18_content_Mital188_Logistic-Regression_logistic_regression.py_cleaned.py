import glob
from collections import Counter
from nltk.corpus import stopwords
import string
import numpy as np
import sys
ham_train, spam_train, ham_test, b1 = sys.argv[1:5]
Lamda, iteration, b2 = map(float, sys.argv[5:8])
b3 = glob.glob(f"{ham_train}/*.txt")
b4 = glob.glob(f"{spam_train}/*.txt")
b5 = glob.glob(f"{ham_test}/*.txt")
b6 = glob.glob(f"{b1}/*.txt")
def fonk1(filename, b7 = True):
    b8 = ""
    for file_name in filename:
        with open(file_name, 'r') as file:
            b8 += file.read()
    b9 = str.maketrans('', '', string.punctuation)
    b8 = b8.translate(b9)
    b9 = str.maketrans('', '', string.digits)
    b8 = b8.translate(b9)
    b10 = Counter(b8.split())
    if b7:
        b10 = Counter([word for word in b10 if word not in stopwords.words('english')])
    return b10
def fonk2(word_counts, b11 = 2):
    return Counter({word: count for word, count in word_counts.items() if count >= b11})
def fonk3(b7):
    b12 = fonk1(b4, b7)
    b13 = fonk2(b12, b11=2)
    b14 = []
    for file_name in b3 + b4:
        b15 = {}
        with open(file_name, 'r') as file:
            b16 = file.read().split(" ")
            b17 = Counter(b16)
            for word in b13:
                b15[word] = b17[word]
            b15["Probability_of_class"] = 0.0 if "ham" in file_name else 1.0
            b14.append(b15)
    return b14, b13
def fonk4(a3, b21, b14):
    for b15 in b14:
        b18 = sum(b21[word] * b15[word] for word in b21)
        b19 = np.exp(a3 + b18) / (1 + np.exp(a3 + b18)) if b18 < 700 else 1.0
        b15["Probability_of_class"] = b19
    return b14
def fonk5(b21, b2, Lamda, b14):
    for word in b21:
        b20 = sum(b15[word] * (b15["Probability_of_class"] - b15["Class_of_file"]) for b15 in b14)
        b21[word] += b2 * b20 - b2 * Lamda * b21[word]
    return b21
def fonk6(b21):
    a1 = 0
    a2 = 0
    for file_name in b6:
        with open(file_name, 'r') as file:
            b16 = file.read().split(" ")
            b17 = Counter(b16)
            b18 = sum(b21[word] * b17[word] for word in b21)
            b19 = np.exp(1 + b18) / (1 + np.exp(1 + b18)) if b18 < 700 else 1.0
            if b19 > 0.9:
                a1 += 1
            a2 += 1
    for file_name in b5:
        with open(file_name, 'r') as file:
            b16 = file.read().split(" ")
            b17 = Counter(b16)
            b18 = sum(b21[word] * b17[word] for word in b21)
            b19 = np.exp(1 + b18) / (1 + np.exp(1 + b18)) if b18 < 700 else 1.0
            if b19 < 0.9:
                a1 += 1
            a2 += 1
    return a1 / a2
def fonk7(iterations, b2, Lamda, b7):
    b14, b13 = fonk3(b7)
    a3 = 1.0
    b21 = {word: 1.0 for word in b13}
    b14 = fonk4(a3, b21, b14)
    for _ in range(iterations):
        b21 = fonk5(b21, b2, Lamda, b14)
        b14 = fonk4(a3, b21, b14)
    b22 = fonk6(b21)
    print(f"Logistic Regression - {'filtered' if b7 else 'unfiltered'} - Total Accuracy - {b22 * 100:.2f}")
fonk7(iteration, b2, Lamda, b7 = False)
fonk7(iteration, b2, Lamda, b7 = True)