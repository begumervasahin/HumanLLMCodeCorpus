import os
from os import listdir
from os.path import isfile, join
import csv
import string
from nltk.corpus import stopwords
def fonk1(filename, b11):
    with open(filename, "b2", b1 = '') as f:
        b2 = csv.writer(f)
        for key, val in b11.items():
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
    b8 = set(stopwords.words('english'))
    b8.add("subject")
    b6 = b6.replace('\n', ' ')
    b6 = b6.translate(b7)
    b9 = b6.split(' ')
    b9 = [word for word in b9 if word not in b8]
    return b9
def fonk4(filename):
    b10 = [f for f in listdir(filename) if isfile(join(filename, f))]
    b11 = {}
    a1 = 0
    for file in b10:
        with open(join(filename, file), b12 = "ignore") as f:
            b6 = f.read()
        b9 = fonk3(b6)
        for word in b9:
            a1 += 1
            if word in b11:
                b11[word] += 1
            else:
                b11[word] = 1
    b13 = len(b10)
    for word in b11.keys():
        b11[word] = float(b11[word]) / b13
    b11["fileCount"] = b13
    return b11
def fonk5(b14, diction, priori):
    b14 = fonk3(b14)
    a2 = 1
    for word in b14:
        if word in diction:
            a2 *= diction[word]
        else:
            a2 *= 1 / (diction["fileCount"] + len(diction) + 1)
    a2 *= priori
    return a2
def fonk6():
    fonk1("spam_train_results.csv", fonk4("spam"))
    fonk1("ham_train_results.csv", fonk4("ham"))
def fonk7():
    b15 = fonk2("ham_train_results.csv")
    b16 = fonk2("spam_train_results.csv")
    b10 = [f for f in listdir("input") if isfile(join("input", f))]
    b17 = ham_count = 0
    for file in b10:
        with open(join("input", file), b12 = "ignore") as f:
            b6 = f.read()
        b18 = fonk5(b6, b15, 0.67)
        b19 = fonk5(b6, b16, 0.33)
        if b18 <= b19:
            b17 += 1
        else:
            ham_count += 1
    print("Spam:\t" + str(b17))
    print("Ham:\t" + str(ham_count))
if b20 = = "__main__":
    fonk6()
    fonk7()