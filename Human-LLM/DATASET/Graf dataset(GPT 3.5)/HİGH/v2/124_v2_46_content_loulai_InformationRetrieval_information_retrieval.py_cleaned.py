import re
from stop_list import closed_class_stop_words
def fonk1(string):
    b1 = []
    b2 = re.findall(r".I \d{3}", string)
    for match in b2:
        b1.append(match.replace(".I ", ""))
    return b1
def fonk2(string):
    b3 = []
    b2 = re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", string)
    for match in b2:
        b3.append(match)
    return b3
def fonk3(string):
    b4 = filter(None, re.sub(r"\n|\r", " ", string).split(" "))
    b5 = closed_class_stop_words
    for stop_word in b5:
        while stop_word in b4:
            b4.remove(stop_word)
    return b4
def fonk4(array):
    b6 = list(set(array))
    b7 = dict.fromkeys(b6, 0)
    for word in array:
        b7[word] += 1
    return b7
def fonk5(dictionary):
    for key, value in dictionary.items():
        print(key, value)
b8 = open("cran.qry", 'r').read()
b8.replace("\s ", "")
b3 = fonk2(b8)
for i, query_string in enumerate(b3):
    print(f"Query {i+1}:")
    print(fonk3(query_string))
    print()
print("Term Frequencies:")
b9 = open("cran2.qry", 'r').read()
b10 = fonk3(b9)
b11 = fonk4(b10)
fonk5(b11)