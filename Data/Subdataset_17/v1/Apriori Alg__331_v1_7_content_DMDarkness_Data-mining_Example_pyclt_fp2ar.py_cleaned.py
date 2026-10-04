
import pyclt
import fp2ar
import re
def read(dName):
    with open(dName, 'r') as f:
        Trans = []
        content = f.readlines()
        for line in content:
            sline = re.split(' |\n', line)
            trans = [int(item) for item in sline if item.isdigit()]
            if len(trans) > 0:
                Trans.append(trans)
    return Trans
dataset = read("kosarak.dat")
fi, sN = pyclt.getFP(dataset, 0.03, 0.005, 0.01)
ar = fp2ar.getAR(fi, sN, 0.75, 1)
for rule in ar:
    print(rule)