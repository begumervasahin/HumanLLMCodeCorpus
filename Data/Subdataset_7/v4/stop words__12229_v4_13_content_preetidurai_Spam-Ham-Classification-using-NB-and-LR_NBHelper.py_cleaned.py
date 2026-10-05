import os
import re
b1 = re.compile("[a-zA-Z']+(?:-[a-zA-Z']+)?")
def fonk1(text):
    return list(b1.findall(text.lower()))
def fonk2(text, b8):
    b2 = list(b1.findall(text.lower()))
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
    b9 = []
    for key, value in mail_dict.items():
        b9.extend(value)
    return b9