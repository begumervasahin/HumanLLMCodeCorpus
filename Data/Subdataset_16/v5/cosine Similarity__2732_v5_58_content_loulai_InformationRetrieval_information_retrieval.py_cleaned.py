import re
from stop_list import closed_class_stop_words
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = file.read()
    return b1.replace(r"\s ", "")
def fonk2(b1):
    return [match.replace(".I ", "") for match in re.findall(r"\.I \d{3}", b1)]
def fonk3(b1):
    b2 = re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", b1)
    return [match.strip() for match in b2]
def fonk4(text):
    b3 = re.sub(r"\n|\r", " ", text).split()
    return [word for word in b3 if word not in closed_class_stop_words]
def fonk5(b3):
    b4 = {word: b3.count(word) for word in set(b3)}
    return b4
def fonk6(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
def fonk7():
    b5 = fonk1("cran.qry")
    b6 = fonk2(b5)
    print("Query Numbers:")
    print(b6)
    b7 = fonk3(b5)
    print("\nExtracted Query Strings:")
    for query in b7:
        print(query)
    with open("cran2.qry", 'r') as file:
        b8 = file.read()
    b9 = fonk4(b8)
    print("\nTrimmed Content:")
    print(b9)
    b4 = fonk5(b9)
    print("\nTerm Frequencies:")
    fonk6(b4)
if b10 = = "__main__":
    fonk7()