import numpy as np
from csv import reader
from random import sample
import sys
def fonk1(input_file):
    with open(input_file, 'r') as file:
        b1 = reader(file)
        b2 = np.array([row for row in b1 if row], dtype=float)
    return b2
def fonk2(b12):
    return (b12 - b12.min(b3 = 0)) / (b12.max(b3=0) - b12.min(b3=0))
def fonk3(b12, k):
    b4 = sample(range(len(b12)), k)
    return b12[b4]
def fonk4(b12, b6):
    b5 = np.sqrt(((b12 - b6[:, np.newaxis])**2).sum(b3=2))
    return np.argmin(b5, b3 = 0)
def fonk5(b12, b9, k):
    b6 = np.array([b12[b9 == i].mean(b3=0) for i in range(k)])
    return b6
def fonk6(b12, b9, b6):
    b7 = sum(np.linalg.norm(b12[b9 == i] - b6[i], b3=1)**2 for i in range(len(b6)))
    return b7
def fonk7(b12, k, b8 = 100):
    b6 = fonk3(b12, k)
    for iteration in range(b8):
        b9 = fonk4(b12, b6)
        b10 = fonk5(b12, b9, k)
        if np.allclose(b6, b10):
            break
        b6 = b10
    return b9, b6
def fonk8(b9, b7, b11):
    with open(b11, 'w') as f:
        for cluster_id in b9:
            f.write(f"{cluster_id}\n")
        f.write(f"SSE is {b7:.2f}")
def fonk9():
    if len(sys.argv) != 4:
        print("Usage: python script.py <inputfile.csv> <k> <outputfile.txt>")
        sys.exit(1)
    input_file, k, b11 = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    b2 = fonk1(input_file)
    b12 = fonk2(b2[:, :-1])
    b9, b6 = fonk7(b12, k)
    b7 = fonk6(b12, b9, b6)
    print(f"SSE is {b7:.2f}")
    fonk8(b9, b7, b11)
if b13 = = "__main__":
    fonk9()