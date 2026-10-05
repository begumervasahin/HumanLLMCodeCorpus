import re
from nltk.stem import PorterStemmer
def fonk1(filepath, stop_words):
    b1 = PorterStemmer()
    b2 = ""
    b3 = []
    b4 = []
    with open(filepath) as file:
        for line in file:
            b5 = line.strip() + " "
            b2 += b5
            if "<DOCNO>" in b5:
                b6 = re.search(r'<DOCNO>(.*?)</DOCNO>', b5).group(1)
                b4.append(b6)
    b7 = re.findall(r'<TEXT>(.*?)</TEXT>', b2)
    for b8 in b7:
        b8 = str(b8).strip()
        b8 = re.sub(r'\w*-*\d+-*\w*', " ", b8)
        b8 = re.sub(r'\d+', " ", b8)
        b8 = re.sub(r'\W+', " ", b8)
        b9 = b8.lower()
        b10 = re.split('\s+', b9)
        b10 = [word for word in b10 if word not in stop_words]
        b11 = [b1.stem(word) for word in b10 if word]
        b3.extend(b11)
    return b3, b4