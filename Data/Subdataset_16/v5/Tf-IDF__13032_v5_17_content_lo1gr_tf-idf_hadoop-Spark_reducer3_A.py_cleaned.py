import sys
from math import log10
a1 = 10.0
b1 = None
b2 = {}
b3 = []
def fonk1(word, b8, b9, n, N):
    b4 = f"{n} {N} {b8}"
    b2[word] = b4
    b3.append(f"{word} {b9}")
for b5 in sys.stdin:
    b5 = b5.strip()
    word, b6 = b5.split('\t', 1)
    b9, n, N, b7 = b6.split(' ', 3)
    if b1 = = word:
        b8 += int(b7)
    else:
        if b1 is not None:
            fonk1(b1, b8, b9, n, N)
        b8 = int(b7)
        b1 = word
if b1 is not None:
    fonk1(b1, b8, b9, n, N)
for item in b3:
    word, b9 = item.split(' ', 1)
    if word in b2:
        n, N, b10 = b2[word].split(' ', 2)
        n, N, b10 = float(n), float(N), float(b10)
        b11 = (n / N) * log10(a1 / b10)
        print(f'{item}\t{b11}')