def fonk1() -> None:
    a1 = 3
    a2 = 7
    b1 = [8, 6, 7, 5, 3, 0, 9]
    for _ in range(10):
        for b2 in range(len(b1)):
            if b2 = = 0:
                b3 = (b1[a1 - 1] + b1[a2 - 1]) % 10
            elif 0 < b2 < len(b1) - 1:
                b1[b2] = b1[b2 + 1]
            else:
                b1[b2] = b3
                print(b1[b2])
if b4 = = "__main__":
    fonk1()