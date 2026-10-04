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
        print("Invalid Syntax\nUsage: performanceTest.py filename chainedLoad willowLoad")
        sys.exit(1)
    filename, chained_load_factor, b1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    with open(filename, "r") as file:
        b2 = file.read().split()
    b3 = len(b2)
    print(f"Using {b3} b2")
    b4 = ChainedHashTable(12, chained_load_factor, BST)
    b5 = WillowCuttingHashTable(b1, 0, b3)
    b6 = list(range(b3))
    random.shuffle(b6)
    print("Timing put operations")
    b7 = fonk2(b4, b2)
    b8 = fonk2(b5, b2)
    print(f"Willow put time: {b8:.6f} seconds, Chained put time: {b7:.6f} seconds")
    print("Timing random get operations")
    b9 = fonk3(b4, b6)
    b10 = fonk3(b5, b6)
    print(f"Willow random get time: {b10:.6f} seconds, Chained random get time: {b9:.6f} seconds")
    print("Timing in-order get operations")
    b11 = fonk3(b4, range(b3))
    b12 = fonk3(b5, range(b3))
    print(f"Willow in-order get time: {b12:.6f} seconds, Chained in-order get time: {b11:.6f} seconds")
def fonk2(hash_table, b2):
    b13 = time()
    for index, word in enumerate(b2):
        hash_table[index] = word
    return time() - b13
def fonk3(hash_table, keys):
    b13 = time()
    for key in keys:
        b14 = hash_table[key]
    return time() - b13
if b15 = = "__main__":
    fonk1()