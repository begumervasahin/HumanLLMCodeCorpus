import time
import numpy as np
from mpi4py import MPI
import math
def lcs(s1, s2):
    matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i - 1][j - 1] + s1[i]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1], key=len)
    cs = matrix[-1][-1]
    return len(cs), cs
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print('My rank is', rank)
start_time = time.time()
if rank == 0:
    num_procs = comm.Get_size()
    with open('a.txt', 'r') as file:
        str1 = file.read()
    with open('b.txt', 'r') as file:
        str2 = file.read()
    xSize = len(str1)
    ySize = len(str2)
    rSize = ySize
    fTab = [[0 for _ in range(rSize)] for _ in range(rSize)]
    subX = list(str1)
    subY = list(str2)
    comm.bcast(subX, root=0)
    for _ in range(num_procs):
        comm.send(subY, dest=0, tag=11)
    comm.barrier()
    lcs_result = lcs(str1, str2)
    print("LCS length:", lcs_result[0])
    print("LCS sequence:", lcs_result[1])
    if num_procs > 1:
        comm.Isend(fTab[rSize], dest=0, tag=12)
else:
    subX = comm.bcast(None, root=0)
    subY = comm.recv(source=0, tag=11)
    rSize = len(subY)
    fTab = [[0 for _ in range(rSize)] for _ in range(rSize)]
    comm.barrier()
    lcs_result = lcs(''.join(subX), ''.join(subY))
    print("LCS length:", lcs_result[0])
    print("LCS sequence:", lcs_result[1])
    comm.Isend(fTab[rSize], dest=0, tag=12)
print("--- %s seconds ---" % (time.time() - start_time))
Q