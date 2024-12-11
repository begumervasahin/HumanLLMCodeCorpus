import re
from nltk.stem import PorterStemmer
def fonk1(filepath, b12):
    b1 = PorterStemmer()
    b2 = ""
    b3 = []
    b4 = []
    with open(filepath) as file:
        b5 = file.readlines()
    for line in b5:
        b6 = line.strip() + " "
        b2 += b6
        if "<DOCNO>" in b6:
            b7 = re.search(r'<DOCNO>(.*?)</DOCNO>', b6).group(1)
            b4.append(b7)
    b8 = re.findall(r'<TEXT>(.*?)</TEXT>', b2)
    for b9 in b8:
        b9 = re.sub(r'\W+|\d+', ' ', b9).lower()
        b10 = b9.split()
        b10 = [word for word in b10 if word not in b12]
        b11 = [b1.stem(word) for word in b10 if word]
        b3.extend(b11)
    return b3, b4
b12 = ["the", "and", "is", "in", "it", "on"]
b13 = "sample.txt"
final_words, b14 = fonk1(b13, b12)
print("Final Word List:", final_words)
print("Doc Number List For Each File:", b14)