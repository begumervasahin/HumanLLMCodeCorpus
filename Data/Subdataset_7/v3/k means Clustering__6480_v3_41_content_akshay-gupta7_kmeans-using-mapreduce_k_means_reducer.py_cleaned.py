import sys
a1 = 5
b1 = [0.0] * a1
b2 = [0.0] * a1
b3 = [0] * a1
for line in sys.stdin:
    centroid_id, salary, b4 = map(float, line.strip().split("\t"))
    b1[int(centroid_id)] += salary
    b2[int(centroid_id)] += b4
    b3[int(centroid_id)] += 1
b5 = []
for i in range(a1):
    if b3[i] != 0:
        b6 = b1[i] / b3[i]
        b7 = b2[i] / b3[i]
        b5.append((i, b6, b7))
with open("b5.txt", "w") as file1:
    for centroid_id, b6, b7 in b5:
        file1.write(f"{centroid_id}\t{b6};{b7}\n")