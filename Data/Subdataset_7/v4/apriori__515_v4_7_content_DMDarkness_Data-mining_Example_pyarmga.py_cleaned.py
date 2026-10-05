
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
    b6 = ga.getAR(b5, 0.7, 1, 30, 30, 0.25, 1, 1, 10)
    for rule in b6:
        print(rule)