import re
from stop_list import closed_class_stop_words
b1 = open("cran.qry", 'r')
b2 = b1.read()
b1.close()
b2 = b2.replace("\s ", "")
def fonk1(string):
    b3 = []
    b4 = re.findall(r".I \d{3}", string)
    for match in b4:
        b3.append(match.replace(".I ", ""))
    return b3
def fonk2(string):
    b5 = []
    b4 = re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", string)
    for match in b4:
        b5.append(match)
    return b5
b5 = fonk2(b2)
print(b5)
def fonk3(string):
    b6 = filter(None, (re.sub(r"\n|\r", " ", string)).split(" "))
    b7 = closed_class_stop_words
    for stop_word in b7:
        while stop_word in b6:
            b6.remove(stop_word)
    return b6
def fonk4(array):
    b8 = list(set(array))
    b9 = dict.fromkeys(b8, 0)
    for word in array:
        b9[word] = b9[word] + 1
    return b9
def fonk5(dictionary):
    for key, value in dictionary.items():
        print(key, value)
b6 = fonk3(open("cran2.qry", 'r').read())
print(b6)