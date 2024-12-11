import os
import re
b1 = re.compile(r"[a-zA-Z']+(?:-[a-zA-Z']+)?")
def fonk1(text):
    return b1.findall(text.lower())
def fonk2(text, stop_words):
    b2 = fonk1(text)
    return [word for word in b2 if word not in stop_words]
def fonk3(path):
    b3 = {}
    for file_name in os.listdir(path):
        b4 = os.path.join(path, file_name)
        with open(b4, b5 = 'utf-8', errors="ignore") as mail_file:
            b3[file_name] = fonk1(mail_file.read())
    return b3
def fonk4(path, stop_words):
    b3 = {}
    for file_name in os.listdir(path):
        b4 = os.path.join(path, file_name)
        with open(b4, b5 = 'utf-8', errors="ignore") as mail_file:
            b3[file_name] = fonk2(mail_file.read(), stop_words)
    return b3
def fonk5(path):
    with open(path, b5 = 'utf-8', errors="ignore") as stop_file:
        return fonk1(stop_file.read())
def fonk6(mail_dict):
    return [word for b2 in mail_dict.values() for word in b2]