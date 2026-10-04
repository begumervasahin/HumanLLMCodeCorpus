
import pybpsohd as pybp
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
    b6 = pybp.getFP(b5, 0.00001, 30, 30, 0.5, 1, 1, 10)
    print("Frequent itemsets:")
    for itemset in b6:
        print(itemset)
if b7 = = "__main__":
    fonk2()
