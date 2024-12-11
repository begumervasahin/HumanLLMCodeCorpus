import pyarmga as genetic_algorithm
import re
def fonk1(file_name):
    b1 = []
    with open(file_name, 'r') as file:
        for line in file:
            b2 = re.findall(r'\d+', line)
            if b2:
                b1.append([int(item) for item in b2])
    return b1
def fonk2(b6, a1, a2, a3,
                            a4, a5, a6,
                            a7, a8):
    b3 = genetic_algorithm.getAR(b6, a1, a2,
                                                 a3, a4,
                                                 a5, a6,
                                                 a7, a8)
    return b3
def fonk3(b3):
    for rule in b3:
        print(rule)
if b4 = = '__main__':
    b5 = "kosarak.dat"
    b6 = fonk1(b5)
    a1 = 0.7
    a2 = 1
    a3 = 30
    a4 = 30
    a5 = 0.25
    a6 = 1
    a7 = 1
    a8 = 10
    b3 = fonk2(b6, a1, a2,
                                               a3, a4,
                                               a5, a6,
                                               a7, a8)
    fonk3(b3)