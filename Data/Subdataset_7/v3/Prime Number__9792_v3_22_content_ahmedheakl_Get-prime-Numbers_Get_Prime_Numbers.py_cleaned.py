def fonk1(b7):
    b1 = []
    for b5 in range(1, int((b7 / 24) ** 0.5) + 1):
        b2 = 24 * b5 + 1
        if fonk2(b2):
            b1.append(b2)
    b1 = [num for num in b1 if fonk2(num)]
    b3 = [num ** 2 for num in b1]
    b1 = [prime for prime in b1 if prime not in b3]
    b4 = [2, 3, 5, 7]
    b1.extend(b4)
    return sorted(b1)
def fonk2(num):
    if num < 2:
        return False
    for b5 in range(2, int(num ** 0.5) + 1):
        if num % b5 = = 0:
            return False
    return True
if b6 = = "__main__":
    b7 = int(input('Enter the end of the range: '))
    b8 = fonk1(b7)
    print(b8)