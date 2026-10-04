from cp_otp import strxor
from cp_dictionary import list_of_words
from itertools import combinations
b1 = b'\x0b\x0e\x1e\x0b\x17'
b2 = b'\x15\x0a\x1b\x1d\x01'
b3 = list_of_words(of_length=len(b1))
b4 = combinations(b3, r=2)