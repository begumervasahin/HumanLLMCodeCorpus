import time
import numpy as np
from mpi4py import MPI
import math
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
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
print('My rank is ',rank)
if ( rank == 0 ):
		num_procs = 1
		str1= open('a.txt').read()
		str2= open('b.txt').read()
		print str1
		xSize=len(str1)
		ySize=len(str2)
		subX = []
		subY = []
		rSize =ySize
		fTab =[[0 for i in xrange(rSize)] for i in xrange(rSize)]
		for b in range(num_procs):
			if ((b) <= xSize):
				subX[:] = str1
		for b in range(num_procs):
			if ((b) <= xSize):
				subY[:] = str1
		comm.bcast(subX, root=0)
		for k in range(num_procs):
			comm.send([subY,MPI.INT],dest=0)
		comm.barrier()
		lcs(open('a.txt').read(), open('b.txt').read())
		if (num_procs > 1):
			comm.Isend(ftab[rSize],dest=0)
else:
	comm.bcast(subX, root=0)
	for b in range(num_procs):
		if ((b) <= xSize):
			subX[:] = str1
	for b in range(num_procs):
		if ((b) <= xSize):
			subY[:] = str1
	mySubY = []
	comm.recv(source=0)
	fTab =[[0 for i in xrange(rSize)] for i in xrange(rSize)]
	comm.barrier()
	lcs(open('a.txt').read(), open('b.txt').read())
	if (rNK < num_procs-1):
			comm.Isend(ftab[rSize],dest=0)
print("--- %s seconds ---" % (time.time() - start_time))