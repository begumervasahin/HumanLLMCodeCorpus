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
        print("Invalid Syntax\nUsage: performanceTest.py b1 chainedLoad willowLoad\n")
        sys.exit(1)
    b1 = sys.argv[1]
    b2 = int(sys.argv[2])
    b3 = int(sys.argv[3])
    with open(b1, "r") as file:
        b4 = file.read().split()
    b5 = len(b4)
    print(f"Using {b5} b4")
    b6 = ChainedHashTable(12, b2, BST)
    b7 = WillowCuttingHashTable(b3, 0, b5)
    b8 = list(range(b5))
    random.shuffle(b8)
    print("Timing put operations...")
    b9 = fonk5(lambda: fonk2(b6, b4))
    b10 = fonk5(lambda: fonk2(b7, b4))
    print(f"Chained insertion time: {b9:.6f} seconds")
    print(f"Willow insertion time: {b10:.6f} seconds")
    print("Timing random access (get) operations...")
    b11 = fonk5(lambda: fonk3(b6, b8))
    b12 = fonk5(lambda: fonk3(b7, b8))
    print(f"Chained random access time: {b11:.6f} seconds")
    print(f"Willow random access time: {b12:.6f} seconds")
    print("Timing in-order access (get) operations...")
    b13 = fonk5(lambda: fonk4(b6, b5))
    b14 = fonk5(lambda: fonk4(b7, b5))
    print(f"Chained in-order access time: {b13:.6f} seconds")
    print(f"Willow in-order access time: {b14:.6f} seconds")
def fonk2(table, b4):
    for i, word in enumerate(b4):
        table[i] = word
def fonk3(table, indices):
    for i in indices:
        b15 = table[i]
def fonk4(table, count):
    for i in range(count):
        b15 = table[i]
def fonk5(operation):
    b16 = time()
    operation()
    return time() - b16
if b17 = = "__main__":
    fonk1()