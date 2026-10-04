
import re
from Apriori import Apriori
def fonk1():
    b1 = int(input("Enter minimum support (as an integer): "))
    b2 = float(input("Enter minimum confidence (as a float): "))
    b3 = int(input("Enter minimum length of b10 (as an integer): "))
    return b1, b2, b3
def fonk2(b9):
    b4 = set(chr(i) for i in range(ord('a'), ord('z') + 1))
    b5 = []
    with open(b9, 'r') as file:
        for b6 in file:
            b6 = re.sub(r"[?\s]", 'a', b6.strip())
            b7 = b6.split(',')
            b8 = [item for item in b7 if item in b4]
            b5.append(b8)
    return b5
def fonk3():
    b1, b2, b3 = fonk1()
    b9 = 'datasetUCI.txt'
    b5 = fonk2(b9)
    b10 = Apriori(b5, b1, b2, b3)
    for rule in b10:
        print(rule)
if b11 = = "__main__":
    fonk3()