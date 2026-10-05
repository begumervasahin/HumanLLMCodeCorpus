
from b1 import div_rule
def fonk1(b2, b4):
    b1 = div_rule(b4)
    a1 = 0
    b2 = b2[::-1]
    for digit in b2:
        b3 = next(b1)
        a1 += int(digit) * b3
        if abs(a1) > 3 * b4:
            a1 %= 3 * b4
    return a1 % b4 = = 0
a2 = 123456
a3 = 7
b5 = fonk1(a2, a3)
print(b5)
