def fonk1(num):
    if not isinstance(num, int) or num < 0:
        return 'Argument must be a non-negative integer'
    b1 = []
    for i in range(2, num + 1):
        b2 = True
        for b3 in range(2, int(i ** 0.5) + 1):
            if i % b3 = = 0:
                b2 = False
                break
        if b2:
            b1.append(i)
    return b1
b4 = fonk1(20)
print(b4)