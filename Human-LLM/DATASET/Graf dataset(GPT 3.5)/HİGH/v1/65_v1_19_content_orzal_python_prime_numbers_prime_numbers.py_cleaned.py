def fonk1(num):
    if num < 2:
        return False
    for b1 in range(2, int(num ** 0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
for n in range(2, 100):
    if fonk1(n):
        print(n, 'is a prime number')
    else:
        for b2 in range(2, n):
            if n % b2 = = 0:
                print(n, 'equals', b2, '*', n
                break