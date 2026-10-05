import numpy as np
from csv import reader
from random import randint
from copy import deepcopy
import sys
def fonk1(input_file):
    with open(input_file, 'r') as file:
        b1 = reader(file)
        b2 = np.array([row for row in b1 if row], dtype=float)
    return b2
def fonk2(b11):
    return (b11 - b11.min(b3 = 0)) / (b11.max(b3=0) - b11.min(b3=0))
def fonk3(b11, k):
    b4 = np.random.choice(len(b11), size=k, replace=False)
    return b11[b4]
def fonk4(b11, b6):
    b5 = np.sqrt(((b11 - b6[:, np.newaxis])**2).sum(b3=2))
    return np.argmin(b5, b3 = 0)
def fonk5(b11, b8, k):
    b6 = np.array([b11[b8 == i].mean(b3=0) for i in range(k)])
    return b6
def fonk6(b11, b8, b6):
    b7 = sum(np.linalg.norm(b11[b8 == i] - b6[i], b3=1)**2 for i in range(len(b6)))
    return b7
def fonk7(b11, k):
    b6 = fonk3(b11, k)
    for iteration in range(100):
        b8 = fonk4(b11, b6)
        b9 = fonk5(b11, b8, k)
        if np.all(b6 = = b9):
            break
        b6 = b9
    return b8, b6
def fonk8():
    if len(sys.argv) != 4:
        print("Usage: python script.py <inputfile.csv> <k> <outputfile.txt>")
        sys.exit(1)
    input_file, k, b10 = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    b2 = fonk1(input_file)
    b11 = fonk2(b2[:, :-1])
    b8, b6 = fonk7(b11, k)
    b7 = fonk6(b11, b8, b6)
    print(f"SSE is {b7:.2f}")
    with open(b10, 'w') as f:
        for cluster_id in b8:
            f.write(f"{cluster_id}\n")
        f.write(f"SSE is {b7:.2f}")
if b12 = = "__main__":
    fonk8()