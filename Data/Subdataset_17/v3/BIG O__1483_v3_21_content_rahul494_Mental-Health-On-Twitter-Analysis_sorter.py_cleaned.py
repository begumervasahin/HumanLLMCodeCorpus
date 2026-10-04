import sys
import operator
def read_input():
    storage = {}
    for line in sys.stdin:
        value, key = line.split()
        storage[key] = int(value)
    return storage
def sort_storage(storage):
    return sorted(storage.items(), key=operator.itemgetter(1), reverse=True)
def print_sorted_storage(sorted_storage):
    for key, value in sorted_storage:
        print(f"{key},{value}")
def main():
    storage = read_input()
    sorted_storage = sort_storage(storage)
    print_sorted_storage(sorted_storage)
if __name__ == "__main__":
    main()