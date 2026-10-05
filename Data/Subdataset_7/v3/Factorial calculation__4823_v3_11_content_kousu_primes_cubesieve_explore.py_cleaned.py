import math
def fonk1(a1):
    b1 = [2, 3, 5]
    b2 = [False] * (a1 + 1)
    b2[2], b2[3], b2[5] = True, True, True
    for x in range(1, int(math.sqrt(a1)) + 1):
        for y in range(1, int(math.sqrt(a1)) + 1):
            b3 = (4 * x**2) + (y**2)
            b4 = (3 * x**2) + (y**2)
            b5 = (3 * x**2) - (y**2)
            if b3 <= a1 and (b3 % b6 = = 1 or b3 % b6 == 5):
                b2[b3] = not b2[b3]
            if b4 <= a1 and b4 % b6 = = 7:
                b2[b4] = not b2[b4]
            if x > y and b5 <= a1 and b5 % b6 = = 11:
                b2[b5] = not b2[b5]
    for prime in range(5, int(math.sqrt(a1)) + 1):
        if b2[prime]:
            for k in range(prime**2, a1 + 1, prime**2):
                b2[k] = False
    for num in range(7, a1 + 1):
        if b2[num]:
            b1.append(num)
    return b1
if b7 = = "__main__":
    a1 = 15000
    b8 = fonk1(a1)
    print("Prime numbers up to", a1, ":", b8)