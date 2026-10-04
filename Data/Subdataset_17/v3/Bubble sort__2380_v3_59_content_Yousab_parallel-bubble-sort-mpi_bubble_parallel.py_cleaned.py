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
def main():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    if rank == 0:
        array_size = int(input("Please enter array size: "))
        numbers = np.arange(array_size)
        np.random.shuffle(numbers)
        print(f"Generated list of size {array_size} is: {numbers}")
        chunks = np.array_split(numbers, size)
    else:
        chunks = None
    start_time = time.time()
    chunk = comm.scatter(chunks, root=0)
    print(f"Process {rank} received chunk: {chunk}")
    bubble_sort(chunk)
    sorted_chunks = comm.gather(chunk, root=0)
    if rank == 0:
        sorted_array = merge_sorted_chunks(sorted_chunks, array_size, size)
        print(f"\n\nSorted Array: {sorted_array}")
        print(f"\n\nExecution Time: {time.time() - start_time} seconds")
def merge_sorted_chunks(sorted_chunks, array_size, size):
    iterator_indices = np.zeros(size, dtype=int)
    sorted_array = []
    for _ in range(array_size):
        iterator = [
            (i, (99999999 if iterator_indices[i] >= len(sorted_chunks[i]) else sorted_chunks[i][iterator_indices[i]]))
            for i in range(size)
        ]
        min_value_index = min(iterator, key=itemgetter(1))
        iterator_indices[min_value_index[0]] += 1
        sorted_array.append(min_value_index[1])
    return sorted_array
if __name__ == "__main__":
    main()