
b1 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for i in range(len(b1)):
    for j in range(len(b1) - 1):
        if b1[j] > b1[j + 1]:
            b1[j], b1[j + 1] = b1[j + 1], b1[j]
print("Sorted array:")
print(b1)