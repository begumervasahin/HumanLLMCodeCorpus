
b1 = [0, 2, 100, 0, 120, 11]
for i in range(len(b1) - 1):
    b2 = max(b1[i:])
    b3 = b1.index(b2, i)
    if b3 != i:
        b1[i], b1[b3] = b2, b1[i]
print(b1)