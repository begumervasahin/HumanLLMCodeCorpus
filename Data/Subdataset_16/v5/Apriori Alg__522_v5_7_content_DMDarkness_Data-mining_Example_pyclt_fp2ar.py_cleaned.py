
import pyclt
import fp2ar
import re
def fonk1(file_name):
    b1 = []
    with open(file_name, 'r') as file:
        b2 = file.readlines()
        for line in b2:
            b3 = re.split(r' |\n', line)
            b4 = [int(item) for item in b3 if item.isdigit()]
            if b4:
                b1.append(b4)
    return b1
def fonk2():
    b5 = fonk1("kosarak.dat")
    a1 = 0.03
    a2 = 0.005
    a3 = 0.01
    frequent_patterns, b6 = pyclt.getFP(b5, a1, a2, a3)
    a4 = 0.75
    a5 = 1
    b7 = fp2ar.getAR(frequent_patterns, b6, a4, a5)
    print("Frequent Patterns:")
    for pattern in frequent_patterns:
        print(pattern)
    print("\nAssociation Rules:")
    for rule in b7:
        print(rule)
if b8 = = "__main__":
    fonk2()