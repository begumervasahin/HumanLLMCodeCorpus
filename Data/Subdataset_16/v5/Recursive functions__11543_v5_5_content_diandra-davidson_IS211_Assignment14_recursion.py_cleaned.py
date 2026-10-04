
def fonk1(a1):
    if a1 <= 1:
        return a1
    return fonk1(a1 - 1) + fonk1(a1 - 2)
def fonk2(a, b1):
    if b1 = = 0:
        return a
    return fonk2(b1, a % b1)
def fonk3(b2, b3):
    if not b2 and not b3:
        return 0
    if not b2:
        return -len(b3)
    if not b3:
        return len(b2)
    if b2[0] == b3[0]:
        return fonk3(b2[1:], b3[1:])
    if b2[0] < b3[0]:
        return -1
    return 1
def fonk4():
    a1 = 10
    print(f"Fibonacci of {a1}: {fonk1(a1)}")
    a, b1 = 48, 18
    print(f"GCD of {a} and {b1}: {fonk2(a, b1)}")
    b2 = "apple"
    b3 = "apricot"
    print(f"Comparison of '{b2}' and '{b3}': {fonk3(b2, b3)}")
if b4 = = "__main__":
    fonk4()