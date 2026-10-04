import sys
import random
from time import time
from BST import BST
from linkedList import LinkedList as LL
from willowCuttingHashTable import WillowCuttingHashTable
from chainedHashTable import ChainedHashTable
def fonk1(b6):
    with open(b6, "r") as f:
        b1 = f.read().split()
    return b1
def fonk2(b9, b7, b8):
    b2 = ChainedHashTable(12, b7, BST)
    b3 = WillowCuttingHashTable(b8, 0, b9)
    return b2, b3
def fonk3(b1, hash_table):
    b4 = time()
    for i, value in enumerate(b1):
        hash_table[i] = value
    return time() - b4
def fonk4(hash_table, keys):
    b4 = time()
    for key in keys:
        b5 = hash_table[key]
    return time() - b4
def fonk5():
    sys.setrecursionlimit(10000)
    if len(sys.argv) != 4:
        print("Invalid Syntax\nUsage: performanceTest.py b6 chainedLoad willowLoad\n")
        sys.exit(1)
    b6 = sys.argv[1]
    b7 = int(sys.argv[2])
    b8 = int(sys.argv[3])
    b1 = fonk1(b6)
    b9 = len(b1)
    print(f"Using {b9} words")
    b2, b3 = fonk2(b9, b7, b8)
    b10 = list(range(b9))
    random.shuffle(b10)
    print("Timing put operations")
    b11 = fonk3(b1, b2)
    b12 = fonk3(b1, b3)
    print(f"Willow put time: {b12:.6f} seconds")
    print(f"Chained put time: {b11:.6f} seconds")
    print("Timing get operations (random order)")
    b13 = fonk4(b2, b10)
    b14 = fonk4(b3, b10)
    print(f"Willow get time (random): {b14:.6f} seconds")
    print(f"Chained get time (random): {b13:.6f} seconds")
    print("Timing get operations (in order)")
    b15 = list(range(b9))
    b16 = fonk4(b2, b15)
    b17 = fonk4(b3, b15)
    print(f"Willow get time (in order): {b17:.6f} seconds")
    print(f"Chained get time (in order): {b16:.6f} seconds")
if b18 = = "__main__":
    fonk5()