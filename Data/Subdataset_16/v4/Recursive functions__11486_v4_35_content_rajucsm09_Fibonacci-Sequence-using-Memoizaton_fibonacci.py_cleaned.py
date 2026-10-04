
b1 = {}
def fonk1(b2):
    if not isinstance(b2, int):
        return False
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
for b2 in range(1000):
    print(f"{b2}: {fonk1(b2)}")