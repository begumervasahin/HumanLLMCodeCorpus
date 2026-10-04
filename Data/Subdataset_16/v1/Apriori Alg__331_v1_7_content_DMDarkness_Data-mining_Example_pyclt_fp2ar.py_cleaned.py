
import pyclt
import fp2ar
import re
def fonk1(dName):
    with open(dName, 'r') as f:
        b1 = []
        b2 = f.readlines()
        for line in b2:
            b3 = re.split(' |\n', line)
            b4 = [int(item) for item in b3 if item.isdigit()]
            if len(b4) > 0:
                b1.append(b4)
    return b1
b5 = fonk1("kosarak.dat")
fi, b6 = pyclt.getFP(b5, 0.03, 0.005, 0.01)
b7 = fp2ar.getAR(fi, b6, 0.75, 1)
for rule in b7:
    print(rule)