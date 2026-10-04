import os
import re
b1 = re.compile(r"[a-zA-Z']+(?:-[a-zA-Z']+)?")
def fonk1(text):
    return list(b1.findall(text.lower()))
def fonk2(text, b10):
    b2 = fonk1(text)
    return [word for word in b2 if word not in b10]
def fonk3(directory):
    b3 = {}
    for file in os.listdir(directory):
        b4 = os.path.join(directory, file)
        if os.path.isfile(b4):
            with open(b4, b5 = 'utf-8', errors='ignore') as mail_file:
                b3[file] = fonk1(mail_file.read())
    return b3
def fonk4(directory, b10):
    b3 = {}
    for file in os.listdir(directory):
        b4 = os.path.join(directory, file)
        if os.path.isfile(b4):
            with open(b4, b5 = 'utf-8', errors='ignore') as mail_file:
                b3[file] = fonk2(mail_file.read(), b10)
    return b3
def fonk5(b4):
    with open(b4, b5 = 'utf-8', errors='ignore') as stop_file:
        return fonk1(stop_file.read())
def fonk6(b11):
    b6 = []
    for b2 in b11.values():
        b6.extend(b2)
    return b6
if b7 = = "__main__":
    b8 = "path_to_mails"
    b9 = "path_to_stopwords.txt"
    b10 = fonk5(b9)
    b11 = fonk3(b8)
    b12 = fonk4(b8, b10)
    b13 = fonk6(b11)
    b14 = fonk6(b12)
    print("Mail Dictionary:", b11)
    print("Mail Dictionary Without Stop Words:", b12)
    print("Vocabulary:", b13)
    print("Vocabulary Without Stop Words:", b14)