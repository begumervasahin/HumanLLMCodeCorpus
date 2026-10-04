def fonk1(b5, b1 = 0, desc=0):
    def fonk2(b5):
        if not isinstance(b5, list) or len(b5) == 0:
            print("List expected. Got:", b5)
            exit(1)
        b3, b2 = b5[0], 0
        for i in range(1, len(b5)):
            if b5[i] < b3:
                b3 = b5[i]
                b2 = i
        return (b3, b2)
    def fonk3(b5):
        if len(b5) <= 1:
            return b5
        b4 = len(b5)
        val, b2 = fonk2(b5)
        while b2 > 0:
            if b1 = = 2:
                print("  sub:", b2, b5[b2], " :: ", b5)
            b5[b2] = b5[b2 - 1]
            b2 -= 1
        b5[0] = val
        if b1:
            print("iteration:", b5)
        b5 = [val] + fonk3(b5[1:])
        return b5
    b5 = fonk3(b5)
    if desc:
        b5 = b5[::-1]
    return b5
if b6 = = "__main__":
    b7 = [64, 25, 12, 22, 11]
    print("Array before sorting:")
    print(b7)
    b8 = fonk1(b7, b1=1, desc=0)
    print("Sorted array is:")
    print(b8)