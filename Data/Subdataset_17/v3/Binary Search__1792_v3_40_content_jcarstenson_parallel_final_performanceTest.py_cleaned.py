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
    chained_load_factor = int(sys.argv[2])
    willow_load_factor = int(sys.argv[3])
    with open(filename, "r") as file:
        words = file.read().split()
    word_count = len(words)
    print(f"Using {word_count} words")
    chained_table = ChainedHashTable(12, chained_load_factor, BST)
    willow_table = WillowCuttingHashTable(willow_load_factor, 0, word_count)
    shuffled_indices = list(range(word_count))
    random.shuffle(shuffled_indices)
    print("Timing put operations...")
    chained_put_time = measure_time(lambda: put_words(chained_table, words))
    willow_put_time = measure_time(lambda: put_words(willow_table, words))
    print(f"Chained insertion time: {chained_put_time:.6f} seconds")
    print(f"Willow insertion time: {willow_put_time:.6f} seconds")
    print("Timing random access (get) operations...")
    chained_get_random_time = measure_time(lambda: get_words(chained_table, shuffled_indices))
    willow_get_random_time = measure_time(lambda: get_words(willow_table, shuffled_indices))
    print(f"Chained random access time: {chained_get_random_time:.6f} seconds")
    print(f"Willow random access time: {willow_get_random_time:.6f} seconds")
    print("Timing in-order access (get) operations...")
    chained_get_order_time = measure_time(lambda: get_words_in_order(chained_table, word_count))
    willow_get_order_time = measure_time(lambda: get_words_in_order(willow_table, word_count))
    print(f"Chained in-order access time: {chained_get_order_time:.6f} seconds")
    print(f"Willow in-order access time: {willow_get_order_time:.6f} seconds")
def put_words(table, words):
    for i, word in enumerate(words):
        table[i] = word
def get_words(table, indices):
    for i in indices:
        _ = table[i]
def get_words_in_order(table, count):
    for i in range(count):
        _ = table[i]
def measure_time(operation):
    start_time = time()
    operation()
    return time() - start_time
if __name__ == "__main__":
    main()