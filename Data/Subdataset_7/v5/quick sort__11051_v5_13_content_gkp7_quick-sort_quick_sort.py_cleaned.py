def fonk1(b6):
    def fonk2(b6, first, last):
        b1 = b6[first]
        b2 = first + 1
        b3 = last
        while True:
            while b2 <= b3 and b6[b2] <= b1:
                b2 += 1
            while b6[b3] >= b1 and b3 >= b2:
                b3 -= 1
            if b3 < b2:
                break
            b6[b2], b6[b3] = b6[b3], b6[b2]
        b6[first], b6[b3] = b6[b3], b6[first]
        return b3
    def fonk3(b6, first, last):
        if first < last:
            b4 = fonk2(b6, first, last)
            fonk3(b6, first, b4 - 1)
            fonk3(b6, b4 + 1, last)
    fonk3(b6, 0, len(b6) - 1)
if b5 = = "__main__":
    b6 = [57, 26, 93, 77, 33, 44, 50, 20]
    fonk1(b6)
    print(b6)