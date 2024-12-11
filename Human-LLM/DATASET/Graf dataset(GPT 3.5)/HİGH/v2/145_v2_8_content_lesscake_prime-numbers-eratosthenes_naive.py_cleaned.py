def fonk1(limit):
    b1 = []
    for number in range(2, limit + 1):
        if fonk2(number):
            b1.append(number)
    return b1
def fonk2(number):
    if number < 2:
        return False
    for b2 in range(2, int(number ** 0.5) + 1):
        if number % b2 = = 0:
            return False
    return True
if b3 = = '__main__':
    b4 = fonk1(100)
    print(b4)