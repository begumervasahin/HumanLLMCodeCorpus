
b1 = {}
def fonk1(b2):
    if not isinstance(b2, int):
        raise ValueError("The input must be an integer.")
    if b2 in b1:
        return b1[b2]
    if b2 = = 0:
        a1 = 1
    elif b2 = = 1:
        a1 = 1
    else:
        a1 = fonk1(b2 - 1) + fonk1(b2 - 2)
    b1[b2] = a1
    return a1
def fonk2():
    for b2 in range(1000):
        print(f"{b2}: {fonk1(b2)}")
if b3 = = "__main__":
    fonk2()