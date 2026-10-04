
b1 = [6, 2, 7, 8, 3, 1, 10, 5, 4, 9]
b2 = []
while b1:
    b3 = b1[0]
    a1 = 0
    for i, value in enumerate(b1):
        if value < b3:
            b3 = value
            a1 = i
    b2.append(b1.pop(a1))
print(b2)