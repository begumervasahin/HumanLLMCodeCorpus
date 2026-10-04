
b1 = {}
def fonk1(b2):
    if type(b2) != int:
        return False
    if b2 in b1:
        return b1[b2]
    if b2 = = 0:
        return 1
    elif b2 = = 1:
        return 1
    else:
        b3 = fonk1(b2 - 1) + fonk1(b2 - 2)
        b1[b2] = b3
        return b3
for b2 in range(1000):
    print(f"{b2}: {fonk1(b2)}")