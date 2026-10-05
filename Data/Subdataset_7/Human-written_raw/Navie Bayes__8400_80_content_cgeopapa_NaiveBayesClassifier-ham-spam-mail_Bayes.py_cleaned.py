from os import listdir
from os.path import isfile, join
import csv
import string
from nltk.corpus import stopwords
def fonk1(filename, b10):
    b1 = csv.writer(open(filename, "b1"))
    for key, val in b10.items():
        b1.writerow([key, val])
def fonk2(filename):
    b2 = {}
    with open(filename, b3 = 'r') as infile:
        b4 = csv.b4(infile)
        for rows in b4:
            if len(rows) == 2:
                b2[rows[0]] = float(rows[1])
    return b2
def fonk3(b5):
    b5 = b5.lower()
    b6 = dict.fromkeys(map(ord, string.punctuation + '\0'), None)
    b7 = set(stopwords.words('english'))
    b7.add("subject")
    b5 = b5.replace('\n', ' ')
    b5 = b5.translate(b6)
    b8 = b5.split(' ')
    b8 = [word for word in b8 if word not in b7]
    return b8
def fonk4(filename):
    b9 = [f for f in listdir(filename) if isfile(join(filename, f))]
    b10 = {}
    a1 = 0
    for b11 in b9:
        b11 = open(filename + "/" + b11, errors="ignore")
        b5 = b11.read()
        b11.close()
        b8 = fonk3(b5)
        for word in b8:
            a1 += 1
            if word in b10:
                b10[word] += 1
            else:
                b10[word] = 1
    b12 = len(b9)
    for word in b10.keys():
        b10[word] = float(b10[word]) / b12
    b10["b12"] = b12
    return b10
def fonk5(b13, diction, priori):
    b13 = fonk3(b13)
    a2 = 1
    for word in b13:
        if word in diction.keys():
            a2 *= diction[word]
        else:
            a2 *= 1/diction["b12"]+len(diction)+1
    a2 *= priori
    return a2
def fonk6():
    fonk1("spam_train_results.csv", fonk4("b18"))
    fonk1("ham_train_results.csv", fonk4("b17"))
def fonk7():
    b14 = fonk2("ham_train_results.csv")
    b15 = fonk2("spam_train_results.csv")
    b9 = [f for f in listdir("b13") if isfile(join("b13", f))]
    b16 = hamC = 0
    for b11 in b9:
        b11 = open("b13" + "/" + b11, errors = "ignore")
        b5 = b11.read()
        b11.close()
        b17 = fonk5(b5, b14, 0.67)
        b18 = fonk5(b5, b15, 0.33)
        if b17 <= b18:
            b16 += 1
        else:
            hamC += 1
    print("Spam:\t" + str(hamC))
    print("Ham:\t" + str(b16))
fonk6()
fonk7()