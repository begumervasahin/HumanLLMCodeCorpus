
import pybpsohd as pybp
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
    b8 = pybp.getFP(b7, 0.00001, 30, 30, 0.5, 1, 1, 10)
    for itemset in b8:
        print(itemset)