import re
from nltk.stem import PorterStemmer
def fonk1(b12, b13):
    b1 = PorterStemmer()
    b2 = ""
    b3 = []
    b4 = []
    with open(b12, 'r') as file:
        for line in file:
            b5 = line.strip() + " "
            b2 += b5
            if "<DOCNO>" in b5:
                b6 = re.search(r'<DOCNO>(.*?)</DOCNO>', b5).group(1)
                b4.append(b6)
    b7 = re.findall(r'<TEXT>(.*?)</TEXT>', b2)
    for b11 in b7:
        b8 = fonk2(b11)
        b9 = fonk3(b8, b13)
        b10 = fonk4(b9, b1)
        b3.extend(b10)
    return b3, b4
def fonk2(b11):
    b11 = b11.strip()
    b11 = re.sub(r"\w*-*\d+-*\w*", " ", b11)
    b11 = re.sub(r"\d+", " ", b11)
    b11 = re.sub(r"\W+", " ", b11)
    return b11.lower()
def fonk3(b11, b13):
    b9 = re.split(r'\s+', b11)
    return [word for word in b9 if word not in b13]
def fonk4(b9, stemmer):
    return [stemmer.stem(word) for word in b9 if word]
def fonk5():
    b12 = 'path_to_your_file'
    b13 = ['your', 'stop', 'words', 'here']
    b3, b4 = fonk1(b12, b13)
    print(f"Final Word List: {b3}")
    print(f"Document Numbers: {b4}")
if b14 = = "__main__":
    fonk5()