import pyarmga as ga
import re
def fonk1(file_name):
    b1 = []
    with open(file_name, 'r') as file:
        for line in file:
            b2 = re.findall(r'\d+', line)
            if b2:
                b1.append([int(item) for item in b2])
    return b1
if b3 = = '__main__':
    b4 = "kosarak.dat"
    b5 = fonk1(b4)
    a1 = 0.7
    a2 = 1
    a3 = 30
    a4 = 30
    a5 = 0.25
    a6 = 1
    a7 = 1
    a8 = 10
    b6 = ga.getAR(b5, a1, a2, a3,
                                  a4, a5, a6,
                                  a7, a8)
    for rule in b6:
        print(rule)