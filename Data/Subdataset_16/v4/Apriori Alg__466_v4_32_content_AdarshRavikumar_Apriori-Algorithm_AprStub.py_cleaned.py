
import re
from Apriori import Apriori
def fonk1(file_path):
    b1 = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    b2 = []
    with open(file_path, 'r') as file:
        for line in file:
            b3 = re.sub(r"[?\s]", 'a', line.strip())
            b4 = [item for item in b3.split(',') if item in b1]
            b2.append(b4)
    return b2
def fonk2():
    b5 = int(input("Minimum support: "))
    b6 = float(input("Minimum confidence: "))
    b7 = int(input("Minimum length of rules: "))
    b8 = 'datasetUCI.txt'
    b2 = fonk1(b8)
    b9 = Apriori(b2, b5, b6, b7)
if b10 = = "__main__":
    fonk2()