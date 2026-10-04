
b1 = [6, 2, 7, 8, 3, 1, 10, 5, 4, 9]
b2 = []
while b1:
    b3 = b1[0]
    a1 = 0
    for i in range(len(b1)):
        if b1[i] < b3:
            b3 = b1[i]
            a1 = i
    del b1[a1]
    b2.append(b3)
print(b2)