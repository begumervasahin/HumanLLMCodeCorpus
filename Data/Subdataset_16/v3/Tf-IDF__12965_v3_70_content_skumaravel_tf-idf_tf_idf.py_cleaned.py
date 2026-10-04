import math
import string
def fonk1(b1):
    b1 = b1.lower()
    b2 = set(string.punctuation)
    return ''.join(ch for ch in b1 if ch not in b2)
def fonk2(b1, b12):
    b3 = b1.split()
    b4 = b3.count(b12)
    return b4 / len(b3)
def fonk3(b11, b12):
    b5 = sum(1 for doc in b11 if b12 in fonk1(doc).split())
    if b5 = = 0:
        return 0
    return math.log(len(b11) / b5)
def fonk4(b11, b1, b12):
    b6 = fonk1(b1)
    b7 = b12.lower()
    b8 = fonk2(b6, b7)
    b9 = fonk3(b11, b7)
    return b8 * b9
if b10 = = "__main__":
    b11 = [
        "This is a sample b1.",
        "This b1 is another example b1.",
        "And this is a different b1."
    ]
    b1 = "This b1 is a sample b1."
    b12 = "b1"
    b13 = fonk4(b11, b1, b12)
    print(f"The TF-IDF score for the b12 '{b12}' is: {b13}")