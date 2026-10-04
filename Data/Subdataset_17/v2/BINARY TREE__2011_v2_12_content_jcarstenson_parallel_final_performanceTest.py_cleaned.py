import sys
import random
from time import time
from BST import BST
from linkedList import LinkedList as LL
from willowCuttingHashTable import WillowCuttingHashTable
from chainedHashTable import ChainedHashTable
def main():
    sys.setrecursionlimit(10000)
    if len(sys.argv) != 4:
        print("Invalid Syntax\nUsage: performanceTest.py filename chainedLoad willowLoad\n")
        sys.exit(1)
    filename = sys.argv[1]
    chainedLoad = int(sys.argv[2])
    willowLoad = int(sys.argv[3])
    with open(filename, "r") as f:
        data = f.read().split()
    size = len(data)
    print(f"Using {size} words")
    chained = ChainedHashTable(12, chainedLoad, BST)
    willow = WillowCuttingHashTable(willowLoad, 0, size)
    shuffledKeys = list(range(size))
    random.shuffle(shuffledKeys)
    print("Timing put")
    start = time()
    for i in range(size):
        chained[i] = data[i]
    chainedPutTime = time() - start
    start = time()
    for i in range(size):
        willow[i] = data[i]
    willowPutTime = time() - start
    print(f"Willow put time: {willowPutTime:.6f} seconds | Chained put time: {chainedPutTime:.6f} seconds")
    print("Timing get (random)")
    start = time()
    for i in shuffledKeys:
        _ = chained[i]
    chainedGetTimeRandom = time() - start
    start = time()
    for i in shuffledKeys:
        _ = willow[i]
    willowGetTimeRandom = time() - start
    print(f"Willow get (random) time: {willowGetTimeRandom:.6f} seconds | Chained get (random) time: {chainedGetTimeRandom:.6f} seconds")
    print("Timing get (in order)")
    start = time()
    for i in range(size):
        _ = chained[i]
    chainedGetTimeOrder = time() - start
    start = time()
    for i in range(size):
        _ = willow[i]
    willowGetTimeOrder = time() - start
    print(f"Willow get (in order) time: {willowGetTimeOrder:.6f} seconds | Chained get (in order) time: {chainedGetTimeOrder:.6f} seconds")
if __name__ == "__main__":
    main()