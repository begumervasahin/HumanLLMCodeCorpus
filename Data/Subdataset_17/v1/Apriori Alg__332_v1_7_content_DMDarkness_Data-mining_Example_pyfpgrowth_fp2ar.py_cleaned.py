
import pyfpgrowth as pyfp
import fp2ar
import re
def read(dName):
    with open(dName, 'r') as f:
        content = f.readlines()
    Trans = []
    for line in content:
        sline = re.split(' |\n', line)
        trans = [int(item) for item in sline if item.isdigit()]
        if trans:
            Trans.append(trans)
    return Trans
dataset = read("kosarak.dat")
fi = pyfp.getFP(dataset, 0.01)
ar = fp2ar.getAR(fi, len(dataset), 0.75, 1)
print("Frequent Patterns:")
for pattern in fi:
    print(pattern)
print("\nAssociation Rules:")
for rule in ar:
    print(rule)