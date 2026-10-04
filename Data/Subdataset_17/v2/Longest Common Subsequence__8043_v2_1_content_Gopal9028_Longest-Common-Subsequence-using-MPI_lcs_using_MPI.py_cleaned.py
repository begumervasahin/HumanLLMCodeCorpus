from mpi4py import MPI
import time
def lcs(s1, s2):
    matrix = [["" for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + s1[i - 1]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1], key=len)
    cs = matrix[-1][-1]
    return len(cs), cs
def main():
    start_time = time.time()
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    if rank == 0:
        with open('a.txt', 'r') as file:
            str1 = file.read().strip()
        with open('b.txt', 'r') as file:
            str2 = file.read().strip()
        xSize = len(str1)
        ySize = len(str2)
        comm.bcast(xSize, root=0)
        comm.bcast(ySize, root=0)
        comm.bcast(str1, root=0)
        comm.bcast(str2, root=0)
        lcs_length, lcs_string = lcs(str1, str2)
        print(f"LCS length: {lcs_length}, LCS string: '{lcs_string}'")
    else:
        xSize = comm.bcast(None, root=0)
        ySize = comm.bcast(None, root=0)
        str1 = comm.bcast(None, root=0)
        str2 = comm.bcast(None, root=0)
        print(f"My rank is {rank}")
    comm.Barrier()
    if rank == 0:
        print(f"--- {time.time() - start_time} seconds ---")
if __name__ == '__main__':
    main()