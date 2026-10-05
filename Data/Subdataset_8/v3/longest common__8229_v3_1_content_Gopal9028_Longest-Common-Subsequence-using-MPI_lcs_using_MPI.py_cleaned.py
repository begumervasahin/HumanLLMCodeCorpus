import time
from mpi4py import MPI
start_time = time.time()
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
if rank == 0:
    num_procs = comm.Get_size()
    str1 = open('a.txt').read()
    str2 = open('b.txt').read()
    x_size = len(str1)
    y_size = len(str2)
    r_size = y_size
    sub_x = []
    sub_y = []
    f_tab = [[0 for _ in range(r_size)] for _ in range(r_size)]
    for b in range(num_procs):
        if b <= x_size:
            sub_x[:] = str1
    comm.bcast(sub_x, root=0)
    for k in range(1, num_procs):
        comm.send(sub_y, dest=k)
    comm.barrier()
    longest_common_subsequence(open('a.txt').read(), open('b.txt').read())
    if num_procs > 1:
        comm.Isend(f_tab[r_size], dest=0)
else:
    sub_x = comm.bcast(None, root=0)
    for b in range(num_procs):
        if b <= x_size:
            sub_x[:] = str1
    my_sub_y = []
    comm.recv(source=0)
    f_tab = [[0 for _ in range(r_size)] for _ in range(r_size)]
    comm.barrier()
    longest_common_subsequence(open('a.txt').read(), open('b.txt').read())
    if rank < num_procs - 1:
        comm.Isend(f_tab[r_size], dest=0)
print("--- %s seconds ---" % (time.time() - start_time))