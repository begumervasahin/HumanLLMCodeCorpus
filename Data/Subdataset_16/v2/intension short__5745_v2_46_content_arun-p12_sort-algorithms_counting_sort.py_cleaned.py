def fonk1(b3, b1 = 0, desc=False):
    if not b3:
        return []
    smallest, b2 = min(b3), max(b3)
    if smallest < 0:
        b3 = [x - smallest for x in b3]
    if b1:
        print("Normalized array:", b3)
    b4 = b2 - smallest + 1
    b5 = [0] * b4
    for number in b3:
        b5[number] += 1
    for i in range(1, len(b5)):
        b5[i] += b5[i - 1]
        if b1 = = 2:
            print(f"Count array at index {i}: {b5}")
    b6 = [0] * len(b3)
    for i in range(len(b3) - 1, -1, -1):
        b7 = b3[i]
        b5[b7] -= 1
        b6[b5[b7]] = b7
    if smallest < 0:
        b6 = [x + smallest for x in b6]
    if desc:
        b6.reverse()
    return b6
if b8 = = "__main__":
    b9 = [4, 2, 2, 8, 3, 3, 1]
    b10 = fonk1(b9, b1=1)
    print("Sorted array:", b10)