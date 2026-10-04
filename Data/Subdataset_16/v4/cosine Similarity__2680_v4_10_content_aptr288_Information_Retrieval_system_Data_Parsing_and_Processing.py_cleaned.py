import re
from nltk.stem import PorterStemmer
def fonk1(b13, b14):
    b1 = PorterStemmer()
    b2 = ""
    b3 = []
    b4 = []
    with open(b13, 'r') as file:
        for line in file:
            b5 = line.strip() + " "
            b2 += b5
            if "<DOCNO>" in b5:
                b6 = re.search(r'<DOCNO>(.*?)</DOCNO>', b5).group(1)
                if b6:
                    b4.append(b6)
    b7 = re.findall(r'<TEXT>(.*?)</TEXT>', b2)
    for b11 in b7:
        b8 = fonk2(b11)
        b9 = fonk3(b8, b14)
        b10 = fonk4(b9, b1)
        b3.extend(b10)
    return b3, b4
def fonk2(b11):
    b11 = b11.strip()
    b11 = re.sub(r'\w*-*\d+-*\w*', ' ', b11)
    b11 = re.sub(r'\d+', ' ', b11)
    b11 = re.sub(r'\W+', ' ', b11)
    return b11.lower()
def fonk3(b11, b14):
    b12 = re.split(r'\s+', b11)
    return [word for word in b12 if word not in b14]
def fonk4(b12, stemmer):
    return [stemmer.stem(word) for word in b12 if word]
def fonk5():
    b13 = 'path_to_your_file'
    b14 = ['your', 'stop', 'b12', 'here']
    b3, b4 = fonk1(b13, b14)
    print(f"Final Word List: {b3}")
    print(f"Document Numbers: {b4}")
if b15 = = "__main__":
    fonk5()