
b1 = [0, 2, 100, 0, 120, 11]
for i in range(len(b1) - 1):
    b2 = b1[i]
    b3 = i
    for j in range(i + 1, len(b1)):
        if b1[j] > b2:
            b2 = b1[j]
            b3 = j
    if b3 != i:
        b4 = b1[i]
        b1[i] = b2
        b1[b3] = b4
print(b1)