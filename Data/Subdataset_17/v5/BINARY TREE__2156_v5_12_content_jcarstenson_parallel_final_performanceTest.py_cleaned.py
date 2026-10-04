import sys
import random
from time import time
from BST import BST
from linkedList import LinkedList as LL
from willowCuttingHashTable import WillowCuttingHashTable
from chainedHashTable import ChainedHashTable
def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().split()
    return data
def initialize_hash_tables(size, chained_load, willow_load):
    chained = ChainedHashTable(12, chained_load, BST)
    willow = WillowCuttingHashTable(willow_load, 0, size)
    return chained, willow
def measure_put_time(data, hash_table):
    start = time()
    for i, value in enumerate(data):
        hash_table[i] = value
    return time() - start
def measure_get_time(hash_table, keys):
    start = time()
    for key in keys:
        _ = hash_table[key]
    return time() - start
def main():
    sys.setrecursionlimit(10000)
    if len(sys.argv) != 4:
        print("Invalid Syntax\nUsage: performanceTest.py filename chainedLoad willowLoad\n")
        sys.exit(1)
    filename = sys.argv[1]
    chained_load = int(sys.argv[2])
    willow_load = int(sys.argv[3])
    data = read_data(filename)
    size = len(data)
    print(f"Using {size} words")
    chained, willow = initialize_hash_tables(size, chained_load, willow_load)
    shuffled_keys = list(range(size))
    random.shuffle(shuffled_keys)
    print("Timing put operations")
    chained_put_time = measure_put_time(data, chained)
    willow_put_time = measure_put_time(data, willow)
    print(f"Willow put time: {willow_put_time:.6f} seconds")
    print(f"Chained put time: {chained_put_time:.6f} seconds")
    print("Timing get operations (random order)")
    chained_get_random_time = measure_get_time(chained, shuffled_keys)
    willow_get_random_time = measure_get_time(willow, shuffled_keys)
    print(f"Willow get time (random): {willow_get_random_time:.6f} seconds")
    print(f"Chained get time (random): {chained_get_random_time:.6f} seconds")
    print("Timing get operations (in order)")
    ordered_keys = list(range(size))
    chained_get_order_time = measure_get_time(chained, ordered_keys)
    willow_get_order_time = measure_get_time(willow, ordered_keys)
    print(f"Willow get time (in order): {willow_get_order_time:.6f} seconds")
    print(f"Chained get time (in order): {chained_get_order_time:.6f} seconds")
if __name__ == "__main__":
    main()