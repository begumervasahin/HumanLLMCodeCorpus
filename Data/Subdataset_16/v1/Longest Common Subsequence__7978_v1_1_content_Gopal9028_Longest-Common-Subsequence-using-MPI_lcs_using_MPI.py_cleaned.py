from mpi4py import MPI
import time
def fonk1(s1, s2):
    b1 = [["" for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                b1[i][j] = b1[i - 1][j - 1] + s1[i - 1]
            else:
                b1[i][j] = max(b1[i - 1][j], b1[i][j - 1], b2 = len)
    b3 = b1[-1][-1]
    return len(b3), b3
def fonk2():
    b4 = time.time()
    b5 = MPI.COMM_WORLD
    b6 = b5.Get_rank()
    b7 = b5.Get_size()
    if b6 = = 0:
        with open('a.txt', 'r') as file:
            b8 = file.read().strip()
        with open('b.txt', 'r') as file:
            b9 = file.read().strip()
        b10 = len(b8)
        b11 = len(b9)
        b5.bcast(b10, b12 = 0)
        b5.bcast(b11, b12 = 0)
        b5.bcast(b8, b12 = 0)
        b5.bcast(b9, b12 = 0)
        lcs_length, b13 = fonk1(b8, b9)
        print(f"LCS length: {lcs_length}, LCS string: '{b13}'")
    else:
        b10 = b5.bcast(None, b12=0)
        b11 = b5.bcast(None, b12=0)
        b8 = b5.bcast(None, b12=0)
        b9 = b5.bcast(None, b12=0)
        print(f"My b6 is {b6}")
    b5.Barrier()
    if b6 = = 0:
        print("--- %s seconds ---" % (time.time() - b4))
if b14 = = '__main__':
    fonk2()