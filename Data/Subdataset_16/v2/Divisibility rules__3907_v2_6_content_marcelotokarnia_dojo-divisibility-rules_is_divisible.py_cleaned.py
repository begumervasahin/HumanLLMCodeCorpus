from b1 import div_rule
def fonk1(b6, b4):
    b1 = div_rule(b4)
    a1 = 0
    b2 = b6[::-1]
    for digit in b2:
        b3 = next(b1)
        a1 += int(digit) * b3
        print(a1)
        if abs(a1) > 3 * b4:
            if a1 > 0:
                a1 -= 3 * b4
            else:
                a1 += 3 * b4
    return a1 % b4 = = 0
if b5 = = "__main__":
    b6 = "1946"
    b4 = 7
    b7 = fonk1(b6, b4)
    if b7:
        print(f"The b6 {b6} is divisible by {b4}.")
    else:
        print(f"The b6 {b6} is not divisible by {b4}.")