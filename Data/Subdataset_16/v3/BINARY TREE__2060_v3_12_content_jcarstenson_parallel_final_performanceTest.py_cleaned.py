import sys
import random
from time import time
from BST import BST
from linkedList import LinkedList as LL
from willowCuttingHashTable import WillowCuttingHashTable
from chainedHashTable import ChainedHashTable
def fonk1(b4):
    with open(b4, "r") as file:
        b1 = file.read().split()
    return b1
def fonk2(hash_table, b1):
    b2 = time()
    for i, value in enumerate(b1):
        hash_table[i] = value
    return time() - b2
def fonk3(hash_table, keys, description):
    b2 = time()
    for key in keys:
        b3 = hash_table[key]
    return time() - b2
def fonk4():
    sys.setrecursionlimit(10000)
    if len(sys.argv) != 4:
        print("Invalid Syntax\nUsage: performanceTest.py b4 chainedLoad willowLoad\n")
        sys.exit(1)
    b4 = sys.argv[1]
    b5 = int(sys.argv[2])
    b6 = int(sys.argv[3])
    b1 = fonk1(b4)
    b7 = len(b1)
    print(f"Using {b7} words")
    b8 = ChainedHashTable(12, b5, BST)
    b9 = WillowCuttingHashTable(b6, 0, b7)
    b10 = list(range(b7))
    random.shuffle(b10)
    print("Timing put")
    b11 = fonk2(b8, b1)
    b12 = fonk2(b9, b1)
    print(f"Chained put time: {b11:.6f} seconds | Willow put time: {b12:.6f} seconds")
    print("Timing get (random)")
    b13 = fonk3(b8, b10, "random")
    b14 = fonk3(b9, b10, "random")
    print(f"Chained get (random) time: {b13:.6f} seconds | Willow get (random) time: {b14:.6f} seconds")
    print("Timing get (in order)")
    b15 = fonk3(b8, range(b7), "in order")
    b16 = fonk3(b9, range(b7), "in order")
    print(f"Chained get (in order) time: {b15:.6f} seconds | Willow get (in order) time: {b16:.6f} seconds")
if b17 = = "__main__":
    fonk4()