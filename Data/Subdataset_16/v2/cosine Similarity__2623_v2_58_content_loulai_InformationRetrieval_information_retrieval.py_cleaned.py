import re
from stop_list import closed_class_stop_words
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return file.read().replace(r"\s", "")
def fonk2(string):
    return [match.replace(".I ", "") for match in re.findall(r"\.I \d{3}", string)]
def fonk3(string):
    return [match.strip() for match in re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", string)]
def fonk4(string):
    b1 = re.sub(r"\n|\r", " ", string).split()
    return [word for word in b1 if word not in closed_class_stop_words]
def fonk5(b1):
    return {word: b1.count(word) for word in set(b1)}
def fonk6(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
if b2 = = "__main__":
    b3 = fonk1("cran.qry")
    b4 = fonk3(b3)
    for query in b4:
        print(query)
    b5 = fonk4(open("cran2.qry", 'r').read())
    print(b5)
    b6 = fonk5(b5)
    fonk6(b6)