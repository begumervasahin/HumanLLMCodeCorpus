
from Apriori import Apriori
import re
def fonk1():
    b1 = int(input("Minimum support\n"))
    b2 = float(input("Minimum Confidence\n"))
    b3 = int(input("Minimum Length of b10 \n"))
    return b1, b2, b3
def fonk2(b9):
    b4 = [chr(i) for i in range(ord('a'), ord('z')+1)]
    b5 = []
    with open(b9, 'r') as file:
        for b6 in file:
            b6 = b6.strip()
            b6 = re.sub(r"[?\s]", 'a', b6)
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