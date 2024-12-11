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
    b9 = b6.translate(b7).split(' ')
    b9 = [word for word in b9 if word not in b8]
    return b9
def fonk4(directory):
    b10 = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    b11 = {}
    a1 = 0
    for file in b10:
        with open(os.path.join(directory, file), b12 = "ignore") as f:
            b6 = f.read()
        b9 = fonk3(b6)
        for word in b9:
            a1 += 1
            b11[word] = b11.get(word, 0) + 1
    b13 = len(b10)
    for word in b11.keys():
        b11[word] = float(b11[word]) / b13
    b11["fileCount"] = b13
    return b11
def fonk5(input_text, b11, prior_probability):
    b14 = fonk3(input_text)
    a2 = 1
    for word in b14:
        if word in b11:
            a2 *= b11[word]
        else:
            a2 *= 1 / (b11["fileCount"] + len(b11) + 1)
    a2 *= prior_probability
    return a2
def fonk6():
    b15 = fonk4("spam")
    b16 = fonk4("ham")
    fonk1("spam_train_results.csv", b15)
    fonk1("ham_train_results.csv", b16)
def fonk7():
    b17 = fonk2("ham_train_results.csv")
    b18 = fonk2("spam_train_results.csv")
    b19 = [f for f in os.listdir("input") if os.path.isfile(os.path.join("input", f))]
    b20 = ham_count = 0
    for file in b19:
        with open(os.path.join("input", file), b12 = "ignore") as f:
            b6 = f.read()
        b21 = fonk5(b6, b17, 0.67)
        b22 = fonk5(b6, b18, 0.33)
        if b21 <= b22:
            b20 += 1
        else:
            ham_count += 1
    print("Spam:\t" + str(ham_count))
    print("Ham:\t" + str(b20))
fonk6()
fonk7()