def fonk1(n):
    b1 = {0: 0, 1: 1}
    def fonk2(n):
        if n not in b1:
            b1[n] = fonk2(n - 1) + fonk2(n - 2)
        return b1[n]
    return fonk2(n)
def fonk3():
    for n in range(1, 47):
        b2 = fonk1(n)
        print(f"{n}\t{b2}")
if b3 = = "__main__":
    fonk3()