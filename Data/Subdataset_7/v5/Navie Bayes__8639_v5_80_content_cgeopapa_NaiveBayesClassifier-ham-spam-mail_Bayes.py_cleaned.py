import csv
import string
from os import listdir
from os.path import isfile, join
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
    b7 = set(stopwords.b8('english'))
    b7.add("subject")
    b5 = b5.replace('\n', ' ')
    b8 = b5.split(' ')
    b8 = [word for word in b8 if word not in b7]
    return b8
def fonk4(directory):
    b9 = [f for f in listdir(directory) if isfile(join(directory, f))]
    b10 = {}
    a1 = 0
    for file in b9:
        with open(join(directory, file), b11 = "ignore") as f:
            b5 = f.read()
            b8 = fonk3(b5)
            a1 += len(b8)
            for word in b8:
                b10[word] = b10.get(word, 0) + 1
    b10 = {word: freq / a1 for word, freq in b10.items()}
    b10["fileCount"] = len(b9)
    return b10
def fonk5(input_text, b10, priori):
    b8 = fonk3(input_text)
    a2 = 1
    for word in b8:
        a2 *= b10.get(word, 1 / (b10["fileCount"] + len(b10) + 1))
    a2 *= priori
    return a2
def fonk6():
    b12 = fonk4("spam")
    b13 = fonk4("ham")
    fonk1("spam_train_results.csv", b12)
    fonk1("ham_train_results.csv", b13)
    b13 = fonk2("ham_train_results.csv")
    b12 = fonk2("spam_train_results.csv")
    b14 = ham_count = 0
    b9 = [f for f in listdir("input") if isfile(join("input", f))]
    for file in b9:
        with open(join("input", file), b11 = "ignore") as f:
            b5 = f.read()
            b15 = fonk5(b5, b13, 0.67)
            b16 = fonk5(b5, b12, 0.33)
            if b15 <= b16:
                b14 += 1
            else:
                ham_count += 1
    print("Spam:\t" + str(ham_count))
    print("Ham:\t" + str(b14))
fonk6()