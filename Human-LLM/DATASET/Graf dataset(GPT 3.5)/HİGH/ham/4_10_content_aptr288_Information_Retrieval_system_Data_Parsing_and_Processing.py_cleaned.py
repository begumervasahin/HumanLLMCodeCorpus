import re
from nltk.stem import PorterStemmer
import os
def fonk1(filepathdoc,stopWordList ):
    b1 = PorterStemmer()
    b2 = ""
    b3 = []
    b4 = []
    with open(filepathdoc) as fp:
        b5 = fp.readline()
        a1 = 1
        while b5:
            b6 = b5.strip() + " "
            b2 = b2 + b6
            if "<DOCNO>" in b6:
                b7 = re.search(r'<DOCNO>(.*?)</DOCNO>', b6).group(1)
                b4.append(b7)
                a1 = a1 + 1
            b5 = fp.readline()
    b8 = re.findall(r'<TEXT>(.*?)</TEXT>', b2)
    for x in range(len(b8)):
        b8[x] = str(b8[x]).strip()
        b8[x] = re.sub("\w*-*\d+-*\w*", " ", b8[x])
        b8[x] = re.sub("\d+", " ", b8[x])
        b8[x] = re.sub("\W+", " ", b8[x])
        b9 = b8[x].lower()
        b10 = re.split('\s+', b9)
        for y in range(len(stopWordList)):
            if stopWordList[y] in b10:
                b11 = stopWordList[y]
                b10 = list(filter(lambda x: x != b11, b10))
        b12 = []
        for word in b10:
            b12.append(b1.stem(word))
        b12 = list(filter(None, b12))
        b3 = b3 + b12
    return b3, b4