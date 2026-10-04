import sys
from operator import itemgetter
def main():
    distances = []
    k = 5
    for line in sys.stdin:
        line = line.strip()
        elements = line.split()
        distances.append(elements)
    distances.sort(key=itemgetter(0))
    estimate_sum = 0.0
    count = 0
    for i in range(k):
        try:
            estimate_sum += float(distances[i][1])
            count += 1
        except (ValueError, IndexError):
            continue
    if count > 0:
        print(estimate_sum / count)
    else:
        print("No valid estimates found in the input.")
if __name__ == "__main__":
    main()