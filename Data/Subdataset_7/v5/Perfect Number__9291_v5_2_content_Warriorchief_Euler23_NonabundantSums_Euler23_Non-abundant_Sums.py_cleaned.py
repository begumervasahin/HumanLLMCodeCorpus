import math
def fonk1(x):
    b1 = []
    for b2 in range(1, math.ceil(x / 2) + 1):
        if x % b2 = = 0:
            b1.append(b2)
    return sum(b1)
def fonk2(a1):
    b3 = []
    for k in range(11, a1):
        if fonk1(k) > k:
            b3.append(k)
    return b3
def fonk3(b3):
    b4 = set()
    for b2 in range(len(b3)):
        for j in range(b2, len(b3)):
            if b3[b2] + b3[j] < 28123:
                b4.add(b3[b2] + b3[j])
    return b4
def fonk4(a1):
    b3 = fonk2(a1)
    b4 = fonk3(b3)
    b5 = sum(b2 for b2 in range(a1) if b2 not in b4)
    return b5
def fonk5():
    a1 = 28123
    b6 = fonk4(a1)
    print("The b6 to this question should be", b6)
if b7 = = "__main__":
    fonk5()