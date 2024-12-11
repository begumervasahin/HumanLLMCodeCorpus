def fonk1(n):
    b1 = []
    for number in range(2, n + 1):
        if fonk2(number):
            b1.append(number)
    return b1
def fonk2(number):
    if number <= 1:
        return False
    for b2 in range(2, int(number ** 0.5) + 1):
        if number % b2 = = 0:
            return False
    return True
b3 = fonk1(10)
print(b3)