import sys
import csv
import operator
def fonk1():
    b1 = {}
    for line in sys.stdin:
        value, b2 = line.split()
        b1[b2] = int(value)
    return b1
def fonk2(b1):
    return sorted(b1.items(), b2 = operator.itemgetter(1), reverse=True)
def fonk3(b3):
    for b2, value in b3:
        print(f"{b2},{value}")
def fonk4():
    b1 = fonk1()
    b3 = fonk2(b1)
    fonk3(b3)
if b4 = = "__main__":
    fonk4()