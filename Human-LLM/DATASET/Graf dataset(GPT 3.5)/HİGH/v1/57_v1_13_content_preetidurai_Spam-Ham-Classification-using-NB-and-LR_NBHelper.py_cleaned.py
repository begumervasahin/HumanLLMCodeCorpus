import os
import re
b1 = re.compile("[a-zA-Z']+(?:-[a-zA-Z']+)?")
def fonk1(text):
    return b1.findall(text.lower())
def fonk2(text, b8):
    b2 = fonk1(text)
    b3 = [word for word in b2 if word not in b8]
    return b3
def fonk3(path):
    b4 = {}
    b5 = os.listdir(path)
    for file in b5:
        b6 = os.path.join(path, file)
        with open(b6, b7 = 'utf-8', errors="ignore") as mail_file:
            b4[file] = fonk1(mail_file.read())
    return b4
def fonk4(path, b8):
    b4 = {}
    b5 = os.listdir(path)
    for file in b5:
        b6 = os.path.join(path, file)
        with open(b6, b7 = 'utf-8', errors="ignore") as mail_file:
            b4[file] = fonk2(mail_file.read(), b8)
    return b4
def fonk5(path):
    with open(path, b7 = 'utf-8', errors="ignore") as stop_file:
        b8 = fonk1(stop_file.read())
        return b8
def fonk6(mail_dict):
    b9 = set()
    for value in mail_dict.values():
        b9.update(value)
    return list(b9)
b10 = "stopwords.txt"
b11 = "mails"
b8 = fonk5(b10)
b12 = fonk3(b11)
b13 = fonk4(b11, b8)
b14 = fonk6(b12)
print("Stop b2:", b8)
print("\nMail dictionary with stop b2:", b12)
print("\nMail dictionary without stop b2:", b13)
print("\nVocabulary:", b14)