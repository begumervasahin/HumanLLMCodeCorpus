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
        words = f.read().split()
    word_count = len(words)
    print(f"Using {word_count} words")
    chained_table = ChainedHashTable(12, chainedLoad, BST)
    willow_table = WillowCuttingHashTable(willowLoad, 0, word_count)
    shuffled_indices = list(range(word_count))
    random.shuffle(shuffled_indices)
    print("Timing put operations...")
    start_time = time()
    for i in range(word_count):
        chained_table[i] = words[i]
    chained_put_time = time() - start_time
    start_time = time()
    for i in range(word_count):
        willow_table[i] = words[i]
    willow_put_time = time() - start_time
    print(f"Willow insertion time: {willow_put_time:.6f} seconds")
    print(f"Chained insertion time: {chained_put_time:.6f} seconds")
    print("Timing random access (get) operations...")
    start_time = time()
    for i in shuffled_indices:
        _ = chained_table[i]
    chained_get_random_time = time() - start_time
    start_time = time()
    for i in shuffled_indices:
        _ = willow_table[i]
    willow_get_random_time = time() - start_time
    print(f"Willow random access time: {willow_get_random_time:.6f} seconds")
    print(f"Chained random access time: {chained_get_random_time:.6f} seconds")
    print("Timing in-order access (get) operations...")
    start_time = time()
    for i in range(word_count):
        _ = chained_table[i]
    chained_get_order_time = time() - start_time
    start_time = time()
    for i in range(word_count):
        _ = willow_table[i]
    willow_get_order_time = time() - start_time
    print(f"Willow in-order access time: {willow_get_order_time:.6f} seconds")
    print(f"Chained in-order access time: {chained_get_order_time:.6f} seconds")
if __name__ == "__main__":
    main()