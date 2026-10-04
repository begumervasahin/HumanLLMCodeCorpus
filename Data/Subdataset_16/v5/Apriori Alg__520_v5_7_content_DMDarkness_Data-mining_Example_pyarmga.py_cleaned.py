
import pyarmga as ga
import re
def fonk1(filename):
    b1 = []
    with open(filename) as file:
        b2 = file.readlines()
        for line in b2:
            b3 = re.split(r'\s+', line.strip())
            b4 = [int(item) for item in b3 if item.isdigit()]
            if b4:
                b1.append(b4)
    return b1
b5 = fonk1("kosarak.dat")
a1 = 0.75
a2 = 1
a3 = 30
a4 = 30
a5 = 0.25
a6 = 1
a7 = 1
a8 = 10
b6 = ga.getAR(
    b5,
    a1,
    a2,
    a3,
    a4,
    a5,
    a6,
    a7,
    a8
)
