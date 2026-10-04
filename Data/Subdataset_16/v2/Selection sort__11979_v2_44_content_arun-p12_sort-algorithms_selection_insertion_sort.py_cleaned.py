def fonk1(b4, b1 = 0, desc=0):
    def fonk2(b4):
        if not isinstance(b4, list) or len(b4) == 0:
            raise ValueError("Expected a non-empty list. Got: {}".format(b4))
        min_val, b2 = b4[0], 0
        for i in range(1, len(b4)):
            if b4[i] < min_val:
                min_val, b2 = b4[i], i
        return min_val, b2
    def fonk3(b4):
        if len(b4) <= 1:
            return b4
        b3 = len(b4)
        val, b2 = fonk2(b4)
        while b2 > 0:
            if b1 = = 2:
                print("  sub:", b2, b4[b2], " :: ", b4)
            b4[b2] = b4[b2 - 1]
            b2 -= 1
        b4[0] = val
        if b1:
            print("iteration:", b4)
        b4 = [val] + fonk3(b4[1:])
        return b4
    b4 = fonk3(b4)
    if desc:
        b4 = b4[::-1]
    return b4
def fonk4():
    b5 = [64, 25, 12, 22, 11]
    print("Array before sorting:")
    print(b5)
    b6 = fonk1(b5, b1=1, desc=0)
    print("Sorted array is:")
    print(b6)
if b7 = = "__main__":
    fonk4()