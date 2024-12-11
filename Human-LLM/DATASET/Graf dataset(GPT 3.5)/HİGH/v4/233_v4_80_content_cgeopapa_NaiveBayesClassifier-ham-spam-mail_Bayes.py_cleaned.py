from os import listdir
from os.path import isfile, join
import csv
import string
from nltk.corpus import stopwords
def fonk1(filename, b2):
    with open(filename, "w") as file:
        b1 = csv.b1(file)
        for key, val in b2.items():
            b1.writerow([key, val])
def fonk2(filename):
    b2 = {}
    with open(filename, b3 = 'r') as file:
        b4 = csv.b4(file)
        for row in b4:
            if len(row) == 2:
                b2[row[0]] = float(row[1])
    return b2
def fonk3(b5):
    b5 = b5.lower()
    b6 = dict.fromkeys(map(ord, string.punctuation + '\0'), None)
    b5 = b5.translate(b6)
    b7 = set(stopwords.words('english'))
    b7.add("subject")
    b5 = b5.replace('\n', ' ')
    b8 = b5.split(' ')
    b8 = [word for word in b8 if word not in b7]
    return b8
def fonk4(filename):
    b9 = [f for f in listdir(filename) if isfile(join(filename, f))]
    b2 = {}
    a1 = 0
    for file in b9:
        with open(join(filename, file), b10 = "ignore") as f:
            b5 = f.read()
            b8 = fonk3(b5)
            a1 += len(b8)
            for word in b8:
                if word in b2:
                    b2[word] += 1
                else:
                    b2[word] = 1
    b11 = len(b9)
    for word in b2:
        b2[word] = float(b2[word]) / a1
    b2["fileCount"] = b11
    return b2
def fonk5(b12, b2, priori):
    b12 = fonk3(b12)
    a2 = 1
    for word in b12:
        if word in b2:
            a2 *= b2[word]
        else:
            a2 *= 1 / (b2["fileCount"] + len(b2) + 1)
    a2 *= priori
    return a2
def fonk6():
    b13 = fonk4("spam")
    b14 = fonk4("ham")
    fonk1("spam_train_results.csv", b13)
    fonk1("ham_train_results.csv", b14)
def fonk7():
    b14 = fonk2("ham_train_results.csv")
    b13 = fonk2("spam_train_results.csv")
    b9 = [f for f in listdir("input") if isfile(join("input", f))]
    b15 = ham_count = 0
    for file in b9:
        with open(join("input", file), b10 = "ignore") as f:
            b5 = f.read()
            b16 = fonk5(b5, b14, 0.67)
            b17 = fonk5(b5, b13, 0.33)
            if b16 <= b17:
                b15 += 1
            else:
                ham_count += 1
    print("Spam:\t" + str(ham_count))
    print("Ham:\t" + str(b15))
fonk6()
fonk7()