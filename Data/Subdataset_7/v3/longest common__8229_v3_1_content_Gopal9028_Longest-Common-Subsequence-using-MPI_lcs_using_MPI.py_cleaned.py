import time
from mpi4py import MPI
b1 = time.time()
def fonk1(s1, s2):
    b2 = [["" for _ in range(len(s2))] for _ in range(len(s1))]
    for b3 in range(len(s1)):
        for j in range(len(s2)):
            if s1[b3] == s2[j]:
                if b3 = = 0 or j == 0:
                    b2[b3][j] = s1[b3]
                else:
                    b2[b3][j] = b2[b3 - 1][j - 1] + s1[b3]
            else:
                b2[b3][j] = max(b2[b3 - 1][j], b2[b3][j - 1], b4 = len)
    b5 = b2[-1][-1]
    return len(b5), b5
b6 = MPI.COMM_WORLD
b7 = b6.Get_rank()
if b7 = = 0:
    b8 = b6.Get_size()
    b9 = open('a.txt').read()
    b10 = open('b.txt').read()
    b11 = len(b9)
    b12 = len(b10)
    b13 = b12
    b14 = []
    b15 = []
    b16 = [[0 for _ in range(b13)] for _ in range(b13)]
    for b in range(b8):
        if b <= b11:
            b14[:] = b9
    b6.bcast(b14, b17 = 0)
    for k in range(1, b8):
        b6.send(b15, b18 = k)
    b6.barrier()
    fonk1(open('a.txt').read(), open('b.txt').read())
    if b8 > 1:
        b6.Isend(b16[b13], b18 = 0)
else:
    b14 = b6.bcast(None, b17=0)
    for b in range(b8):
        if b <= b11:
            b14[:] = b9
    b19 = []
    b6.recv(b20 = 0)
    b16 = [[0 for _ in range(b13)] for _ in range(b13)]
    b6.barrier()
    fonk1(open('a.txt').read(), open('b.txt').read())
    if b7 < b8 - 1:
        b6.Isend(b16[b13], b18 = 0)
print("--- %s seconds ---" % (time.time() - b1))