
import pyfpgrowth as pyfp
import fp2ar
import re
def fonk1(filename):
    b1 = []
    with open(filename) as file:
        b2 = file.readlines()
        for line in b2:
            b3 = re.split(' |\n', line)
            b4 = [int(item) for item in b3 if item.isdigit()]
            if b4:
                b1.append(b4)
    return b1
b5 = fonk1("kosarak.dat")
a1 = 0.01
b6 = pyfp.getFP(b5, a1)
a2 = 0.75
a3 = 1
b7 = fp2ar.getAR(b6, len(b5), a2, a3)
