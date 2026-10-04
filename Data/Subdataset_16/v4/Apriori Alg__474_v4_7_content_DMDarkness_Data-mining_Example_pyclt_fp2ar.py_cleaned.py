
import pyclt
import fp2ar
import re
def fonk1(file_name):
    with open(file_name, 'r') as file:
        b1 = []
        b2 = file.readlines()
        for line in b2:
            b3 = re.split(r' |\n', line)
            b4 = [int(item) for item in b3 if item.isdigit()]
            if b4:
                b1.append(b4)
    return b1
def fonk2():
    b5 = fonk1("kosarak.dat")
    fi, b6 = pyclt.getFP(b5, 0.03, 0.005, 0.01)
    b7 = fp2ar.getAR(fi, b6, 0.75, 1)
    print("Frequent Patterns:")
    for pattern in fi:
        print(pattern)
    print("\nAssociation Rules:")
    for rule in b7:
        print(rule)
if b8 = = "__main__":
    fonk2()