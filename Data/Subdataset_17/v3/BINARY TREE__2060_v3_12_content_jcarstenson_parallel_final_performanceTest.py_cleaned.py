import sys
import random
from time import time
from BST import BST
from linkedList import LinkedList as LL
from willowCuttingHashTable import WillowCuttingHashTable
from chainedHashTable import ChainedHashTable
def read_data(filename):
    with open(filename, "r") as file:
        data = file.read().split()
    return data
def measure_put_time(hash_table, data):
    start_time = time()
    for i, value in enumerate(data):
        hash_table[i] = value
    return time() - start_time
def measure_get_time(hash_table, keys, description):
    start_time = time()
    for key in keys:
        _ = hash_table[key]
    return time() - start_time
def main():
    sys.setrecursionlimit(10000)
    if len(sys.argv) != 4:
        print("Invalid Syntax\nUsage: performanceTest.py filename chainedLoad willowLoad\n")
        sys.exit(1)
    filename = sys.argv[1]
    chained_load_factor = int(sys.argv[2])
    willow_load_factor = int(sys.argv[3])
    data = read_data(filename)
    size = len(data)
    print(f"Using {size} words")
    chained_hash_table = ChainedHashTable(12, chained_load_factor, BST)
    willow_hash_table = WillowCuttingHashTable(willow_load_factor, 0, size)
    shuffled_keys = list(range(size))
    random.shuffle(shuffled_keys)
    print("Timing put")
    chained_put_time = measure_put_time(chained_hash_table, data)
    willow_put_time = measure_put_time(willow_hash_table, data)
    print(f"Chained put time: {chained_put_time:.6f} seconds | Willow put time: {willow_put_time:.6f} seconds")
    print("Timing get (random)")
    chained_get_time_random = measure_get_time(chained_hash_table, shuffled_keys, "random")
    willow_get_time_random = measure_get_time(willow_hash_table, shuffled_keys, "random")
    print(f"Chained get (random) time: {chained_get_time_random:.6f} seconds | Willow get (random) time: {willow_get_time_random:.6f} seconds")
    print("Timing get (in order)")
    chained_get_time_order = measure_get_time(chained_hash_table, range(size), "in order")
    willow_get_time_order = measure_get_time(willow_hash_table, range(size), "in order")
    print(f"Chained get (in order) time: {chained_get_time_order:.6f} seconds | Willow get (in order) time: {willow_get_time_order:.6f} seconds")
if __name__ == "__main__":
    main()