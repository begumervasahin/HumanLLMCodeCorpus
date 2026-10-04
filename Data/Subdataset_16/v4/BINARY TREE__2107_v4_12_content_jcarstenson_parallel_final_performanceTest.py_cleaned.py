import sys
import random
from time import time
from BST import BST
from linkedList import LinkedList as LL
from willowCuttingHashTable import WillowCuttingHashTable
from chainedHashTable import ChainedHashTable
def fonk1():
    sys.setrecursionlimit(10000)
    if len(sys.argv) != 4:
        print("Invalid Syntax\nUsage: performanceTest.py b1 b2 b3\n")
        sys.exit(1)
    b1 = sys.argv[1]
    b2 = int(sys.argv[2])
    b3 = int(sys.argv[3])
    with open(b1, "r") as f:
        b4 = f.read().split()
    b5 = len(b4)
    print(f"Using {b5} words")
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
    print(f"Willow time: {b11:.6f} Chained time: {b10:.6f}")
    print("Timing get (random)")
    b9 = time()
    for i in b8:
        b12 = b6[i]
    b13 = time() - b9
    b9 = time()
    for i in b8:
        b12 = b7[i]
    b14 = time() - b9
    print(f"Willow time: {b14:.6f} Chained time: {b13:.6f}")
    print("Timing get (in order)")
    b9 = time()
    for i in range(b5):
        b12 = b6[i]
    b15 = time() - b9
    b9 = time()
    for i in range(b5):
        b12 = b7[i]
    b16 = time() - b9
    print(f"Willow time: {b16:.6f} Chained time: {b15:.6f}")
if b17 = = "__main__":
    fonk1()