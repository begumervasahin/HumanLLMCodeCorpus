def fonk1(b7, b1 = 0, desc=0):
    def fonk2(left, right):
        b2 = b7[left]
        b3 = left + 1
        b4 = right
        b5 = False
        while not b5:
            while b3 <= b4 and b7[b3] <= b2:
                b3 += 1
            while b7[b4] >= b2 and b4 >= b3:
                b4 -= 1
            if b4 < b3:
                b5 = True
            else:
                b7[b3], b7[b4] = b7[b4], b7[b3]
        b7[left], b7[b4] = b7[b4], b7[left]
        return b4
    def fonk3(left, right):
        if left < right:
            b6 = fonk2(left, right)
            if b1:
                print("Iteration:", b6, left, right, "::", b7)
            fonk3(left, b6 - 1)
            fonk3(b6 + 1, right)
    fonk3(0, len(b7) - 1)
    if desc:
        b7 = b7[::-1]
    return b7