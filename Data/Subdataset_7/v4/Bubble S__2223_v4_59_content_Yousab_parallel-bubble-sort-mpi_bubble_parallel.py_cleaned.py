from mpi4py import MPI
import numpy as np
import time
from operator import itemgetter
def fonk1(nums):
    b1 = True
    while b1:
        b1 = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                b1 = True
b2 = MPI.COMM_WORLD
b3 = b2.Get_size()
b4 = b2.Get_rank()
if b4 = = 0:
    b5 = input("Please enter array b3: ")
    b6 = np.arange(int(b5))
    np.random.shuffle(b6)
    print("Generated list of b3 " + str(b5) + " is: " + str(b6))
    b7 = np.array_split(b6, b3)
else:
    b7 = None
b8 = time.time()
b9 = b2.scatter(b7, root=0)
print("Process " + str(b4) + " has this b9 of data: " + str(b9))
fonk1(b9)
b10 = b2.gather(b9, root=0)
if b4 = = 0:
    b11 = np.zeros((len(b10),), dtype=int)
    b12 = []
    for my_index in range(0, int(b5)):
        b13 = [(i, (99999999 if b11[i] >= len(b10[i]) else b10[i][b11[i]])) for i in range(0, len(b10))]
        b14 = min(b13, key=itemgetter(1))
        b11[b14[0]] = b11[b14[0]] + 1
        b12.append(b14[1])
        b13 = []
    print("\n\n Sorted Array: " + str(b12))
    print("\n\n Execution Time --- %s seconds ---" % (time.time() - b8))