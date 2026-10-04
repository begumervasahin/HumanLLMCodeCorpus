
import pybpsohd as pybp
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
fi = pybp.getFP(dataset, 0.00001, 30, 30, 0.5, 1, 1, 10)
for itemset in fi:
    print(itemset)
