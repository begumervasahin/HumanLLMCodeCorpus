
import pyarmga as ga
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
ar = ga.getAR(dataset, 0.7, 1, 30, 30, 0.25, 1, 1, 10)
for rule in ar:
    print(rule)