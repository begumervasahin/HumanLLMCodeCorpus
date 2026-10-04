def fonk1(number):
    if number < 2:
        return False
    for b1 in range(2, int(number ** 0.5) + 1):
        if number % b1 = = 0:
            return False
    return True
def fonk2(limit):
    return [num for num in range(2, limit + 1) if fonk1(num)]
if b2 = = '__main__':
    a1 = 100
    b3 = fonk2(a1)
    print(f"Prime numbers up to {a1}: {b3}")