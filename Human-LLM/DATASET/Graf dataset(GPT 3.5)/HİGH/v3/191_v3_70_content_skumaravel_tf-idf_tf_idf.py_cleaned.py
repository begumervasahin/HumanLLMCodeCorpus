import math
import string
def fonk1(b1):
    b1 = b1.lower()
    b2 = set(string.punctuation)
    b1 = ''.join(ch for ch in b1 if ch not in b2)
    return b1
def fonk2(term_count, total_terms):
    return term_count / total_terms
def fonk3(b8, total_docs):
    if b8 != 0:
        return math.log(total_docs / b8)
    else:
        return 0
def fonk4(b6, b9):
    return b6 * b9
def fonk5(b11, b1, b12):
    b1 = fonk1(b1)
    b3 = b1.split()
    b4 = len(b3)
    b5 = b3.count(b12)
    b6 = fonk2(b5, b4)
    b7 = len(b11)
    b8 = sum(1 for doc in b11 if b12 in fonk1(doc).split())
    b9 = fonk3(b8, b7)
    b10 = fonk4(b6, b9)
    return b10
b11 = [
    "This is the first b1.",
    "This b1 is the second b1.",
    "And this is the third one.",
    "Is this the first b1?",
]
b1 = "This is the first b1."
b12 = "b1"
print("TF-IDF Score:", fonk5(b11, b1, b12))