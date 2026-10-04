def fonk1(b4, b1 = 0, desc=0):
    def fonk2(b4):
        from common import minimum
        if len(b4) <= 1:
            return b4
        b2 = len(b4)
        val, b3 = minimum(b4)
        while b3 > 0:
            if b1 = = 2:
                print("  sub:", b3, b4[b3], " :: ", b4)
            b4[b3] = b4[b3 - 1]
            b3 -= 1
        b4[0] = val
        if b1:
            print("iter:", b4)
        b4 = [val] + fonk2(b4[1:])
        return b4
    b4 = fonk2(b4)
    if desc:
        b4 = b4[::-1]
    return b4
if b5 = = "__main__":
    b6 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    b7 = fonk1(b6, b1=1, desc=0)
    print("Sorted list:", b7)