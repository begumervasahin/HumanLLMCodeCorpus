import re
from nltk.stem import PorterStemmer
def fonk1(b14, b13):
    b1 = PorterStemmer()
    b2 = ""
    b3 = []
    b4 = []
    with open(b14) as fp:
        b5 = fp.readlines()
    for line in b5:
        b6 = line.strip() + " "
        b2 = b2 + b6
        if "<DOCNO>" in b6:
            b7 = re.search(r'<DOCNO>(.*?)</DOCNO>', b6).group(1)
            b4.append(b7)
    b8 = re.findall(r'<TEXT>(.*?)</TEXT>', b2)
    for b9 in b8:
        b9 = str(b9).strip()
        b9 = re.sub("\w*-*\d+-*\w*", " ", b9)
        b9 = re.sub("\d+", " ", b9)
        b9 = re.sub("\W+", " ", b9)
        b10 = b9.lower()
        b11 = re.split('\s+', b10)
        for stopWord in b13:
            if stopWord in b11:
                b11 = [word for word in b11 if word != stopWord]
        b12 = [b1.stem(word) for word in b11 if word]
        b3.extend(b12)
    return b3, b4
b13 = ["the", "and", "is", "in", "it", "on"]
b14 = "sample.txt"
final_word_list, b15 = fonk1(b14, b13)
print("Final Word List:", final_word_list)
print("Doc Number List For Each File:", b15)