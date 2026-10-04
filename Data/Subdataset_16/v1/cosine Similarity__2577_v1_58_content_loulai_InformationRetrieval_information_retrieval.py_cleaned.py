import re
from stop_list import closed_class_stop_words
b1 = open("cran.qry", 'r').read()
b1 = b1.replace("\s", "")
def fonk1(string):
    b2 = []
    b3 = re.findall(r"\.I \d{3}", string)
    for match in b3:
        b2.append(match.replace(".I ", ""))
    return b2
def fonk2(string):
    b4 = []
    b3 = re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", string)
    for match in b3:
        b4.append(match.strip())
    return b4
def fonk3(string):
    b5 = re.sub(r"\n|\r", " ", string).split()
    b6 = [word for word in b5 if word not in closed_class_stop_words]
    return b6
def fonk4(array):
    b7 = list(set(array))
    b8 = {term: array.count(term) for term in b7}
    return b8
def fonk5(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
if b9 = = "__main__":
    b4 = fonk2(b1)
    for query in b4:
        print(query)
    b10 = fonk3(open("cran2.qry", 'r').read())
    print(b10)
    b8 = fonk4(b10)
    fonk5(b8)