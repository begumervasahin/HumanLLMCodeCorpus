
import pyfpgrowth as pyfp
import fp2ar
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
    b6 = pyfp.getFP(b5, 0.01)
    b7 = fp2ar.getAR(b6, len(b5), 0.75, 1)