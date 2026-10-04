def fonk1(n, b1 = {}):
    if n in b1:
        return b1[n]
    if n <= 1:
        return n
    b1[n] = fonk1(n - 1, b1) + fonk1(n - 2, b1)
    return b1[n]
def fonk2():
    for n in range(1, 47):
        b2 = fonk1(n)
        print(f"{n}\t{b2}")
if b3 = = "__main__":
    fonk2()