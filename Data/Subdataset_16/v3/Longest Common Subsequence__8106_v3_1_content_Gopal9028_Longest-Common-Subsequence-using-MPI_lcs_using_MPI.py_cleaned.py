from mpi4py import MPI
import time
def fonk1(s1, s2):
    b1 = [["" for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                b1[i][j] = b1[i - 1][j - 1] + s1[i - 1]
            else:
                b1[i][j] = max(b1[i - 1][j], b1[i][j - 1], b2 = len)
    b3 = b1[-1][-1]
    return len(b3), b3
def fonk2(filename):
    with open(filename, 'r') as file:
        return file.read().strip()
def fonk3(b7, b5, b4 = None):
    return b7.bcast(b4, b5 = b5)
def fonk4():
    b6 = time.time()
    b7 = MPI.COMM_WORLD
    b8 = b7.Get_rank()
    b9 = b7.Get_size()
    if b8 = = 0:
        b10 = fonk2('a.txt')
        b11 = fonk2('b.txt')
        b12 = len(b10)
        b13 = len(b11)
        fonk3(b7, b5 = 0, b4=b12)
        fonk3(b7, b5 = 0, b4=b13)
        fonk3(b7, b5 = 0, b4=b10)
        fonk3(b7, b5 = 0, b4=b11)
        lcs_length, b14 = fonk1(b10, b11)
        print(f"LCS length: {lcs_length}, LCS string: '{b14}'")
    else:
        b12 = fonk3(b7, b5=0)
        b13 = fonk3(b7, b5=0)
        b10 = fonk3(b7, b5=0)
        b11 = fonk3(b7, b5=0)
        print(f"My b8 is {b8}")
    b7.Barrier()
    if b8 = = 0:
        b15 = time.time() - b6
        print(f"--- {b15:.2f} seconds ---")
if b16 = = '__main__':
    fonk4()