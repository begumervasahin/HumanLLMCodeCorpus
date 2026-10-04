def fonk1(num):
    if num < 2:
        return False
    for b1 in range(2, int(num ** 0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(n):
    b2 = []
    for num in range(2, n + 1):
        if fonk1(num):
            b2.append(num)
    return b2
print(fonk2(10))