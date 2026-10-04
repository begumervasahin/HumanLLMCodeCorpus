b1 = [6, 2, 7, 8, 3, 1, 10, 5, 4, 9]
b2 = []
while b1:
    b3 = min(b1)
    b1.remove(b3)
    b2.append(b3)
print(b2)