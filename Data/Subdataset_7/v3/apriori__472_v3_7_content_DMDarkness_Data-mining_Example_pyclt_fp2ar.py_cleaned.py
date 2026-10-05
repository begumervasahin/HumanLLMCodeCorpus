
import pyclt
import fp2ar
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
    a1 = 0.03
    a2 = 0.005
    a3 = 0.01
    frequent_patterns, b6 = pyclt.getFP(b5, a1, a2, a3)
    a4 = 0.75
    a5 = 1
    b7 = fp2ar.getAR(frequent_patterns, b6, a4, a5)