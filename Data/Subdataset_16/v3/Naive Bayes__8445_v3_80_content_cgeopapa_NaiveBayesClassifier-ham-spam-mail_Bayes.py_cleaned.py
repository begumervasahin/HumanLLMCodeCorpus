import os
import csv
import string
from os import listdir
from os.path import isfile, join
from nltk.corpus import stopwords
def fonk1(filename, b3):
    with open(filename, "w", b1 = '') as f:
        b2 = csv.b2(f)
        for key, val in b3.items():
            b2.writerow([key, val])
def fonk2(filename):
    b3 = {}
    with open(filename, b4 = 'r') as infile:
        b5 = csv.b5(infile)
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
    b11 = [f for f in listdir(directory) if isfile(join(directory, f))]
    b3 = {}
    a1 = 0
    for file in b11:
        with open(join(directory, file), b12 = "ignore") as f:
            b6 = f.read()
        b9 = fonk3(b6)
        for word in b9:
            a1 += 1
            b3[word] = b3.get(word, 0) + 1
    b13 = len(b11)
    for word in b3:
        b3[word] = b3[word] / b13
    b3["fileCount"] = b13
    return b3
def fonk5(input_text, b3, prior):
    b9 = fonk3(input_text)
    a2 = 1
    for word in b9:
        if word in b3:
            a2 *= b3[word]
        else:
            a2 *= 1 / (b3["fileCount"] + len(b3) + 1)
    return a2 * prior
def fonk6():
    fonk1("spam_train_results.csv", fonk4("spam"))
    fonk1("ham_train_results.csv", fonk4("ham"))
def fonk7():
    b14 = fonk2("ham_train_results.csv")
    b15 = fonk2("spam_train_results.csv")
    b11 = [f for f in listdir("input") if isfile(join("input", f))]
    b16 = ham_count = 0
    for file in b11:
        with open(join("input", file), b12 = "ignore") as f:
            b6 = f.read()
        b17 = fonk5(b6, b14, 0.67)
        b18 = fonk5(b6, b15, 0.33)
        if b17 <= b18:
            b16 += 1
        else:
            ham_count += 1
    print("Spam:\t", b16)
    print("Ham:\t", ham_count)
if b19 = = "__main__":
    fonk6()
    fonk7()