
b1 = int(input('Enter the end of the range: '))
b2 = []
a1 = 0
for b4 in range(b3, 1000000000000000000):
    a1 = (24 * b4 + b3) ** 0.5
    if a1 % b3 = = 0 and int(a1) < b1:
        b2.append(int(a1))
    elif int(a1) > b1:
        break
for b4 in range(2, 10):
    for b5 in b2:
        if b5 % b4 = = 0:
            b2.remove(b5)
b5 = [y ** 2 for y in b2]
for b4 in b5:
    for b6 in b2:
        if b6 = = b4:
            b2.remove(b6)
b7 = [2, 3, 5, 7]
b2 = b2 + b7
print(sorted(b2))