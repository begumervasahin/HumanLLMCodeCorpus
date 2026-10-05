import sys
distances = []
estimate_val = 0.0
k = 5
for line in sys.stdin:
    line = line.strip()
    elements = line.split()
    distances.append(elements)
distances = sorted(distances)
for i in range(k):
    try:
        estimate_val += float(distances[i][1])
    except (IndexError, ValueError):
        continue
if k > 0:
    print(estimate_val / k)
else:
    print("k must be greater than 0")