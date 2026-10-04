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
    print(f"Willow time: {willowPutTime:.6f} Chained time: {chainedPutTime:.6f}")
    print("Timing get (random)")
    start = time()
    for i in shuffledKeys:
        x = chained[i]
    chainedGetRandomTime = time() - start
    start = time()
    for i in shuffledKeys:
        x = willow[i]
    willowGetRandomTime = time() - start
    print(f"Willow time: {willowGetRandomTime:.6f} Chained time: {chainedGetRandomTime:.6f}")
    print("Timing get (in order)")
    start = time()
    for i in range(size):
        x = chained[i]
    chainedGetOrderTime = time() - start
    start = time()
    for i in range(size):
        x = willow[i]
    willowGetOrderTime = time() - start
    print(f"Willow time: {willowGetOrderTime:.6f} Chained time: {chainedGetOrderTime:.6f}")
if __name__ == "__main__":
    main()