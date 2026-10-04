def fonk1(n):
    if n < 2:
        return []
    b1 = []
    for current_number in range(2, n + 1):
        b2 = True
        for b3 in range(2, int(current_number ** 0.5) + 1):
            if current_number % b3 = = 0:
                b2 = False
                break
        if b2:
            b1.append(current_number)
    return b1
print(fonk1(10))