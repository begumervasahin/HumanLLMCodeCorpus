import sys
import operator
def main():
    storage = {}
    for line in sys.stdin:
        value, key = line.split()
        storage[key] = int(value)
    sorted_storage = sorted(storage.items(), key=operator.itemgetter(1), reverse=True)
    for key, value in sorted_storage:
        print(f"{key},{value}")
if __name__ == "__main__":
    main()