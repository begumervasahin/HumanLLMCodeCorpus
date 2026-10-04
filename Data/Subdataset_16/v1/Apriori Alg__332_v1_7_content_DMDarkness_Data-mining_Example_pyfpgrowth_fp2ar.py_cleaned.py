
import pyfpgrowth as pyfp
import fp2ar
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
b6 = pyfp.getFP(b5, 0.01)
b7 = fp2ar.getAR(b6, len(b5), 0.75, 1)
print("Frequent Patterns:")
for pattern in b6:
    print(pattern)
print("\nAssociation Rules:")
for rule in b7:
    print(rule)