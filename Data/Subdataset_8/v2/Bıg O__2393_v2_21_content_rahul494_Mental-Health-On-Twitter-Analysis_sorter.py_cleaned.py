import sys
import csv
import operator
storage = {}
for line in sys.stdin:
    value, key = line.split()
    storage[key] = int(value)
sorted_storage = sorted(storage.items(), key=operator.itemgetter(1), reverse=True)
for key, value in sorted_storage:
    print(f"{key},{value}")