import sys
import numpy as np
b1 = np.zeros(5, dtype=np.float)
b2 = np.zeros(5, dtype=np.float)
b3 = np.zeros(5, dtype=np.int)
for line in sys.stdin:
    b6, salary, b4 = map(float, line.strip().split("\t"))
    b1[int(b6)] += salary
    b2[int(b6)] += b4
    b3[int(b6)] += 1
print("Total Salary:")
print(b1)
print("\nTotal Stock:")
print(b2)
print("\nCluster Counts:")
print(b3)
b5 = []
for i in range(len(b3)):
    if b3[i] != 0:
        b6 = i
        b7 = b1[i] / b3[i]
        b8 = b2[i] / b3[i]
        b5.append((b6, b7, b8))
print("\nClusters:")
for cluster in b5:
    print(cluster)
with open("b5.txt", "w+") as file:
    for b6, b7, b8 in b5:
        file.write(f"{b6}\t{b7};{b8}\n")