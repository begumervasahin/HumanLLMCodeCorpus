import time
import numpy as np
from mpi4py import MPI
import math
def fonk1(s1, s2):
    b1 = [["" for x in range(len(s2))] for x in range(len(s1))]
    for b2 in range(len(s1)):
        for j in range(len(s2)):
            if s1[b2] == s2[j]:
                if b2 = = 0 or j == 0:
                    b1[b2][j] = s1[b2]
                else:
                    b1[b2][j] = b1[b2 - 1][j - 1] + s1[b2]
            else:
                b1[b2][j] = max(b1[b2 - 1][j], b1[b2][j - 1], b3 = len)
    b4 = b1[-1][-1]
    return len(b4), b4
b5 = MPI.COMM_WORLD
b6 = b5.Get_rank()
print('My b6 is', b6)
b7 = time.time()
if b6 = = 0:
    b8 = b5.Get_size()
    with open('a.txt', 'r') as file:
        b9 = file.read()
    with open('b.txt', 'r') as file:
        b10 = file.read()
    b11 = len(b9)
    b12 = len(b10)
    b13 = b12
    b14 = [[0 for _ in range(b13)] for _ in range(b13)]
    b15 = list(b9)
    b16 = list(b10)
    b5.bcast(b15, b17 = 0)
    for _ in range(b8):
        b5.send(b16, b18 = 0, tag=11)
    b5.barrier()
    b19 = fonk1(b9, b10)
    print("LCS length:", b19[0])
    print("LCS sequence:", b19[1])
    if b8 > 1:
        b5.Isend(b14[b13], b18 = 0, tag=12)
else:
    b15 = b5.bcast(None, b17=0)
    b16 = b5.recv(source=0, tag=11)
    b13 = len(b16)
    b14 = [[0 for _ in range(b13)] for _ in range(b13)]
    b5.barrier()
    b19 = fonk1(''.join(b15), ''.join(b16))
    print("LCS length:", b19[0])
    print("LCS sequence:", b19[1])
    b5.Isend(b14[b13], b18 = 0, tag=12)
print("--- %s seconds ---" % (time.time() - b7))
Q