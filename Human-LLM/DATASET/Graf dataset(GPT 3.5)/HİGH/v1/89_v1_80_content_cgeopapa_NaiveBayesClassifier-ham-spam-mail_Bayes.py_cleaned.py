import os
import csv
import string
from nltk.corpus import stopwords
def fonk1(filename, b11):
    with open(filename, "w", b1 = '') as file:
        b2 = csv.b2(file)
        for key, val in b11.items():
            b2.writerow([key, val])
def fonk2(filename):
    b3 = {}
    with open(filename, b4 = 'r') as file:
        b5 = csv.b5(file)
        for row in b5:
            if len(row) == 2:
                b3[row[0]] = float(row[1])
    return b3
def fonk3(b6):
    b6 = b6.lower()
    b7 = dict.fromkeys(map(ord, string.punctuation + '\0'), None)
    b8 = set(stopwords.b9('english'))
    b8.add("subject")
    b6 = b6.replace('\n', ' ')
    b6 = b6.translate(b7)
    b9 = b6.split(' ')
    b9 = [word for word in b9 if word not in b8]
    return b9
def fonk4(filename):
    b10 = [f for f in os.listdir(filename) if os.path.isfile(os.path.join(filename, f))]
    b11 = {}
    a1 = 0
    for file in b10:
        with open(os.path.join(filename, file), b12 = "ignore") as f:
            b6 = f.read()
        b13 = fonk3(b6)
        for word in b13:
            a1 += 1
            if word in b11:
                b11[word] += 1
            else:
                b11[word] = 1
    b14 = len(b10)
    for word in b11.keys():
        b11[word] = float(b11[word]) / b14
    b11["b14"] = b14
    return b11
def fonk5(input_text, diction, priori):
    b15 = fonk3(input_text)
    a2 = 1
    for word in b15:
        if word in diction:
            a2 *= diction[word]
        else:
            a2 *= 1 / (diction["b14"] + len(diction) + 1)
    a2 *= priori
    return a2
def fonk6():
    b16 = fonk4("spam")
    b17 = fonk4("ham")
    fonk1("spam_train_results.csv", b16)
    fonk1("ham_train_results.csv", b17)
def fonk7():
    b18 = fonk2("ham_train_results.csv")
    b19 = fonk2("spam_train_results.csv")
    b20 = [f for f in os.listdir("input") if os.path.isfile(os.path.join("input", f))]
    b21 = ham_count = 0
    for file in b20:
        with open(os.path.join("input", file), b12 = "ignore") as f:
            b6 = f.read()
        b22 = fonk5(b6, b18, 0.67)
        b23 = fonk5(b6, b19, 0.33)
        if b22 <= b23:
            b21 += 1
        else:
            ham_count += 1
    print("Spam:\t" + str(ham_count))
    print("Ham:\t" + str(b21))
fonk6()
fonk7()