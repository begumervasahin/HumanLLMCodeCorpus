
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
    b6 = pybp.getFP(b5, 0.00001, 30, 30, 0.5, 1, 1, 10)
    for pattern in b6:
        print(pattern)