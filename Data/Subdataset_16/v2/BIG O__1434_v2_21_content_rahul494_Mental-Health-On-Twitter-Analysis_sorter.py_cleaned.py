import sys
import operator
def fonk1():
    b1 = {}
    for line in sys.stdin:
        value, b2 = line.split()
        b1[b2] = int(value)
    b3 = sorted(b1.items(), b2=operator.itemgetter(1), reverse=True)
    for b2, value in b3:
        print(f"{b2},{value}")
if b4 = = "__main__":
    fonk1()