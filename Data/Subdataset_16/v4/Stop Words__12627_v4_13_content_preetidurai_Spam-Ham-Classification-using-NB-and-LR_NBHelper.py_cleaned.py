import os
import re
b1 = re.compile(r"[a-zA-Z']+(?:-[a-zA-Z']+)?")
def fonk1(text):
    return b1.findall(text.lower())
def fonk2(text, stop_words):
    b2 = b1.findall(text.lower())
    return [word for word in b2 if word not in stop_words]
def fonk3(path):
    b3 = {}
    for root, _, files in os.walk(path):
        for file in files:
            b4 = os.path.join(root, file)
            with open(b4, b5 = 'utf-8', errors='ignore') as mail_file:
                b3[file] = fonk1(mail_file.read())
    return b3
def fonk4(path, stop_words):
    b3 = {}
    for root, _, files in os.walk(path):
        for file in files:
            b4 = os.path.join(root, file)
            with open(b4, b5 = 'utf-8', errors='ignore') as mail_file:
                b3[file] = fonk2(mail_file.read(), stop_words)
    return b3
def fonk5(path):
    with open(path, b5 = 'utf-8', errors='ignore') as stop_file:
        return fonk1(stop_file.read())
def fonk6(mail_dict):
    b6 = []
    for b2 in mail_dict.values():
        b6.extend(b2)
    return b6