
import pyarmga as ga
import re
def fonk1(file_name):
    with open(file_name, 'r') as file:
        b1 = file.readlines()
    b2 = []
    for line in b1:
        b3 = re.split(r' |\n', line)
        b4 = [int(item) for item in b3 if item.isdigit()]
        if b4:
            b2.append(b4)
    return b2
def fonk2(b6, a1, a2, a3, a4, a5, a6, a7, a8):
    return ga.getAR(b6, a1, a2, a3, a4, a5, a6, a7, a8)
def fonk3():
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
    b7 = fonk2(
        b6,
        a1,
        a2,
        a3,
        a4,
        a5,
        a6,
        a7,
        a8
    )
    for rule in b7:
        print(rule)
if b8 = = "__main__":
    fonk3()