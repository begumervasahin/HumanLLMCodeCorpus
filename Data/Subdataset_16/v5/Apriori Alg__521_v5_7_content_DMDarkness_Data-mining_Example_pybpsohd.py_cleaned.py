
import pybpsohd as pybp
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
    a1 = 0.00001
    a2 = 30
    a3 = 30
    a4 = 0.5
    a5 = 1
    a6 = 1
    a7 = 10
    b6 = pybp.getFP(
        b5, a1, a2, a3,
        a4, a5, a6, a7
    )
    print("Frequent itemsets:")
    for itemset in b6:
        print(itemset)
if b7 = = "__main__":
    fonk2()
