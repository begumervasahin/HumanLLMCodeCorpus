from cp_otp import strxor
from cp_dictionary import list_of_words
from itertools import combinations
c1 = b'\x0b\x0e\x1e\x0b\x17'
c2 = b'\x15\x0a\x1b\x1d\x01'
words = list_of_words(of_length=len(c1))
pairs = combinations(words, r=2)