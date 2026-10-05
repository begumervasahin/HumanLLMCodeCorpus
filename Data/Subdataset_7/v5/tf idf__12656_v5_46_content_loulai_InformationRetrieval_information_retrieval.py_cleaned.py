import re
from stop_list import closed_class_stop_words
def fonk1(filename):
    with open(filename, 'r') as file:
        return file.read()
def fonk2(text):
    return text.replace("\s ", "")
def fonk3(text):
    return re.findall(r".I \d{3}", text)
def fonk4(text):
    return re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", text)
def fonk5(string):
    b1 = re.split(r"\s+|\n+|\r+", string)
    b2 = [word for word in b1 if word not in closed_class_stop_words]
    return b2
def fonk6(b1):
    b3 = {}
    for word in b1:
        b3[word] = b3.get(word, 0) + 1
    return b3
def fonk7(dictionary):
    for key, value in dictionary.items():
        print(key, value)
if b4 = = "__main__":
    b5 = fonk1("cran.qry")
    b5 = fonk2(b5)
    b6 = fonk4(b5)
    print(b6)
    b2 = fonk5(fonk1("cran2.qry"))
    print(b2)