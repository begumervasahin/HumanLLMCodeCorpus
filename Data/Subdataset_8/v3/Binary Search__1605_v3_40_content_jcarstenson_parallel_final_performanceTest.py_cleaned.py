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
def timing_put(table, data):
    start = time()
    for i, item in enumerate(data):
        table[i] = item
    return time() - start
def timing_get(table, keys):
    start = time()
    for key in keys:
        x = table[key]
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
    chained_put_time = timing_put(chained, data)
    willow_put_time = timing_put(willow, data)
    print("Willow time: %f Chained time: %f" % (willow_put_time, chained_put_time))
    print("Timing get (random)")
    chained_get_time = timing_get(chained, shuffled_keys)
    willow_get_time = timing_get(willow, shuffled_keys)
    print("Willow time: %f Chained time: %f" % (willow_get_time, chained_get_time))
    print("Timing get (in order)")
    chained_get_time = timing_get(chained, range(size))
    willow_get_time = timing_get(willow, range(size))
    print("Willow time: %f Chained time: %f" % (willow_get_time, chained_get_time))
if __name__ == "__main__":
    main()