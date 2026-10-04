from collections import namedtuple
import random
import bisect
b1 = namedtuple("b1", ["value", "left_child", "right_child"])
b2 = [
    1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845,
    35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650,
    1289904147324, 4861946401452
]
b3 = len(b2) - 1
b4 = [-1] * (b3 + 1)
b4[0] = b4[1] = 0
b5 = [{} for _ in range(b3 + 1)]
b5[0] = {0: 1}
b5[1] = {0: 1}
b6 = [-1] * (b3 + 1)
b6[0] = 0
b6[1] = 1
b7 = [{} for _ in range(b3 + 1)]
b7[0] = {0: 1}
b7[1] = {1: 1}
b8 = [-1] * (b3 + 1)
b8[0] = b8[1] = 0
b9 = [{} for _ in range(b3 + 1)]
b9[0] = {0: 1}
b9[1] = {0: 1}
a1 = 0
def fonk1(b10):
    global a1
    if b10 = = 0 or b10 > b3:
        return None
    b11 = b1(value=a1, left_child=None, right_child=None)
    a1 += 1
    if b10 = = 1:
        return b11
    b12 = [b2[0] * b2[b10 - 1]]
    for i in range(1, b10):
        b12.append(b12[i - 1] + b2[i] * b2[b10 - 1 - i])
    b13 = b12[-1]
    b14 = random.randint(1, b13)
    b15 = bisect.bisect_left(b12, b14)
    b11 = b11._replace(left_child=fonk1(b15))
    b11 = b11._replace(right_child=fonk1(b10 - 1 - b15))
    return b11
def fonk2(b10):
    if b10 > b3:
        return None
    if b4[b10] != -1:
        return b4[b10]
    total, b16 = 0, 0
    for i in range(b10):
        b17 = b2[i] * b2[b10 - 1 - i]
        b16 += b17
        total += b17 * max(fonk2(i), fonk2(b10 - 1 - i))
    b4[b10] = 1 + total / b16
    return b4[b10]
def fonk3(b10):
    if b10 > b3:
        return None
    if b5[b10]:
        return b5[b10]
    for i in range(b10):
        b18 = fonk3(i)
        b19 = fonk3(b10 - 1 - i)
        b17 = b2[i] * b2[b10 - 1 - i] / b2[b10]
        for left_key in b18:
            for right_key in b19:
                b20 = 1 + max(left_key, right_key)
                b5[b10][b20] = b5[b10].get(b20, 0) + b18[left_key] * b19[right_key] * b17
    return b5[b10]
def fonk4(b10):
    if b10 > b3:
        return None
    if b6[b10] != -1:
        return b6[b10]
    total, b16 = 0, 0
    for i in range(b10):
        b17 = b2[i] * b2[b10 - 1 - i]
        b16 += b17
        total += b17 * (fonk4(i) + fonk4(b10 - 1 - i))
    b6[b10] = total / b16
    return b6[b10]
def fonk5(b10):
    if b10 > b3:
        return None
    if b7[b10]:
        return b7[b10]
    for i in range(b10):
        b18 = fonk5(i)
        b19 = fonk5(b10 - 1 - i)
        b17 = b2[i] * b2[b10 - 1 - i] / b2[b10]
        for left_key in b18:
            for right_key in b19:
                b20 = left_key + right_key
                b7[b10][b20] = b7[b10].get(b20, 0) + b18[left_key] * b19[right_key] * b17
    return b7[b10]
def fonk6(b10):
    if b10 > b3:
        return None
    if b8[b10] != -1:
        return b8[b10]
    total, b16 = 0, 0
    for i in range(b10):
        b17 = b2[i] * b2[b10 - 1 - i]
        b16 += b17
        total += b17 * ((b10 - 1) + fonk6(i) + fonk6(b10 - 1 - i))
    b8[b10] = total / b16
    return b8[b10]
def fonk7(b10):
    if b10 > b3:
        return None
    if b9[b10]:
        return b9[b10]
    for i in range(b10):
        b18 = fonk7(i)
        b19 = fonk7(b10 - 1 - i)
        b17 = b2[i] * b2[b10 - 1 - i] / b2[b10]
        for left_key in b18:
            for right_key in b19:
                b20 = left_key + right_key + b10 - 1
                b9[b10][b20] = b9[b10].get(b20, 0) + b18[left_key] * b19[right_key] * b17
    return b9[b10]
def fonk8(b10):
    return fonk6(b10) / b10
def fonk9(b10):
    b21 = fonk7(b10)
    return {b20 / b10: value for b20, value in b21.items()}
if b22 = = "__main__":
    b23 = fonk1(5)
    print("Average height per node for b10 = 3:", fonk8(3))
    print("Probability b21 of average height per node for b10 = 3:", fonk9(3))