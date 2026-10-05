import math
import string
def fonk1(b1):
    b1 = b1.lower()
    b2 = set(string.punctuation)
    b1 = ''.join(ch for ch in b1 if ch not in b2)
    return b1
def fonk2(b9, term):
    b3 = len(b9)
    b4 = b9.count(term)
    b5 = b4 / b3
    return b5
def fonk3(corpus, term):
    b6 = len(corpus)
    b7 = sum(1 for doc in corpus if term in doc)
    if b7 != 0:
        b8 = math.log(b6 / b7)
    else:
        b8 = 0
    return b8
def fonk4(corpus, b1, term):
    b1 = fonk1(b1)
    b9 = b1.split()
    b5 = fonk2(b9, term)
    b8 = fonk3(corpus, term)
    return b5 * b8