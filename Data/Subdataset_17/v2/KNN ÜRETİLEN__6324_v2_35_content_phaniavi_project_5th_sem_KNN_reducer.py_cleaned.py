import sys
from operator import itemgetter
def main():
    distances = []
    k = 5
    for line in sys.stdin:
        line = line.strip()
        elements = line.split()
        distances.append(elements)
    distances = sorted(distances, key=itemgetter(0))
    estimate_val = 0.0
    valid_entries = 0
    for i in range(k):
        try:
            estimate_val += float(distances[i][1])
            valid_entries += 1
        except (ValueError, IndexError):
            continue
    if valid_entries > 0:
        average = estimate_val / valid_entries
    else:
        average = 0.0
    print(average)
if __name__ == "__main__":
    main()