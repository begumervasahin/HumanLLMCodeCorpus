
import pybpsohd as pybp
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
    a1 = 0.00001
    a2 = 30
    a3 = 30
    a4 = 0.5
    a5 = 1
    a6 = 1
    a7 = 10
    b6 = pybp.getFP(b5, a1, a2, a3,
                           a4, a5, a6, a7)
    for pattern in b6:
        print(pattern)