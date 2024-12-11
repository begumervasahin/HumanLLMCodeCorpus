from BST import BST
from linkedList import LinkedList as LL
from time import time
from willowCuttingHashTable import WillowCuttingHashTable
from chainedHashTable import ChainedHashTable
import sys
import random
def fonk1():
    sys.setrecursionlimit(10000)
    if len(sys.argv) != 4:
        print("Invalid Syntax\nUsage: performanceTest.py b1 b2 b3\n")
        sys.exit(1)
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    with open(b1, "r") as file:
        b4 = file.read().split()
    b5 = len(b4)
    print("Using %d words" % b5)
    b6 = ChainedHashTable(12, b2, BST)
    b7 = WillowCuttingHashTable(b3, 0, b5)
    b8 = list(range(b5))
    random.shuffle(b8)
    print("Timing put")
    b9 = time()
    for i in range(b5):
        b6[i] = b4[i]
    b10 = time() - b9
    b9 = time()
    for i in range(b5):
        b7[i] = b4[i]
    b11 = time() - b9
    print("Willow time: %f Chained time: %f" % (b11, b10))
    print("Timing get (random)")
    b9 = time()
    for i in b8:
        b12 = b6[i]
    b10 = time() - b9
    b9 = time()
    for i in b8:
        b12 = b6[i]
    b11 = time() - b9
    print("Willow time: %f Chained time: %f" % (b11, b10))
    print("Timing get (in order)")
    b9 = time()
    for i in range(b5):
        b12 = b6[i]
    b10 = time() - b9
    b9 = time()
    for i in range(b5):
        b12 = b6[i]
    b11 = time() - b9
    print("Willow time: %f Chained time: %f" % (b11, b10))
if b13 = = "__main__":
    fonk1()