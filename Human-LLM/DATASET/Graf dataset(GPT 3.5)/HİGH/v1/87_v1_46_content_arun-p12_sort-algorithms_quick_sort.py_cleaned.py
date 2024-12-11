def fonk1(b4, b1 = 0, desc=0):
    def fonk2(lb, ub):
        pivot, start, b2 = b4[lb], lb, ub
        while start < b2:
            while b4[start] <= pivot and start < ub:
                start += 1
            while b4[b2] > pivot and b2 > lb:
                b2 -= 1
            if start < b2:
                b4[start], b4[b2] = b4[b2], b4[start]
            if b1 = = 2:
                print("Sub:", pivot, start, b2, "::", b4)
        b4[lb], b4[b2] = b4[b2], b4[lb]
        return b2
    def fonk3(x, y):
        if x < y:
            b3 = fonk2(x, y)
            if b1:
                print("Iteration:", b3, x, y, "::", b4)
            fonk3(x, b3 - 1)
            fonk3(b3 + 1, y)
    fonk3(0, len(b4) - 1)
    if desc:
        b4 = b4[::-1]
    return b4