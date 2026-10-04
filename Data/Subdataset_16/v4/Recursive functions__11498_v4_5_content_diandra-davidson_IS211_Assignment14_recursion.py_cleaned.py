
def fonk1(a1):
    if a1 <= 1:
        return a1
    else:
        return fonk1(a1 - 1) + fonk1(a1 - 2)
def fonk2(a, b1):
    if b1 = = 0:
        return a
    else:
        return fonk2(b1, a % b1)
def fonk3(b3, b4):
    if not b3 and not b4:
        return 0
    if not b3:
        return -len(b4)
    if not b4:
        return len(b3)
    if b3[0] == b4[0]:
        return fonk3(b3[1:], b4[1:])
    elif b3[0] < b4[0]:
        return -1 + fonk3(b3[1:], b4[1:])
    else:
        return 1 + fonk3(b3[1:], b4[1:])
if b2 = = "__main__":
    a1 = 10
    print(f"Fibonacci of {a1}: {fonk1(a1)}")
    a, b1 = 48, 18
    print(f"GCD of {a} and {b1}: {fonk2(a, b1)}")
    b3 = "apple"
    b4 = "apricot"
    print(f"Comparison of '{b3}' and '{b4}': {fonk3(b3, b4)}")