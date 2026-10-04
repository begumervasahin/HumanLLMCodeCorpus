def fonk1(n, b1 = {0: 0, 1: 1}):
    if n not in b1:
        b1[n] = fonk1(n - 1, b1) + fonk1(n - 2, b1)
    return b1[n]
def fonk2(a1):
    for n in range(1, a1 + 1):
        b2 = fonk1(n)
        print(f"{n}\t{b2}")
def fonk3():
    a1 = 46
    fonk2(a1)
if b3 = = "__main__":
    fonk3()