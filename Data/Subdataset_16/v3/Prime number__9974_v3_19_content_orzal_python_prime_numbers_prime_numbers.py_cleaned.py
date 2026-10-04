def fonk1(n):
    if n < 2:
        return False
    for b1 in range(2, int(n ** 0.5) + 1):
        if n % b1 = = 0:
            return False
    return True
def fonk2(limit):
    for n in range(2, limit):
        if fonk1(n):
            print(f"{n} is a prime number")
        else:
            for b1 in range(2, int(n ** 0.5) + 1):
                if n % b1 = = 0:
                    print(f"{n} equals {b1} * {n
                    break
fonk2(100)