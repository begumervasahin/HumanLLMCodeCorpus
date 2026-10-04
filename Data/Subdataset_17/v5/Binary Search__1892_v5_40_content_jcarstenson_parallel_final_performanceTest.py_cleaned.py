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
        print("Invalid Syntax\nUsage: performanceTest.py filename chainedLoad willowLoad")
        sys.exit(1)
    filename, chained_load_factor, willow_load_factor = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    with open(filename, "r") as file:
        words = file.read().split()
    total_words = len(words)
    print(f"Using {total_words} words")
    chained_hash_table = ChainedHashTable(12, chained_load_factor, BST)
    willow_hash_table = WillowCuttingHashTable(willow_load_factor, 0, total_words)
    shuffled_keys = list(range(total_words))
    random.shuffle(shuffled_keys)
    print("Timing put operations")
    chained_put_time = measure_put_time(chained_hash_table, words)
    willow_put_time = measure_put_time(willow_hash_table, words)
    print(f"Willow put time: {willow_put_time:.6f} seconds, Chained put time: {chained_put_time:.6f} seconds")
    print("Timing random get operations")
    chained_get_random_time = measure_get_time(chained_hash_table, shuffled_keys)
    willow_get_random_time = measure_get_time(willow_hash_table, shuffled_keys)
    print(f"Willow random get time: {willow_get_random_time:.6f} seconds, Chained random get time: {chained_get_random_time:.6f} seconds")
    print("Timing in-order get operations")
    chained_get_order_time = measure_get_time(chained_hash_table, range(total_words))
    willow_get_order_time = measure_get_time(willow_hash_table, range(total_words))
    print(f"Willow in-order get time: {willow_get_order_time:.6f} seconds, Chained in-order get time: {chained_get_order_time:.6f} seconds")
def measure_put_time(hash_table, words):
    start_time = time()
    for index, word in enumerate(words):
        hash_table[index] = word
    return time() - start_time
def measure_get_time(hash_table, keys):
    start_time = time()
    for key in keys:
        _ = hash_table[key]
    return time() - start_time
if __name__ == "__main__":
    main()