from BST import BST
from linkedList import LinkedList as LL
from time import time
from willowCuttingHashTable import WillowCuttingHashTable
from chainedHashTable import ChainedHashTable
import sys
import random
def fonk1(b3):
    with open(b3, "r") as f:
        return f.read().split()
def fonk2(table, b6):
    b1 = time()
    for i, item in enumerate(b6):
        table[i] = item
    return time() - b1
def fonk3(table, keys):
    b1 = time()
    for key in keys:
        b2 = table[key]
    return time() - b1
def fonk4():
    sys.setrecursionlimit(10000)
    if len(sys.argv) != 4:
        print("Invalid Syntax\nUsage: performanceTest.py b3 chainedLoad willowLoad\n")
        sys.exit(1)
    b3 = sys.argv[1]
    b4 = sys.argv[2]
    b5 = sys.argv[3]
    b6 = fonk1(b3)
    b7 = len(b6)
    print("Using %d words" % b7)
    b8 = ChainedHashTable(12, b4, BST)
    b9 = WillowCuttingHashTable(b5, 0, b7)
    b10 = list(range(b7))
    random.shuffle(b10)
    print("Timing put")
    b11 = fonk2(b8, b6)
    b12 = fonk2(b9, b6)
    print("Willow time: %f Chained time: %f" % (b12, b11))
    print("Timing get (random)")
    b13 = fonk3(b8, b10)
    b14 = fonk3(b9, b10)
    print("Willow time: %f Chained time: %f" % (b14, b13))
    print("Timing get (in order)")
    b13 = fonk3(b8, range(b7))
    b14 = fonk3(b9, range(b7))
    print("Willow time: %f Chained time: %f" % (b14, b13))
if b15 = = "__main__":
    fonk4()