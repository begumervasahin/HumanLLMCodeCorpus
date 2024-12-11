import os
import re
b1 = re.compile("[a-zA-Z']+(?:-[a-zA-Z']+)?")
def fonk1(text):
    return b1.findall(text.lower())
def fonk2(text, b7):
    b2 = fonk1(text)
    b3 = [word for word in b2 if word not in b7]
    return b3
def fonk3(directory_path):
    b4 = {}
    for file_name in os.listdir(directory_path):
        b5 = os.path.join(directory_path, file_name)
        with open(b5, b6 = 'utf-8', errors="ignore") as mail_file:
            b4[file_name] = fonk1(mail_file.read())
    return b4
def fonk4(directory_path, b7):
    b4 = {}
    for file_name in os.listdir(directory_path):
        b5 = os.path.join(directory_path, file_name)
        with open(b5, b6 = 'utf-8', errors="ignore") as mail_file:
            b4[file_name] = fonk2(mail_file.read(), b7)
    return b4
def fonk5(b5):
    with open(b5, b6 = 'utf-8', errors="ignore") as stop_file:
        b7 = fonk1(stop_file.read())
        return b7
def fonk6(mail_dict):
    b8 = set()
    for message in mail_dict.values():
        b8.update(message)
    return list(b8)
b9 = "stopwords.txt"
b10 = "mails"
b7 = fonk5(b9)
b11 = fonk3(b10)
b12 = fonk4(b10, b7)
b8 = fonk6(b11)
print("Stop b2:", b7)
print("\nMail dictionary with stop b2:", b11)
print("\nMail dictionary without stop b2:", b12)
print("\nVocabulary:", b8)