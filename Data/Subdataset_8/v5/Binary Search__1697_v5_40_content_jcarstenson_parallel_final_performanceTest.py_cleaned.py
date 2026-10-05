from BST import BST
from linkedList import LinkedList as LL
from time import time
from willowCuttingHashTable import WillowCuttingHashTable
from chainedHashTable import ChainedHashTable
import sys
import random
def read_file(filename):
    with open(filename, "r") as f:
        return f.read().split()
def measure_put_time(hash_table, data):
    start = time()
    for i, item in enumerate(data):
        hash_table[i] = item
    return time() - start
def measure_get_time(hash_table, keys):
    start = time()
    for key in keys:
        x = hash_table[key]
    return time() - start
def main():
    sys.setrecursionlimit(10000)
    if len(sys.argv) != 4:
        print("Invalid Syntax\nUsage: performanceTest.py filename chainedLoad willowLoad\n")
        sys.exit(1)
    filename = sys.argv[1]
    chained_load = sys.argv[2]
    willow_load = sys.argv[3]
    data = read_file(filename)
    size = len(data)
    print("Using %d words" % size)
    chained = ChainedHashTable(12, chained_load, BST)
    willow = WillowCuttingHashTable(willow_load, 0, size)
    shuffled_keys = list(range(size))
    random.shuffle(shuffled_keys)
    print("Timing put")
    chained_put_time = measure_put_time(chained, data)
    willow_put_time = measure_put_time(willow, data)
    print("Willow time: %f Chained time: %f" % (willow_put_time, chained_put_time))
    print("Timing get (random)")
    chained_get_time_random = measure_get_time(chained, shuffled_keys)
    willow_get_time_random = measure_get_time(willow, shuffled_keys)
    print("Willow time: %f Chained time: %f" % (willow_get_time_random, chained_get_time_random))
    print("Timing get (in order)")
    chained_get_time_order = measure_get_time(chained, range(size))
    willow_get_time_order = measure_get_time(willow, range(size))
    print("Willow time: %f Chained time: %f" % (willow_get_time_order, chained_get_time_order))
if __name__ == "__main__":
    main()