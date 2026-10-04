import sys
from operator import itemgetter
def main():
    distances = []
    estimate_val = 0.0
    k = 5
    for line in sys.stdin:
        line = line.strip()
        elements = line.split()
        distances.append(elements)
    distances.sort(key=itemgetter(0))
    for i in range(k):
        try:
            estimate_val += float(distances[i][1])
        except ValueError:
            continue
    print(estimate_val / k)
if __name__ == "__main__":
    main()