import math
import string
def fonk1(b9, b1, b10):
    b1 = b1.lower()
    b2 = set(string.punctuation)
    b1 = ''.join(ch for ch in b1 if ch not in b2)
    b3 = b1.split()
    b4 = len(b3)
    b5 = b3.count(b10) / b4
    b6 = len(b9)
    b7 = sum(1 for doc in b9 if b10 in ''.join(ch for ch in doc.lower() if ch not in b2).split())
    if b7 != 0:
        b8 = math.log(b6 / b7)
    else:
        b8 = 0
    return b5 * b8
b9 = [
    "This is a sample b1.",
    "This b1 is another sample b1.",
    "And this is a different b1."
]
b1 = "This is a sample b1."
b10 = "sample"
b11 = fonk1(b9, b1, b10)
print(f"TF-IDF score for b10 '{b10}' in the b1: {b11}")