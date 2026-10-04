from b1 import div_rule
def fonk1(b6, a2):
    b1 = div_rule(a2)
    a1 = 0
    b2 = b6[::-1]
    for digit in b2:
        b3 = next(b1)
        a1 += int(digit) * b3
        print(f"Intermediate a1 after processing digit {digit}: {a1}")
        if abs(a1) > 3 * a2:
            if a1 > 0:
                a1 -= 3 * a2
            else:
                a1 += 3 * a2
            print(f"Adjusted a1 to keep it within bounds: {a1}")
    b4 = a1 % a2 == 0
    return b4
if b5 = = "__main__":
    b6 = "1946"
    a2 = 7
    b7 = fonk1(b6, a2)
    if b7:
        print(f"The b6 {b6} is divisible by {a2}.")
    else:
        print(f"The b6 {b6} is not divisible by {a2}.")