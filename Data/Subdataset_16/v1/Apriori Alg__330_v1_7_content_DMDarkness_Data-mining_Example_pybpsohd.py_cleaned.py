
import pybpsohd as pybp
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
b6 = pybp.getFP(b5, 0.00001, 30, 30, 0.5, 1, 1, 10)
for itemset in b6:
    print(itemset)
