def fonk1(n):
    b1 = []
    for num in range(2, n + 1):
        b2 = True
        for b3 in range(2, int(num ** 0.5) + 1):
            if num % b3 = = 0:
                b2 = False
                break
        if b2:
            b1.append(num)
    return b1
print(fonk1(10))