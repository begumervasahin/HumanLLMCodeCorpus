from mpi4py import MPI
import numpy as np
import time
from operator import itemgetter
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
if rank == 0:
    array_size = int(input("Please enter array size: "))
    numbers = np.arange(array_size)
    np.random.shuffle(numbers)
    print("Generated list of size", array_size, "is:", numbers)
    chunks = np.array_split(numbers, size)
else:
    chunks = None
start_time = time.time()
chunk = comm.scatter(chunks, root=0)
print("Process", rank, "has this chunk of data:", chunk)
bubble_sort(chunk)
sorted_arrays = comm.gather(chunk, root=0)
if rank == 0:
    iterator_numbers = np.zeros(len(sorted_arrays), dtype=int)
    sorted_array = []
    for _ in range(array_size):
        iterator = [(i, (99999999 if iterator_numbers[i] >= len(sorted_arrays[i]) else sorted_arrays[i][iterator_numbers[i]])) for i in range(len(sorted_arrays))]
        res = min(iterator, key=itemgetter(1))
        iterator_numbers[res[0]] += 1
        sorted_array.append(res[1])
        iterator = []
    print("\n\nSorted Array:", sorted_array)
    print("\n\nExecution Time --- %s seconds ---" % (time.time() - start_time))