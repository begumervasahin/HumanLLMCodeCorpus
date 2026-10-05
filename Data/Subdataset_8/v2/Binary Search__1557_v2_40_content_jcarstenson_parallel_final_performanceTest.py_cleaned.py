from BST import BST
from linkedList import LinkedList as LL
from time import time
from willowCuttingHashTable import WillowCuttingHashTable
from chainedHashTable import ChainedHashTable
import sys
import random
def main():
    sys.setrecursionlimit(10000)
    if len(sys.argv) != 4:
        print("Invalid Syntax\nUsage: performanceTest.py filename chainedLoad willowLoad\n")
        sys.exit(1)
    filename = sys.argv[1]
    chained_load = sys.argv[2]
    willow_load = sys.argv[3]
    with open(filename, "r") as f:
        data = f.read().split()
    size = len(data)
    print("Using %d words" % size)
    chained = ChainedHashTable(12, chained_load, BST)
    willow = WillowCuttingHashTable(willow_load, 0, size)
    shuffled_keys = list(range(size))
    random.shuffle(shuffled_keys)
    print("Timing put")
    start = time()
    for i in range(size):
        chained[i] = data[i]
    chained_put_time = time() - start
    start = time()
    for i in range(size):
        willow[i] = data[i]
    willow_put_time = time() - start
    print("Willow time: %f Chained time: %f" % (willow_put_time, chained_put_time))
    print("Timing get (random)")
    start = time()
    for i in shuffled_keys:
        x = chained[i]
    chained_get_time = time() - start
    start = time()
    for i in shuffled_keys:
        x = chained[i]
    willow_get_time = time() - start
    print("Willow time: %f Chained time: %f" % (willow_get_time, chained_get_time))
    print("Timing get (in order)")
    start = time()
    for i in range(size):
        x = chained[i]
    chained_get_time = time() - start
    start = time()
    for i in range(size):
        x = chained[i]
    willow_get_time = time() - start
    print("Willow time: %f Chained time: %f" % (willow_get_time, chained_get_time))
if __name__ == "__main__":
    main()