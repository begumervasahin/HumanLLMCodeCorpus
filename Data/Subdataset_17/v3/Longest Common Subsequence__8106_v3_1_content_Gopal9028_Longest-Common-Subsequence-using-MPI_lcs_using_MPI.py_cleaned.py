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
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()
def broadcast_data(comm, root, data=None):
    return comm.bcast(data, root=root)
def main():
    start_time = time.time()
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    if rank == 0:
        str1 = read_file('a.txt')
        str2 = read_file('b.txt')
        xSize = len(str1)
        ySize = len(str2)
        broadcast_data(comm, root=0, data=xSize)
        broadcast_data(comm, root=0, data=ySize)
        broadcast_data(comm, root=0, data=str1)
        broadcast_data(comm, root=0, data=str2)
        lcs_length, lcs_string = lcs(str1, str2)
        print(f"LCS length: {lcs_length}, LCS string: '{lcs_string}'")
    else:
        xSize = broadcast_data(comm, root=0)
        ySize = broadcast_data(comm, root=0)
        str1 = broadcast_data(comm, root=0)
        str2 = broadcast_data(comm, root=0)
        print(f"My rank is {rank}")
    comm.Barrier()
    if rank == 0:
        elapsed_time = time.time() - start_time
        print(f"--- {elapsed_time:.2f} seconds ---")
if __name__ == '__main__':
    main()