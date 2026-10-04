import re
from stop_list import closed_class_stop_words
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return file.read().replace(r"\s ", "")
def fonk2(content):
    return [match.replace(".I ", "") for match in re.findall(r"\.I \d{3}", content)]
def fonk3(content):
    b1 = re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", content)
    return [match.strip() for match in b1]
def fonk4(text):
    b2 = re.sub(r"\n|\r", " ", text).split()
    return [word for word in b2 if word not in closed_class_stop_words]
def fonk5(b2):
    b3 = {word: b2.count(word) for word in set(b2)}
    return b3
def fonk6(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
def fonk7():
    b4 = fonk1("cran.qry")
    b5 = fonk2(b4)
    print("Query Numbers:")
    print(b5)
    b6 = fonk3(b4)
    print("\nExtracted Query Strings:")
    for query in b6:
        print(query)
    with open("cran2.qry", 'r') as file:
        b7 = file.read()
    b8 = fonk4(b7)
    print("\nTrimmed Content:")
    print(b8)
    b3 = fonk5(b8)
    print("\nTerm Frequencies:")
    fonk6(b3)
if b9 = = "__main__":
    fonk7()