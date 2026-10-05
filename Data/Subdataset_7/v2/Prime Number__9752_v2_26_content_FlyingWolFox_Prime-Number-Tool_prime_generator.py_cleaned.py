
a1 = 2
b1 = [1]
a2 = 0
while a1 <= 3001:
    a3 = 0
    b2 = b1[a3]
    while b2 < a1:
        b3 = a1 % b2
        if b3 = = 0:
            a2 += 1
            break
        a3 += 1
        if a3 + 1 > len(b1):
            break
        b2 = b1[a3]
    if a2 = = 0:
        print(a1, "is prime")
        b1.append(a1)
    if a1 = = 2:
        a1 += 1
    else:
        a1 += 2
    a2 = 0
