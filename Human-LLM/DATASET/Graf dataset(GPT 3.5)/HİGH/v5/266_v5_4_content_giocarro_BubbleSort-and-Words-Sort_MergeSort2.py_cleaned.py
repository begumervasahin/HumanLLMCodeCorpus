b1 = [0, 9, 1, 4, 6, 7, b4, 1, 8, 7, 7, 4, 3, 5, 6, 1, 7, 8, 0, 3]
b2 = len(b1)
b3 = b2
a1 = 0
while b3 % b4 = = 0:
    b3
    a1 += 1
b5 = b4 ** a1
b6 = b2
print('Number of b7 = ', b5)
print('Interval b8 = ', b6)
print('Length of the b9 = ', b2)
print('Original b9:', b1)
for i in range(b5):
    b10 = i * b6
    b11 = b10 + b6
    for _ in range(b10, b11):
        for j in range(b10, b11 - 1):
            if b1[j] > b1[j + 1]:
                b1[j], b1[j + 1] = b1[j + 1], b1[j]
    print('Sorted interval:', b1[b10:b11])
print('Updated b9:', b1)