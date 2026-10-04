import re
from stop_list import closed_class_stop_words
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return file.read().replace(r"\s", "")
def fonk2(content):
    return [match.replace(".I ", "") for match in re.findall(r"\.I \d{3}", content)]
def fonk3(content):
    return [match.strip() for match in re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", content)]
def fonk4(text):
    b1 = re.sub(r"\n|\r", " ", text).split()
    return [word for word in b1 if word not in closed_class_stop_words]
def fonk5(b1):
    return {word: b1.count(word) for word in set(b1)}
def fonk6(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
def fonk7():
    b2 = fonk1("cran.qry")
    b3 = fonk3(b2)
    print("Extracted Query Strings:")
    for query in b3:
        print(query)
    with open("cran2.qry", 'r') as file:
        b4 = file.read()
    b5 = fonk4(b4)
    print("\nTrimmed Content:")
    print(b5)
    b6 = fonk5(b5)
    print("\nTerm Frequencies:")
    fonk6(b6)
if b7 = = "__main__":
    fonk7()