import sys
from operator import itemgetter
b1 = []
a1 = 0.0
a2 = 5
for b2 in sys.stdin:
    b2 = b2.strip()
    b3 = b2.split()
    b1.append(b3)
b1 = sorted(b1)
for i in range(a2):
    try:
        a1 += float(b1[i][1])
    except ValueError:
        continue
print a1/a2