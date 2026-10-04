def fonk1(n):
    if n < 2:
        return []
    def fonk2(num):
        if num < 2:
            return False
        for b1 in range(2, int(num ** 0.5) + 1):
            if num % b1 = = 0:
                return False
        return True
    b2 = [number for number in range(2, n + 1) if fonk2(number)]
    return b2
print(fonk1(10))