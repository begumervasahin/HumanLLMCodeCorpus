from cp_otp import strxor
from cp_dictionary import list_of_words
from itertools import combinations
def fonk1(b5):
    b1 = list_of_words(of_length=b5)
    return list(combinations(b1, b2 = 2))
def fonk2():
    b3 = b'\x0b\x0e\x1e\x0b\x17'
    b4 = b'\x15\x0a\x1b\x1d\x01'
    b5 = len(b3)
    b6 = fonk1(b5)
    for pair in b6:
        print(pair)
if b7 = = "__main__":
    fonk2()