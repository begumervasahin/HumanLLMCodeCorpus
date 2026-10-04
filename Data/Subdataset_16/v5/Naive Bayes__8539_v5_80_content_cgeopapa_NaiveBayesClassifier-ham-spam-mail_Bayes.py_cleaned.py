import os
import csv
import string
from nltk.corpus import stopwords
def fonk1(filename, b3):
    with open(filename, "w", b1 = '') as file:
        b2 = csv.b2(file)
        for key, val in b3.items():
            b2.writerow([key, val])
def fonk2(filename):
    b3 = {}
    with open(filename, b4 = 'r') as file:
        b5 = csv.b5(file)
        for rows in b5:
            if len(rows) == 2:
                b3[rows[0]] = float(rows[1])
    return b3
def fonk3(b6):
    b6 = b6.lower()
    b7 = str.maketrans('', '', string.punctuation + '\0')
    b8 = set(stopwords.b9('english'))
    b8.add("subject")
    b6 = b6.replace('\n', ' ')
    b6 = b6.translate(b7)
    b9 = b6.split()
    b10 = [word for word in b9 if word not in b8]
    return b10
def fonk4(directory):
    b11 = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    b12 = {}
    a1 = 0
    for file in b11:
        with open(os.path.join(directory, file), b13 = "ignore") as f:
            b6 = f.read()
        b9 = fonk3(b6)
        for word in b9:
            a1 += 1
            b12[word] = b12.get(word, 0) + 1
    b14 = len(b11)
    for word in b12:
        b12[word] = float(b12[word]) / b14
    b12["fileCount"] = b14
    return b12
def fonk5(b6, word_freqs, prior_prob):
    b9 = fonk3(b6)
    a2 = 1
    for word in b9:
        if word in word_freqs:
            a2 *= word_freqs[word]
        else:
            a2 *= 1 / (word_freqs["fileCount"] + len(word_freqs) + 1)
    a2 *= prior_prob
    return a2
def fonk6():
    fonk1("spam_train_results.csv", fonk4("spam"))
    fonk1("ham_train_results.csv", fonk4("ham"))
def fonk7():
    b15 = fonk2("ham_train_results.csv")
    b16 = fonk2("spam_train_results.csv")
    b11 = [f for f in os.listdir("input") if os.path.isfile(os.path.join("input", f))]
    a3 = 0
    a4 = 0
    for file in b11:
        with open(os.path.join("input", file), b13 = "ignore") as f:
            b6 = f.read()
        b17 = fonk5(b6, b15, 0.67)
        b18 = fonk5(b6, b16, 0.33)
        if b17 <= b18:
            a3 += 1
        else:
            a4 += 1
    print(f"Spam: {a3}")
    print(f"Ham: {a4}")
if b19 = = "__main__":
    fonk6()
    fonk7()