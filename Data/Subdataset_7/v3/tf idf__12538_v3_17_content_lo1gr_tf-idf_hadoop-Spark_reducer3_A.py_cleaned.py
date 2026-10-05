import sys
from math import log10
b1 = None
a1 = 1
b2 = None
b3 = {}
b4 = []
a2 = 10.0
for b5 in sys.stdin:
    b5 = b5.strip()
    b2, b6 = b5.split('\t', 1)
    b8, n, N, b7 = b6.split(' ', 3)
    if b1 = = b2:
        a1 += int(b7)
    else:
        if b1 is not None:
            b3[b1] = f"{n} {N} {a1}"
            b4.append(f"{b1} {b8}")
        a1 = 1
        b1 = b2
if b1 is not None:
    b3[b1] = f"{n} {N} {a1}"
    b4.append(f"{b1} {b8}")
for pair in b4:
    b2, b8 = pair.split(' ', 1)
    n, N, b9 = b3[b2].split(' ', 2)
    n, N, b9 = float(n), float(N), float(b9)
    b10 = (n / N) * log10(a2 / b9)
    print(f"{pair}\t{b10}")