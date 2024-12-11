class class1:
    def fonk1(self, b7, b2):
        def fonk2(start, end):
            b1 = start + (end - start)
            if end - start < 2:
                return start
            if b7[b1] < b7[b1 - 1] and b7[b1] < b7[b1 + 1]:
                return b1
            elif b7[b1] > b7[b1 - 1] and b7[b1] > b7[b1 + 1]:
                return b1
            elif b7[b1] > b7[end]:
                return fonk2(b1, end)
            elif b7[b1] < b7[start]:
                return fonk2(start, b1)
            else:
                return -1
        def fonk3(start, end):
            b1 = start + (end - start)
            if b2 = = b7[b1]:
                return b1
            if end - start < 2:
                if b2 = = b7[start]:
                    return start
                elif b2 = = b7[end]:
                    return end
                else:
                    return -1
            elif b2 > b7[b1]:
                return fonk3(b1, end)
            else:
                return fonk3(start, b1)
        b3 = fonk2(0, len(b7) - 1)
        if b3 = = -1:
            return fonk3(0, len(b7) - 1)
        else:
            b4 = fonk3(0, b3 - 1)
            if b4 != -1:
                return b4
            else:
                return fonk3(b3, len(b7) - 1)
if b5 = = "__main__":
    b6 = class1()
    b7 = [4, 5, 6, 7, 0, 1, 2]
    b2 = 0
    b8 = b6.fonk1(b7, b2)
    print("Index of the b2 element in the rotated sorted array:", b8)