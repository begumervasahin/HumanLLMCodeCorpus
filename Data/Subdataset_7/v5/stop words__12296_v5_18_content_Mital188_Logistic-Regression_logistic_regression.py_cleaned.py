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
def fonk2(b16, min_count):
    return Counter({word: count for word, count in b16.items() if count >= min_count})
def fonk3(b13, b14, b16):
    b5 = []
    for file_name in b13:
        with open(file_name) as file:
            b6 = file.read().split()
            b7 = Counter(b6)
            b8 = {word: b7[word] for word in b16}
            b8["Probability_of_class"] = 0.0
            b8["Class_of_file"] = 0
            b5.append(b8)
    for file_name in b14:
        with open(file_name) as file:
            b6 = file.read().split()
            b7 = Counter(b6)
            b8 = {word: b7[word] for word in b16}
            b8["Probability_of_class"] = 0.0
            b8["Class_of_file"] = 1
            b5.append(b8)
    return b5
def fonk4(a1, b18, b5):
    for b8 in b5:
        b9 = sum(b18[word] * b8[word] for word in b18)
        b10 = np.exp(a1 + b9) / (1 + np.exp(a1 + b9)) if b9 < 700 else 1.0
        b8["Probability_of_class"] = b10
    return b5
def fonk5(b18, n, lam, b5):
    for word in b18:
        b11 = sum(b8[word] * (b8["Class_of_file"] - b8["Probability_of_class"]) for b8 in b5)
        b18[word] += n * b11 - n * lam * b18[word]
    return b18
def fonk6(b18, b23, b22):
    count_right, b12 = 0, 0
    for file_name in b23 + b22:
        with open(file_name) as file:
            b6 = file.read().split()
            b7 = Counter(b6)
            b9 = sum(b18[word] * b7[word] for word in b18)
            b10 = np.exp(1 + b9) / (1 + np.exp(1 + b9)) if b9 < 700 else 1.0
            if (b10 > 0.9 and "spam" in file_name) or (b10 < 0.9 and "ham" in file_name):
                count_right += 1
            b12 += 1
    return count_right / b12
def fonk7(iterations, n, lam, b20, b21, b22, b23, b27):
    b13 = glob.glob(b20 + "/*.txt")
    b14 = glob.glob(b21 + "/*.txt")
    b15 = b13 + b14
    b3 = fonk1(b15, b27)
    b16 = fonk2(b3, min_count=2)
    b5 = fonk3(b13, b14, b16)
    a1 = 1.0
    b17 = {word: 1.0 for word in b16}
    b5 = fonk4(a1, b17, b5)
    b18 = b17
    for _ in range(iterations):
        b18 = fonk5(b18, n, lam, b5)
        b5 = fonk4(a1, b18, b5)
    b19 = fonk6(b18, b23, b22)
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
fonk7(b25, b26, b24, b20, b21, b22, b23, b27 = False)
fonk7(b25, b26, b24, b20, b21, b22, b23, b27 = True)