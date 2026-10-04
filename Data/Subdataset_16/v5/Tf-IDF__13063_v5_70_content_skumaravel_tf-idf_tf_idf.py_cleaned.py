import math
import string
def fonk1(b1):
    b1 = b1.lower()
    b2 = set(string.punctuation)
    return ''.join(ch for ch in b1 if ch not in b2)
def fonk2(b12, b13):
    b3 = b12.count(b13)
    b4 = len(b12)
    return b3 / b4
def fonk3(b11, b13):
    b5 = sum(1 for doc in b11 if b13 in doc)
    b6 = len(b11)
    if b5 > 0:
        return math.log(b6 / b5)
    else:
        return 0
def fonk4(b11, b12, b13):
    b7 = [fonk1(doc).split() for doc in b11]
    b8 = fonk1(b12).split()
    b9 = fonk2(b8, b13)
    b10 = fonk3(b7, b13)
    return b9 * b10
b11 = [
    "This is a sample b12.",
    "This b12 is another sample b12.",
    "And this is a different b12."
]
b12 = "This is a sample b12."
b13 = "sample"
b14 = fonk4(b11, b12, b13)
print(f"TF-IDF score for b13 '{b13}' in the b12: {b14}")