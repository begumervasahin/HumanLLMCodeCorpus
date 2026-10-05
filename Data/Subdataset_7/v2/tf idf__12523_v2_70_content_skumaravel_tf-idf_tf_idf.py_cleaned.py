import math
import string
def fonk1(b12, b1, b13):
    b1 = b1.lower()
    b2 = set(string.punctuation)
    b1 = ''.join(ch for ch in b1 if ch not in b2)
    b3 = b1.split()
    b4 = len(b3)
    b5 = b3.count(b13)
    b6 = b5 / b4
    b7 = len(b12)
    b8 = sum(1 for doc in b12 if b13 in doc.lower().split())
    if b8 != 0:
        b9 = b7 / b8
        b10 = math.log(b9)
    else:
        b10 = 0
    b11 = b6 * b10
    return b11
b12 = [
    "This is the first b1.",
    "This b1 is the second b1.",
    "And this is the third one.",
    "Is this the first b1?",
]
b1 = "This is the first b1."
b13 = "b1"
print("TF-IDF Score:", fonk1(b12, b1, b13))