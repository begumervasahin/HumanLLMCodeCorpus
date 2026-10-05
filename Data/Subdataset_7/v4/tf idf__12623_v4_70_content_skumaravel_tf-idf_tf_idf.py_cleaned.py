import math
import string
def fonk1(corpus, b1, term):
    b1 = b1.lower()
    b2 = set(string.punctuation)
    b1 = ''.join(ch for ch in b1 if ch not in b2)
    b3 = b1.split()
    b4 = len(b3)
    a1 = 0
    for b5 in b3:
        if b5 = = term:
            a1 += 1
    b6 = a1 / b4
    b7 = len(corpus)
    a2 = 0
    for b8 in corpus:
        b8 = b8.lower()
        b8 = ''.join(ch for ch in b8 if ch not in b2)
        b9 = b8.lower().split()
        if term in b9:
            a2 += 1
    if a2 != 0:
        b10 = b7 / a2
        b11 = math.log(b10)
    else:
        b11 = 0
    return b6 * b11