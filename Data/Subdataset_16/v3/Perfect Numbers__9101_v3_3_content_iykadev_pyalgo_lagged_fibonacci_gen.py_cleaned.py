def fonk1(b3: list, a1: int, a2: int, a3: int) -> None:
    for _ in range(a3):
        for b1 in range(len(b3)):
            if b1 = = 0:
                b2 = (b3[a1 - 1] + b3[a2 - 1]) % 10
            elif 0 < b1 < len(b3) - 1:
                b3[b1] = b3[b1 + 1]
            else:
                b3[b1] = b2
                print(b3[b1])
def fonk2() -> None:
    a1 = 3
    a2 = 7
    b3 = [8, 6, 7, 5, 3, 0, 9]
    a3 = 10
    print("Original list:", b3)
    fonk1(b3, a1, a2, a3)
    print("Transformed list:", b3)
if b4 = = "__main__":
    fonk2()