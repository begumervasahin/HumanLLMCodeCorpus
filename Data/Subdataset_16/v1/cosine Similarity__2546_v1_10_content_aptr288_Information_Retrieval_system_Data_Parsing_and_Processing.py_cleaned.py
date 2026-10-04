import re
from nltk.stem import PorterStemmer
import os
def fonk1(b13, b14):
    b1 = PorterStemmer()
    b2 = ""
    b3 = []
    b4 = []
    with open(b13, 'r') as file:
        b5 = file.readline()
        while b5:
            b6 = b5.strip() + " "
            b2 += b6
            if "<DOCNO>" in b6:
                b7 = re.search(r'<DOCNO>(.*?)</DOCNO>', b6).group(1)
                b4.append(b7)
            b5 = file.readline()
    b8 = re.findall(r'<TEXT>(.*?)</TEXT>', b2)
    for b12 in b8:
        b9 = fonk2(b12)
        b10 = fonk3(b9, b14)
        b11 = fonk4(b10, b1)
        b3.extend(b11)
    return b3, b4
def fonk2(b12):
    b12 = b12.strip()
    b12 = re.sub(r"\w*-*\d+-*\w*", " ", b12)
    b12 = re.sub(r"\d+", " ", b12)
    b12 = re.sub(r"\W+", " ", b12)
    return b12.lower()
def fonk3(b12, b14):
    b10 = re.split(r'\s+', b12)
    return [word for word in b10 if word not in b14]
def fonk4(b10, stemmer):
    return [stemmer.stem(word) for word in b10 if word]
def fonk5():
    b13 = 'path_to_your_file'
    b14 = ['your', 'stop', 'words', 'here']
    b3, b4 = fonk1(b13, b14)
    print(f"Final Word List: {b3}")
    print(f"Document Numbers: {b4}")
if b15 = = "__main__":
    fonk5()