def fonk1(b5, b1 = 0, desc=False):
    b2 = len(b5)
    for i in range(1, b2):
        b3 = b5[i]
        b4 = i - 1
        while b4 >= 0 and b5[b4] > b3:
            b5[b4 + 1] = b5[b4]
            b4 -= 1
            if b1 = = 2:
                print("  sub:", b4, " :: ", b5)
        b5[b4 + 1] = b3
        if b1 >= 1:
            print(f"Iteration {i}: {b5}")
    if desc:
        b5 = b5[::-1]
    return b5
if b6 = = "__main__":
    b7 = [12, 11, 13, 5, 6]
    b8 = fonk1(b7, b1=1, desc=False)
    print("Sorted array:", b8)