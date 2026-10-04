from cp_otp import strxor
from cp_dictionary import list_of_words
from itertools import combinations
b1 = b'\x0b\x0e\x1e\x0b\x17'
b2 = b'\x15\x0a\x1b\x1d\x01'
b3 = len(b1)
b4 = list_of_words(of_length=b3)
b5 = combinations(b4, r=2)
for pair in b5:
    print(pair)