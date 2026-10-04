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
b8 = glob.glob(f"{b1}/*.txt")
b9 = glob.glob(f"{b2}/*.txt")
b10 = glob.glob(f"{b3}/*.txt")
b11 = glob.glob(f"{b4}/*.txt")
def fonk1(filenames, b12 = False):
    b13 = ""
    for filename in filenames:
        with open(filename, 'r') as file:
            b13 += file.read()
    b14 = str.maketrans('', '', string.punctuation + string.digits)
    b13 = b13.translate(b14)
    b15 = Counter(b13.split())
    if b12:
        b16 = set(stopwords.words('english'))
        b15 = Counter([word for word in b15 if word not in b16])
    return b15
def fonk2(b15):
    b17 = sum(b15.values())
    b18 = {word: count / b17 for word, count in b15.items()}
    return b18
def fonk3(b15, b23):
    return {word: (b15[word] + 1) / (b23[word] + len(b23)) for word in b23}
def fonk4(test_files, b23, b24, b25):
    ham_count, b19 = 0, 0
    for filename in test_files:
        with open(filename, 'r') as file:
            b13 = file.read()
        b15 = Counter(b13.split())
        prob_ham, b20 = 1.0, 1.0
        for word in b15:
            if word in b23:
                prob_ham *= b24.get(word, 1.0)
                b20 *= b25.get(word, 1.0)
        if prob_ham > b20:
            ham_count += 1
        else:
            b19 += 1
    return ham_count, b19
def fonk5(ham_counts, spam_counts, b23):
    for word in b23:
        ham_counts[word] += 1
        spam_counts[word] += 1
    return ham_counts, spam_counts
def fonk6(b12):
    b21 = fonk1(b8, b12)
    b22 = fonk1(b9, b12)
    b23 = set(b21) | set(b22)
    b23 = Counter(b23)
    b21, b22 = fonk5(b21, b22, b23)
    b24 = fonk3(b21, b23)
    b25 = fonk3(b22, b23)
    ham_correct, b26 = fonk4(b10, b23, b24, b25)
    print(f"Ham Accuracy: {ham_correct / len(b10):.2f}")
    print(f"Spam Accuracy: {b26 / len(b11):.2f}")
fonk6(b12 = False)
fonk6(b12 = True)