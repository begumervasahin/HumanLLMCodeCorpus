import sys
from operator import itemgetter
def read_distances():
    distances = []
    for line in sys.stdin:
        elements = line.strip().split()
        distances.append(elements)
    return distances
def calculate_average_of_smallest(distances, k):
    sorted_distances = sorted(distances, key=itemgetter(0))
    estimate_val = 0.0
    valid_entries = 0
    for i in range(k):
        try:
            estimate_val += float(sorted_distances[i][1])
            valid_entries += 1
        except (ValueError, IndexError):
            continue
    if valid_entries > 0:
        return estimate_val / valid_entries
    else:
        return 0.0
def main():
    k = 5
    distances = read_distances()
    average = calculate_average_of_smallest(distances, k)
    print(average)
if __name__ == "__main__":
    main()