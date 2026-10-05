import sys
def main():
    distances = []
    for line in sys.stdin:
        line = line.strip()
        elements = line.split()
        if len(elements) >= 2:
            distances.append((float(elements[0]), float(elements[1])))
    k = 5
    if k <= 0:
        print("k must be greater than 0")
        return
    distances.sort(key=lambda x: x[0])
    total = sum(value for _, value in distances[:k])
    print(total / k)
if __name__ == "__main__":
    main()