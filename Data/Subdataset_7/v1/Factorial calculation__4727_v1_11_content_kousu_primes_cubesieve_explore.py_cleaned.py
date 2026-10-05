import math
def fonk1(a1):
    b1 = [2, 3, 5]
    b2 = [False] * (a1 + 1)
    b2[2], b2[3], b2[5] = True, True, True
    for x in range(1, int(math.sqrt(a1)) + 1):
        for y in range(1, int(math.sqrt(a1)) + 1):
            b3 = (4 * x**2) + (y**2)
            if b3 <= a1 and (b3 % b4 = = 1 or b3 % b4 == 5):
                b2[b3] = not b2[b3]
            b3 = (3 * x**2) + (y**2)
            if b3 <= a1 and b3 % b4 = = 7:
                b2[b3] = not b2[b3]
            b3 = (3 * x**2) - (y**2)
            if x > y and b3 <= a1 and b3 % b4 = = 11:
                b2[b3] = not b2[b3]
    for b3 in range(5, int(math.sqrt(a1)) + 1):
        if b2[b3]:
            for k in range(b3**2, a1 + 1, b3**2):
                b2[k] = False
    for num in range(7, a1 + 1):
        if b2[num]:
            b1.append(num)
    return b1
if b5 = = "__main__":
    a1 = 15000
    b6 = fonk1(a1)
    print("Prime numbers up to", a1, ":", b6)