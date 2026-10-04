
import pyclt
import fp2ar
import re
def fonk1(file_path):
    b1 = []
    with open(file_path, 'r') as file:
        b2 = file.readlines()
        for line in b2:
            b3 = re.split(r' |\n', line)
            b4 = [int(item) for item in b3 if item.isdigit()]
            if b4:
                b1.append(b4)
    return b1
if b5 = = "__main__":
    b6 = "kosarak.dat"
    b7 = fonk1(b6)
    frequent_patterns, b8 = pyclt.getFP(b7, 0.03, 0.005, 0.01)
    b9 = fp2ar.getAR(frequent_patterns, b8, 0.75, 1)
    for rule in b9:
        print(rule)