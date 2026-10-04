import os
import re
b1 = re.compile(r"[a-zA-Z']+(?:-[a-zA-Z']+)?")
def fonk1(text):
    return list(b1.findall(text.lower()))
def fonk2(text, b8):
    b2 = list(b1.findall(text.lower()))
    b3 = [word for word in b2 if word not in b8]
    return b3
def fonk3(path):
    b4 = {}
    b5 = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for file in b5:
        b6 = os.path.join(path, file)
        with open(b6, b7 = 'utf-8', errors='ignore') as mailFile:
            b4[file] = fonk1(mailFile.read())
    return b4
def fonk4(path, b8):
    b4 = {}
    b5 = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for file in b5:
        b6 = os.path.join(path, file)
        with open(b6, b7 = 'utf-8', errors='ignore') as mailFile:
            b4[file] = fonk2(mailFile.read(), b8)
    return b4
def fonk5(path):
    with open(path, b7 = 'utf-8', errors='ignore') as stopFile:
        b8 = fonk1(stopFile.read())
    return b8
def fonk6(b13):
    b9 = []
    for value in b13.values():
        b9.extend(value)
    return b9
if b10 = = "__main__":
    b11 = "path_to_mails"
    b12 = "path_to_stopwords.txt"
    b8 = fonk5(b12)
    b13 = fonk3(b11)
    b14 = fonk4(b11, b8)
    b9 = fonk6(b13)
    b15 = fonk6(b14)
    print("Mail Dictionary:", b13)
    print("Mail Dictionary Without Stop Words:", b14)
    print("Vocabulary:", b9)
    print("Vocabulary Without Stop Words:", b15)