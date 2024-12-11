import sys
import numpy as np
def fonk1():
    b1 = np.zeros(5, dtype=np.float)
    b2 = np.zeros(5, dtype=np.float)
    b3 = np.zeros(5, dtype=np.int)
    for line in sys.stdin:
        centroid_id, salary, b4 = map(float, line.strip().split("\t"))
        b1[int(centroid_id)] += salary
        b2[int(centroid_id)] += b4
        b3[int(centroid_id)] += 1
    return b1, b2, b3
def fonk2(b1, b2, b3):
    b5 = []
    for i, count in enumerate(b3):
        if count != 0:
            b6 = b1[i] / count
            b7 = b2[i] / count
            b5.append((i, b6, b7))
    return b5
def fonk3(b1, b2, b3, b5):
    print("Total Salary:")
    print(b1)
    print("\nTotal Stock:")
    print(b2)
    print("\nCluster Counts:")
    print(b3)
    print("\nClusters:")
    for cluster in b5:
        print(cluster)
def fonk4(b5):
    with open("b5.txt", "w+") as file:
        for centroid_id, b6, b7 in b5:
            file.write(f"{centroid_id}\t{b6};{b7}\n")
def fonk5():
    b1, b2, b3 = fonk1()
    b5 = fonk2(b1, b2, b3)
    fonk3(b1, b2, b3, b5)
    fonk4(b5)
if b8 = = "__main__":
    fonk5()