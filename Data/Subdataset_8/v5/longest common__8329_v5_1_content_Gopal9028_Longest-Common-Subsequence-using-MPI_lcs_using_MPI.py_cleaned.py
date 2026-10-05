import time
from mpi4py import MPI
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
def longest_common_subsequence(s1, s2):
    matrix = [["" for _ in range(len(s2))] for _ in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i - 1][j - 1] + s1[i]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1], key=len)
    longest_subsequence = matrix[-1][-1]
    return len(longest_subsequence), longest_subsequence
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print('My rank is', rank)
if rank == 0:
    num_procs = 1
    str1 = open('a.txt').read()
    str2 = open('b.txt').read()
    print(str1)
    x_size = len(str1)
    y_size = len(str2)
    subX = []
    subY = []
    r_size = y_size
    f_tab = [[0 for _ in range(r_size)] for _ in range(r_size)]
    for b in range(num_procs):
        if b <= x_size:
            subX[:] = str1
    for b in range(num_procs):
        if b <= x_size:
            subY[:] = str1
    comm.bcast(subX, root=0)
    for k in range(num_procs):
        comm.send([subY, MPI.INT], dest=0)
    comm.barrier()
    longest_common_subsequence(open('a.txt').read(), open('b.txt').read())
    if num_procs > 1:
        comm.Isend(f_tab[r_size], dest=0)
else:
    subX = comm.bcast(None, root=0)
    for b in range(num_procs):
        if b <= x_size:
            subX[:] = str1
    for b in range(num_procs):
        if b <= x_size:
            subY[:] = str1
    mySubY = []
    comm.recv(source=0)
    f_tab = [[0 for _ in range(r_size)] for _ in range(r_size)]
    comm.barrier()
    longest_common_subsequence(open('a.txt').read(), open('b.txt').read())
    if rank < num_procs - 1:
        comm.Isend(f_tab[r_size], dest=0)
print("--- %s seconds ---" % (time.time() - start_time))