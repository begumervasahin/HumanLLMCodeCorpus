class class1:
    def fonk1(self, b6, b2):
        def fonk2(start, end, b6):
            b1 = start + (end - start)
            if len(b6) < 3:
                return start
            if b6[b1] < b6[b1 - 1] and b6[b1] < b6[b1 + 1]:
                return b1
            elif b6[b1] > b6[b1 - 1] and b6[b1] > b6[b1 + 1]:
                return b1
            elif b6[b1] > b6[len(b6) - 1]:
                return fonk2(b1, len(b6), b6)
            elif b6[b1] < b6[0]:
                return fonk2(start, b1, b6)
            else:
                return -1
        def fonk3(start, end, b2, b6):
            b1 = start + (end - start)
            if b2 = = b6[b1]:
                return b1
            if end - start < 3:
                if b2 = = b6[start]:
                    return start
                elif b2 = = b6[end]:
                    return end
                else:
                    return -1
            elif b2 > b6[b1]:
                return fonk3(b1, end, b2, b6)
            else:
                return fonk3(start, b1, b2, b6)
        b3 = fonk2(0, len(b6) - 1, b6)
        if b3 = = -1:
            return fonk3(0, len(b6) - 1, b2, b6)
        else:
            b4 = fonk3(0, b3 - 1, b2, b6)
            if b4 != -1:
                return b4
            else:
                return fonk3(b3, len(b6) - 1, b2, b6)
b5 = class1()
b6 = [4, 5, 6, 7, 0, 1, 2]
b2 = 0
b7 = b5.fonk1(b6, b2)
print("Index of b2 in rotated array:", b7)