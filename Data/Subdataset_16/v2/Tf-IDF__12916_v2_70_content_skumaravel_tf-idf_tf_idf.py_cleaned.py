import math
import string
def fonk1(b1):
    b1 = b1.lower()
    b2 = set(string.punctuation)
    b1 = ''.join(ch for ch in b1 if ch not in b2)
    return b1
def fonk2(b1, b10):
    b3 = b1.split()
    b4 = len(b3)
    b5 = b3.count(b10)
    b6 = b5 / b4
    return b6
def fonk3(b12, b10):
    b7 = len(b12)
    b8 = sum(1 for doc in b12 if b10 in fonk1(doc).split())
    if b8 > 0:
        b9 = math.log(b7 / b8)
    else:
        b9 = 0
    return b9
def fonk4(b12, b1, b10):
    b1 = fonk1(b1)
    b10 = b10.lower()
    b6 = fonk2(b1, b10)
    b9 = fonk3(b12, b10)
    return b6 * b9
if b11 = = "__main__":
    b12 = [
        "This is a sample b1.",
        "This b1 is another example b1.",
        "And this is a different b1."
    ]
    b1 = "This b1 is a sample b1."
    b10 = "b1"
    b13 = fonk4(b12, b1, b10)
    print(f"The TF-IDF score for the b10 '{b10}' is: {b13}")