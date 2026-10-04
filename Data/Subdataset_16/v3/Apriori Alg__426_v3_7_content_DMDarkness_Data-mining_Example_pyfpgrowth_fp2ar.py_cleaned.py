
import pyfpgrowth as pyfp
import fp2ar
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
def fonk2(b6, a1):
    return pyfp.getFP(b6, a1)
def fonk3(b7, dataset_size, a2, a3):
    return fp2ar.getAR(b7, dataset_size, a2, a3)
def fonk4(b7):
    print("Frequent Patterns:")
    for pattern, support in b7.b3():
        print(f"Pattern: {pattern}, Support: {support}")
def fonk5(b8):
    print("\nAssociation Rules:")
    for rule, metrics in b8.b3():
        print(f"Rule: {rule}, Confidence: {metrics['confidence']}, Lift: {metrics['lift']}")
def fonk6():
    b5 = "kosarak.dat"
    b6 = fonk1(b5)
    a1 = 0.01
    a2 = 0.75
    a3 = 1
    b7 = fonk2(b6, a1)
    b8 = fonk3(b7, len(b6), a2, a3)
    fonk4(b7)
    fonk5(b8)
if b9 = = "__main__":
    fonk6()