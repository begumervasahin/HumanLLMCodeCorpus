
import pyarmga as ga
import re
def fonk1(dName):
    with open(dName, 'r') as f:
        b1 = f.readlines()
    b2 = []
    for line in b1:
        b3 = re.split(' |\n', line)
        b4 = [int(item) for item in b3 if item.isdigit()]
        if b4:
            b2.append(b4)
    return b2
b5 = fonk1("kosarak.dat")
b6 = ga.getAR(b5, 0.7, 1, 30, 30, 0.25, 1, 1, 10)
for rule in b6:
    print(rule)