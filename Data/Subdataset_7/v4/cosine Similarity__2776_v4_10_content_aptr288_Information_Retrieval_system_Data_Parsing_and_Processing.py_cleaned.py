import re
from nltk.stem import PorterStemmer
def fonk1(filepath, stop_words):
    b1 = PorterStemmer()
    b2 = ""
    b3 = []
    b4 = []
    with open(filepath) as file:
        b5 = file.readline()
        while b5:
            b6 = b5.strip() + " "
            b2 += b6
            if "<DOCNO>" in b6:
                b7 = re.search(r'<DOCNO>(.*?)</DOCNO>', b6).group(1)
                b4.append(b7)
            b5 = file.readline()
    b8 = re.findall(r'<TEXT>(.*?)</TEXT>', b2)
    for b9 in b8:
        b9 = str(b9).strip()
        b9 = re.sub(r'\w*-*\d+-*\w*', " ", b9)
        b9 = re.sub(r'\d+', " ", b9)
        b9 = re.sub(r'\W+', " ", b9)
        b10 = b9.lower()
        b11 = re.split('\s+', b10)
        for stop_word in stop_words:
            if stop_word in b11:
                b11 = list(filter(lambda x: x != stop_word, b11))
        b12 = [b1.stem(word) for word in b11 if word]
        b3.extend(b12)
    return b3, b4