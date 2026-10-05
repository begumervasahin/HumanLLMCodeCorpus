import time
import numpy as np
from mpi4py import MPI
import math
b1 = time.time()
print("--- %s seconds ---" % (time.time() - b1))
def fonk1(s1, s2):
    b2 = [["" for x in range(len(s2))] for x in range(len(s1))]
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
print('My b7 is ',b7)
if ( b7 = = 0 ):
		a1 = 1
		b8 = open('a.txt').read()
		b9 = open('b.txt').read()
		print b8
		b10 = len(b8)
		b11 = len(b9)
		b12 = []
		b13 = []
		b14 = b11
		b15 = [[0 for b3 in xrange(b14)] for b3 in xrange(b14)]
		for b in range(a1):
			if ((b) <= b10):
				b12[:] = b8
		for b in range(a1):
			if ((b) <= b10):
				b13[:] = b8
		b6.bcast(b12, b16 = 0)
		for k in range(a1):
			b6.send([b13,MPI.INT],b17 = 0)
		b6.barrier()
		fonk1(open('a.txt').read(), open('b.txt').read())
		if (a1 > 1):
			b6.Isend(ftab[b14],b17 = 0)
else:
	b6.bcast(b12, b16 = 0)
	for b in range(a1):
		if ((b) <= b10):
			b12[:] = b8
	for b in range(a1):
		if ((b) <= b10):
			b13[:] = b8
	b18 = []
	b6.recv(b19 = 0)
	b15 = [[0 for b3 in xrange(b14)] for b3 in xrange(b14)]
	b6.barrier()
	fonk1(open('a.txt').read(), open('b.txt').read())
	if (rNK < a1-1):
			b6.Isend(ftab[b14],b17 = 0)
print("--- %s seconds ---" % (time.time() - b1))