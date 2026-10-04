
b1 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for i in range(0, 9):
    for j in range(0, 9):
        if b1[j] > b1[i]:
            b2 = b1[i]
            b1[i] = b1[j]
            b1[j] = b2
print(b1)
print("\n")