import sys
b1 = [0.0] * 5
b2 = [0.0] * 5
b3 = [0] * 5
for line in sys.stdin:
    b4 = line.strip().split("\t")
    b7, salary, b5 = map(float, b4)
    b1[int(b7)] += salary
    b2[int(b7)] += b5
    b3[int(b7)] += 1
b6 = []
for i in range(len(b3)):
    if b3[i] != 0:
        b7 = i
        b8 = b1[i] / b3[i]
        b9 = b2[i] / b3[i]
        b6.append((b7, b8, b9))
with open("b6.txt", "w") as file1:
    for cluster in b6:
        b7, b8, b9 = cluster
        file1.write(f"{b7}\t{b8};{b9}\n")