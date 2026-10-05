import re
from stop_list import closed_class_stop_words
def fonk1(text):
    return re.findall(r"\.I (\d{3})", text)
def fonk2(text):
    return re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", text)
def fonk3(text):
    b1 = re.sub(r"\n|\r", " ", text).split(" ")
    return [word for word in b1 if word.lower() not in closed_class_stop_words]
def fonk4(b1):
    b2 = {}
    for word in b1:
        b2[word] = b2.get(word, 0) + 1
    return b2
def fonk5(dictionary):
    for key, value in dictionary.items():
        print(key, value)
b3 = open("cran.qry", 'r').read().replace("\s ", "")
b4 = fonk2(b3)
for i, query_string in enumerate(b4, 1):
    print(f"Query {i}:")
    print(fonk3(query_string))
    print()
print("Term Frequencies:")
b5 = open("cran2.qry", 'r').read()
b6 = fonk3(b5)
b7 = fonk4(b6)
fonk5(b7)