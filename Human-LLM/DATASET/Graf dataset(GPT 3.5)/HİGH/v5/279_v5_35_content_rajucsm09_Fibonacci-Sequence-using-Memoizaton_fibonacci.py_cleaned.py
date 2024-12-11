
b1 = {}
def fonk1(b2):
    if not isinstance(b2, int) or b2 < 0:
        return "Invalid input: Please provide a non-negative integer."
    if b2 in b1:
        return b1[b2]
    if b2 = = 0:
        a1 = 0
    elif b2 = = 1:
        a1 = 1
    else:
        a1 = fonk1(b2 - 1) + fonk1(b2 - 2)
        b1[b2] = a1
    return a1
def fonk2(b2):
    for i in range(b2):
        print(f"Fibonacci({i}): {fonk1(i)}")
fonk2(1000)