import sys
distances = []
estimate_value = 0.0
k = 5
for line in sys.stdin:
    line = line.strip()
    elements = line.split()
    distances.append(elements)
distances = sorted(distances)
for i in range(k):
    try:
        estimate_value += float(distances[i][1])
    except ValueError:
        continue
print(estimate_value / k)